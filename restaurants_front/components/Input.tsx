import {
  StyleSheet,
  Text,
  TextInputProps,
  View,
  TextInput,
} from "react-native";
import React from "react";

const Input = (Props: TextInputProps) => {
  return <TextInput {...Props} style={[styles.input, Props.style]} />;
};

export default Input;

const styles = StyleSheet.create({
  input: {
    height: 40,
    backgroundColor: "#fff",
    borderRadius: 5,
    padding: 10,
  },
});
