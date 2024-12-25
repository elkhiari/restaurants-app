import { createSlice, PayloadAction } from "@reduxjs/toolkit";
import { restaurantApi } from "../services/RestaurantApi";

interface RestaurantState {
  restaurants: Restaurant[];
}

const initialState: RestaurantState = {
  restaurants: [],
};

const restaurantSlice = createSlice({
  name: "restaurants",
  initialState,
  reducers: {
    setRestaurants(state, action: PayloadAction<Restaurant[]>) {
      state.restaurants = action.payload;
    },
  },
  extraReducers: (builder) => {
    builder.addMatcher(
      restaurantApi.endpoints.getNearRestaurants.matchFulfilled,
      (state, action) => {
        state.restaurants = action.payload;
      }
    );
  },
});

export const { setRestaurants } = restaurantSlice.actions;
export default restaurantSlice.reducer;
