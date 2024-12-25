import { StyleSheet, Text, View } from "react-native";
import React from "react";

const SearchBox = () => {
  return (
    <View
      style={{
        backgroundColor: "white",
        width: "90%",
        marginHorizontal: "5%",
        borderRadius: 100,
        padding: 10,
        position: "absolute",
        top: 50,
        zIndex: 100,
        left: 0,
        height: 60,
        shadowColor: "#000",
        shadowOffset: {
          width: 0,
          height: 2,
        },
      }}
    >
      <Text>SearchBox</Text>
    </View>
  );
};

export default SearchBox;

const styles = StyleSheet.create({});
