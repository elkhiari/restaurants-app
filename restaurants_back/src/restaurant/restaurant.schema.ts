import { Prop, raw, Schema, SchemaFactory } from '@nestjs/mongoose';
import { HydratedDocument, Types } from 'mongoose';

@Schema({
  timestamps: true,
})
export class Restaurant {
  @Prop({ required: true, trim: true })
  name: string;

  @Prop({ required: true, trim: true })
  cuisine: string;

  @Prop(
    raw({
      type: { type: String, enum: ['Point'], required: true },
      coordinates: { type: [Number], required: true },
    }),
  )
  location: { type: string; coordinates: [number, number] };

  @Prop({ required: true, trim: true })
  address: string;

  @Prop({
    type: Number,
    default: 0,
  })
  reviews: number;

  @Prop({ type: String, required: true })
  logo: string;
}

export type RestaurantDocument = HydratedDocument<Restaurant>;
export const RestaurantSchema = SchemaFactory.createForClass(Restaurant);

RestaurantSchema.index({ location: '2dsphere' });
RestaurantSchema.index({ name: 1 });
RestaurantSchema.index({ cuisine: 1 });
