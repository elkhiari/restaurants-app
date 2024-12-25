import { StyleSheet, Text, View } from "react-native";
import React from "react";
import ImageWithFallback from "./FallbackImage";
import { AntDesign } from "@expo/vector-icons";

interface ICardProps {
  item: Restaurant;
}

const Card = ({ item }: ICardProps) => {
  return (
    <View style={styles.card}>
      <ImageWithFallback image={item.logo} />
      <View style={styles.cardContent}>
        <View style={styles.ratingContainer}>
          <View
            style={{
              display: "flex",
              flexDirection: "row",
              justifyContent: "space-between",
            }}
          >
            <AntDesign name="star" size={20} color="#ff9800" />
            <Text style={styles.ratingText}>{item.reviews}</Text>
          </View>
          {item.distance && (
            <Text style={styles.ratingText}>
              {(item.distance / 1000).toFixed(2)} KM
            </Text>
          )}
        </View>
        <View style={styles.info}>
          <View
            style={{
              display: "flex",
              flexDirection: "row",
            }}
          >
            {item.cuisine.split(",").map((cuisine, index) => (
              <View
                style={{
                  backgroundColor: "#ff9800",
                  padding: 5,
                  borderRadius: 5,
                  marginRight: 5,
                }}
                key={index}
              >
                <Text style={styles.cuisine} key={index}>
                  {cuisine}
                </Text>
              </View>
            ))}
          </View>
          <Text style={styles.restaurantName} numberOfLines={1}>
            {item.name}
          </Text>
          <Text style={styles.address} numberOfLines={1}>
            {item.address}
          </Text>
        </View>
      </View>
    </View>
  );
};

export default Card;

const styles = StyleSheet.create({
  card: {
    overflow: "hidden",
    marginVertical: 10,
    borderRadius: 5,
    backgroundColor: "#fff",
    borderColor: "#ddd",
    height: 200,
    shadowColor: "#000",
    shadowOffset: { width: 0, height: 2 },
    shadowOpacity: 0.2,
    shadowRadius: 5,
    elevation: 3,
    flexDirection: "row",
    alignItems: "center",
  },
  cardContent: {
    flex: 1,
    position: "absolute",
    backgroundColor: "rgba(0,0,0,0.5)",
    width: "100%",
    height: "100%",
    justifyContent: "space-between",
    padding: 10,
  },
  info: {},
  restaurantName: {
    fontSize: 18,
    fontWeight: "bold",
    color: "#fff",
  },
  address: {
    fontSize: 12,
    color: "#DDE2EE",
    marginVertical: 5,
  },
  ratingContainer: {
    flexDirection: "row",
    alignItems: "center",
    justifyContent: "space-between",
    marginTop: 5,
  },
  ratingText: {
    fontSize: 16,
    fontWeight: "900",
    color: "#fff",
    marginLeft: 5,
  },
  cuisine: {
    fontSize: 12,
    fontWeight: "bold",
    color: "#fff",
    // textTransform: "uppercase",
  },
});
