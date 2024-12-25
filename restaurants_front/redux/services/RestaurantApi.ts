import { apiSlice } from "./api";

export const restaurantApi = apiSlice.injectEndpoints({
  endpoints: (builder) => ({
    getNearRestaurants: builder.query<
      Restaurant[],
      {
        latitude?: number;
        longitude?: number;
        maxDistance?: number;
        cuisine?: string;
      }
    >({
      query: ({ latitude, longitude, maxDistance, cuisine }) => {
        const params: any = {};

        if (latitude && longitude && maxDistance) {
          params.latitude = latitude;
          params.longitude = longitude;
          params.maxDistance = maxDistance;
        }

        if (cuisine) {
          params.cuisine = cuisine;
        }

        return {
          url: `restaurants/getnear`,
          params,
        };
      },
    }),
  }),
});

export const { useGetNearRestaurantsQuery } = restaurantApi;
