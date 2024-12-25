import { createSlice, configureStore } from "@reduxjs/toolkit";
import { combineReducers } from "redux";
import reactotron from "@/config/ReactotronConfig";
import restaurantReducer from "@/redux/slices/restaurantSlice";
import { apiSlice } from "./services/api";

function createReducer(injectedReducers = {}) {
  const rootReducer = combineReducers({
    rootReducer: createSlice({
      name: "rootReducer",
      initialState: "REDUX CONFIGURED CORRECTLY",
      reducers: {},
    }).reducer,
    [apiSlice.reducerPath]: apiSlice.reducer,
    restaurant: restaurantReducer,
    ...injectedReducers,
  });
  return rootReducer;
}

let enhancers = __DEV__ ? [reactotron.createEnhancer()] : [];

const store = configureStore({
  reducer: createReducer(),
  middleware: (getDefaultMiddleware) =>
    getDefaultMiddleware().concat(apiSlice.middleware),
  enhancers: (getDefaultEnhancers) => getDefaultEnhancers().concat(enhancers),
});

export default store;
