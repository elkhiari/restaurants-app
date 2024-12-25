import React, { useState, useEffect, useCallback, useRef } from "react";
import { useGetNearRestaurantsQuery } from "@/redux/services/RestaurantApi";
import {
  View,
  Text,
  FlatList,
  ActivityIndicator,
  StyleSheet,
  TouchableOpacity,
} from "react-native";
import { SafeAreaView } from "react-native-safe-area-context";
import Card from "@/components/Card";
import Input from "@/components/Input";
import * as Location from "expo-location";
import debounce from "lodash.debounce";
import i18n from "@/config/i18n";
import Filter from "@/components/Filter";
import { FontAwesome } from "@expo/vector-icons";

const NearbyRestaurants = () => {
  const [params, setParams] = useState<{
    latitude?: number;
    longitude?: number;
    maxDistance?: number;
    cuisine?: string;
  }>({
    maxDistance: 10000,
  });
  const [showFilter, setShowFilter] = useState<boolean>(false);

  const { data, error, isLoading, refetch, isFetching } =
    useGetNearRestaurantsQuery(params);

  useEffect(() => {
    async function getCurrentLocation() {
      let { status } = await Location.requestForegroundPermissionsAsync();
      if (status !== "granted") {
        console.error("Permission to access location was denied");
        return;
      }
      let location = await Location.getCurrentPositionAsync({});
      setParams((prev) => ({
        ...prev,
        latitude: location.coords.latitude,
        longitude: location.coords.longitude,
      }));
    }

    getCurrentLocation();
  }, []);

  const handleSearch = useCallback(
    debounce(
      (text: string) => setParams((prev) => ({ ...prev, cuisine: text })),
      500
    ),
    []
  );

  if (isLoading)
    return (
      <View
        style={{
          flex: 1,
          justifyContent: "center",
          alignItems: "center",
        }}
      >
        <ActivityIndicator size="large" color="#0000ff" />;
      </View>
    );
  if (error) {
    console.error(error);
    return (
      <View
        style={{
          flex: 1,
          justifyContent: "center",
          alignItems: "center",
        }}
      >
        <Text>Error fetching data</Text>
      </View>
    );
  }

  return (
    <>
      <SafeAreaView style={styles.container}>
        <View style={styles.header}>
          <Input
            placeholder={i18n.t("searchInput")}
            onChangeText={handleSearch}
            style={styles.input}
          />
          <TouchableOpacity
            onPress={() => {
              setShowFilter(true);
            }}
            style={styles.filterButton}
          >
            <FontAwesome name="filter" size={24} color="black" />
          </TouchableOpacity>
        </View>
        {data && data.length > 0 ? (
          <FlatList
            refreshing={isFetching}
            onRefresh={refetch}
            data={data}
            style={styles.list}
            keyExtractor={(item) => item._id}
            renderItem={({ item }) => <Card item={item} />}
          />
        ) : (
          <Text style={styles.noData}>{i18n.t("noRestaurantsFound")}</Text>
        )}
        <Filter
          showFilter={showFilter}
          setShowFilter={setShowFilter}
          setParams={setParams}
          params={params}
        />
      </SafeAreaView>
    </>
  );
};

const styles = StyleSheet.create({
  container: { flex: 1 },
  header: {
    flexDirection: "row",
    alignItems: "center",
    paddingHorizontal: 16,
    paddingVertical: 10,
  },
  input: {
    flex: 1,
    height: 40,
    paddingLeft: 10,
    fontSize: 16,
  },
  filterButton: {
    marginLeft: 10,
    padding: 10,
    borderRadius: 5,
    backgroundColor: "#fff",
    justifyContent: "center",
    alignItems: "center",
  },
  list: { flex: 1, paddingHorizontal: 20 },
  noData: { textAlign: "center", marginTop: 20 },
});

export default NearbyRestaurants;
