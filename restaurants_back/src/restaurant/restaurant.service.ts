import { Injectable } from '@nestjs/common';
import { InjectModel } from '@nestjs/mongoose';
import { Model } from 'mongoose';
import { Restaurant, RestaurantDocument } from './restaurant.schema';

@Injectable()
export class RestaurantService {
  constructor(
    @InjectModel(Restaurant.name)
    private readonly restaurantModel: Model<RestaurantDocument>,
  ) {}

  async getNear(
    latitude?: number,
    longitude?: number,
    maxDistance = 10000,
    cuisine?: string,
  ): Promise<any[]> {
    if (latitude === undefined || longitude === undefined) {
      const query: any = {};
      if (cuisine) {
        query.cuisine = { $regex: cuisine, $options: 'i' };
      }
      return this.restaurantModel.find(query).exec();
    }

    const pipeline: any[] = [
      {
        $geoNear: {
          near: { type: 'Point', coordinates: [longitude, latitude] },
          distanceField: 'distance',
          maxDistance: maxDistance,
          spherical: true,
        },
      },
    ];

    if (cuisine) {
      pipeline.push({
        $match: { cuisine: { $regex: cuisine, $options: 'i' } },
      });
    }

    pipeline.push({ $sort: { distance: 1 } });

    return this.restaurantModel.aggregate(pipeline).exec();
  }

  async filterByName(name: string) {
    return this.restaurantModel.find({ name: new RegExp(name, 'i') }).exec();
  }

  async filterByDistance(
    latitude: number,
    longitude: number,
    maxDistance: number,
  ) {
    return this.restaurantModel
      .aggregate([
        {
          $geoNear: {
            near: {
              type: 'Point',
              coordinates: [longitude, latitude],
            },
            distanceField: 'distance',
            maxDistance: maxDistance,
            spherical: true,
          },
        },
      ])
      .exec();
  }

  async insertMany(restaurantsData: any[]) {
    try {
      const createdRestaurants =
        await this.restaurantModel.insertMany(restaurantsData);
      return createdRestaurants;
    } catch (error) {
      throw new Error('Error saving restaurants: ' + error.message);
    }
  }

  async findAll() {
    return this.restaurantModel.find().exec();
  }
}
