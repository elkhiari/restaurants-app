import Reactotron from "reactotron-react-native";
import AsyncStorage from "@react-native-async-storage/async-storage";
import { reactotronRedux } from "reactotron-redux";

const reactotron = Reactotron.configure({
  name: "React Native Demo",
})
  .setAsyncStorageHandler(AsyncStorage)
  .useReactNative({
    overlay: true,
    networking: {
      ignoreUrls: /symbolicate/,
    },
    errors: { veto: (stackFrame) => false },
    editor: true,
  })
  .use(reactotronRedux())
  .connect();

export default reactotron;
