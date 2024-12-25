import { useState } from "react";
import { Image, StyleSheet } from "react-native";

function ImageWithFallback({ image }: { image: string }) {
  const [imageError, setImageError] = useState(false);

  return (
    <Image
      source={
        imageError
          ? require("@/assets/images/default-fallback-image.png")
          : { uri: image }
      }
      style={styles.logo}
      resizeMode="cover"
      onError={() => setImageError(true)}
    />
  );
}

const styles = StyleSheet.create({
  logo: {
    width: "100%",
    height: "100%",
    resizeMode: "contain",
  },
});

export default ImageWithFallback;
