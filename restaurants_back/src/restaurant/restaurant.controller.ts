import { Body, Controller, Get, Post, Query } from '@nestjs/common';
import { RestaurantService } from './restaurant.service';

@Controller('restaurants')
export class RestaurantController {
  constructor(private readonly restaurantService: RestaurantService) {}

  @Get('getnear')
  async getNear(
    @Query('latitude') latitude?: string,
    @Query('longitude') longitude?: string,
    @Query('maxDistance') maxDistance?: string,
    @Query('cuisine') cuisine?: string,
  ) {
    const lat = latitude ? parseFloat(latitude) : undefined;
    const lon = longitude ? parseFloat(longitude) : undefined;
    const maxDist = maxDistance ? parseInt(maxDistance, 10) : undefined;

    return this.restaurantService.getNear(lat, lon, maxDist, cuisine);
  }

  @Post('insert/many')
  async saveAll(@Body() restaurantsData: any[]) {
    return this.restaurantService.insertMany(restaurantsData);
  }

  @Get()
  async findAll() {
    return this.restaurantService.findAll();
  }
}
