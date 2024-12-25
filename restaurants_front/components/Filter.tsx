import React, { useState, useRef, useCallback, useEffect } from "react";
import { StyleSheet, Text, View, TextInput, Button } from "react-native";
import {
  BottomSheetBackdrop,
  BottomSheetModal,
  BottomSheetModalProvider,
  BottomSheetView,
} from "@gorhom/bottom-sheet";
import debounce from "lodash.debounce"; // Ensure lodash.debounce is installed
import i18n from "@/config/i18n";

interface IParams {
  latitude?: number;
  longitude?: number;
  maxDistance?: number;
  cuisine?: string;
}

interface FilterProps {
  showFilter: boolean;
  setShowFilter: (show: boolean) => void;
  setParams: React.Dispatch<React.SetStateAction<IParams>>;
  params: IParams;
}

const Filter = ({
  showFilter,
  setShowFilter,
  setParams,
  params,
}: FilterProps) => {
  const bottomSheetModalRef = useRef<BottomSheetModal>(null);

  const handleCuisineChange = useCallback(
    debounce((text: string) => {
      setParams((prev) => ({ ...prev, cuisine: text }));
    }, 500),
    []
  );

  const handleMaxDistanceChange = useCallback(
    debounce((text: string) => {
      setParams((prev) => ({ ...prev, maxDistance: parseInt(text, 10) || 0 }));
    }, 500),
    []
  );

  const handleLatitudeChange = useCallback(
    debounce((text: string) => {
      setParams((prev) => ({ ...prev, latitude: parseFloat(text) || 0 }));
    }, 500),
    []
  );

  const handleChange = useCallback(
    debounce((params: IParams) => {
      setParams((prev) => ({ ...prev, ...params }));
    }, 500),
    []
  );

  useEffect(() => {
    if (showFilter) {
      bottomSheetModalRef.current?.present();
    } else {
      bottomSheetModalRef.current?.dismiss();
    }
  }, [showFilter]);

  const renderBackdrop = useCallback(
    (props: any) => (
      <BottomSheetBackdrop
        appearsOnIndex={0}
        disappearsOnIndex={-1}
        {...props}
      />
    ),
    []
  );

  return (
    <BottomSheetModalProvider>
      <BottomSheetModal
        ref={bottomSheetModalRef}
        onDismiss={() => setShowFilter(false)}
        backdropComponent={renderBackdrop}
      >
        <BottomSheetView style={styles.contentContainer}>
          <View style={styles.content}>
            <Text style={styles.label}>{i18n.t("maxDistance")} (KM)</Text>
            <TextInput
              style={styles.input}
              placeholder={i18n.t("maxDistance")}
              onChangeText={(maxDistance) =>
                handleChange({ maxDistance: parseInt(maxDistance) * 1000 })
              }
              defaultValue={
                params.maxDistance ? (params.maxDistance / 1000).toString() : ""
              }
              keyboardType="number-pad"
            />

            <View>
              <View>
                <Text style={styles.label}>Longitude</Text>
                <TextInput
                  style={styles.input}
                  placeholder="longitude"
                  defaultValue={params.longitude?.toString() || ""}
                  onChangeText={(longitude) =>
                    handleChange({ longitude: parseFloat(longitude) })
                  }
                />
              </View>
              <View>
                <Text style={styles.label}>Latitude</Text>
                <TextInput
                  style={styles.input}
                  placeholder="latitude"
                  defaultValue={params.latitude?.toString() || ""}
                  onChangeText={(latitude) =>
                    handleChange({ latitude: parseFloat(latitude) })
                  }
                />
              </View>
            </View>
          </View>
        </BottomSheetView>
      </BottomSheetModal>
    </BottomSheetModalProvider>
  );
};

export default Filter;

const styles = StyleSheet.create({
  openButton: {
    backgroundColor: "#007BFF",
    paddingVertical: 12,
    paddingHorizontal: 24,
    borderRadius: 8,
  },
  openButtonText: {
    color: "#fff",
    fontSize: 16,
    fontWeight: "600",
  },
  backdrop: {
    ...StyleSheet.absoluteFillObject,
    backgroundColor: "rgba(0,0,0,0.5)",
  },
  content: {
    padding: 16,
    width: "100%",
    flex: 1,
  },
  label: {
    fontSize: 16,
    marginBottom: 8,
    fontWeight: "600",
  },
  input: {
    backgroundColor: "#fff",
    borderColor: "#ccc",
    borderWidth: 1,
    borderRadius: 8,
    paddingHorizontal: 12,
    paddingVertical: 8,
    fontSize: 16,
    marginBottom: 16,
  },
  actionButton: {
    backgroundColor: "#28A745",
    paddingVertical: 12,
    borderRadius: 8,
    alignItems: "center",
  },
  actionButtonText: {
    color: "#fff",
    fontSize: 16,
    fontWeight: "600",
  },
  contentContainer: {
    flex: 1,
    height: 500,
    alignItems: "center",
  },
});
