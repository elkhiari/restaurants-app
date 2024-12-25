import json

transformed_data = []
data =  [
  {
    "location": [
      34.020882,
      -6.84165
    ],
    "_id": "676afc9195fa6025007c69ca",
    "name": "Dar Naji",
    "cuisine": "Moroccan",
    "address": "Rabat",
    "reviews": 4.2,
    "logo": "https://itin-dev.sfo2.cdn.digitaloceanspaces.com/freeImage/WDdNqNRfgKE3NyNT6Px0uVmzrasmCjWX",
    "__v": 0,
    "createdAt": "2024-12-24T18:25:21.388Z",
    "updatedAt": "2024-12-24T18:25:21.388Z"
  },
  {
    "location": [
      34.022123,
      -6.832399
    ],
    "_id": "676afc9195fa6025007c69cb",
    "name": "Le Dhow | Restaurant - Lounge",
    "cuisine": "Seafood",
    "address": "Avenue Al Marsa Quai Des Oudayas, 10000 Rabat",
    "reviews": 3.9,
    "logo": "https://itin-dev.sfo2.cdn.digitaloceanspaces.com/freeImage/WDdNqNRfgKE3NyNT6Px0uVmzrasmCjWX",
    "__v": 0,
    "createdAt": "2024-12-24T18:25:21.389Z",
    "updatedAt": "2024-12-24T18:25:21.389Z"
  },
  {
    "location": [
      34.033507,
      -6.82704
    ],
    "_id": "676afc9195fa6025007c69cc",
    "name": "Villa Mandarine Rabat",
    "cuisine": "Moroccan, French",
    "address": "19, Rue Ouled Bousbaa, Soussi, Rabat",
    "reviews": 4,
    "logo": "https://fastly.4sqi.net/img/general/original/18662866_X8Lj8SmHCseu4iOu1aDsIUjA_Kz3bWevgyBoxUlIAwY.jpg",
    "__v": 0,
    "createdAt": "2024-12-24T18:25:21.389Z",
    "updatedAt": "2024-12-24T18:25:21.389Z"
  },
  {
    "location": [
      34.020834,
      -6.835349
    ],
    "_id": "676afc9195fa6025007c69cd",
    "name": "Le Grand Comptoir",
    "cuisine": "French, Mediterranean",
    "address": "Rabat",
    "reviews": 4.3,
    "logo": "https://media-cdn.tripadvisor.com/media/photo-s/19/4a/99/be/photo4jpg.jpg",
    "__v": 0,
    "createdAt": "2024-12-24T18:25:21.389Z",
    "updatedAt": "2024-12-24T18:25:21.389Z"
  },
  {
    "location": [
      34.02039,
      -6.84912
    ],
    "_id": "676afc9195fa6025007c69ce",
    "name": "Il Giardino",
    "cuisine": "Italian",
    "address": "2 bis Avenue Ahmed el Yazidi, Rabat",
    "reviews": 3.4,
    "logo": "https://fastly.4sqi.net/img/general/original/5392339_3xLhXirNlhmtZuN-ceYXbAy30WuFhR_KB3xr38-Br4k.jpg",
    "__v": 0,
    "createdAt": "2024-12-24T18:25:21.389Z",
    "updatedAt": "2024-12-24T18:25:21.389Z"
  },
  {
    "location": [
      34.02205,
      -6.837485
    ],
    "_id": "676afc9195fa6025007c69cf",
    "name": "Cosmopolitan",
    "cuisine": "International",
    "address": "Rabat",
    "reviews": 3.6,
    "logo": "https://fastly.4sqi.net/img/general/original/40795089_6bf5KIbQqsF1TYhiHkDxaCGtp9Sr_pZ-RQNnWUAqzDA.jpg",
    "__v": 0,
    "createdAt": "2024-12-24T18:25:21.390Z",
    "updatedAt": "2024-12-24T18:25:21.390Z"
  },
  {
    "location": [
      34.019389,
      -6.842525
    ],
    "_id": "676afc9195fa6025007c69d0",
    "name": "Restaurant Le Ziryab",
    "cuisine": "Moroccan, Mediterranean",
    "address": "Rue Des Consuls 10 (Impasse Ennajar), Rabat",
    "reviews": 4.6,
    "logo": "https://fastly.4sqi.net/img/general/original/18662866_Vjap9mRjOmvAC9ctjQjnapZ88wo4iRs0wpL_GsHkmMw.jpg",
    "__v": 0,
    "createdAt": "2024-12-24T18:25:21.390Z",
    "updatedAt": "2024-12-24T18:25:21.390Z"
  },
  {
    "location": [
      34.020002,
      -6.83591
    ],
    "_id": "676afc9195fa6025007c69d1",
    "name": "Le Grill Robuchon",
    "cuisine": "French",
    "address": "10104 Rabat",
    "reviews": 3.6,
    "logo": "https://lh3.googleusercontent.com/p/AF1QipNPR3XTFifnpIxvFXM3TdsceNxkkQ0M4FyyjxyL=s680-w680-h510",
    "__v": 0,
    "createdAt": "2024-12-24T18:25:21.390Z",
    "updatedAt": "2024-12-24T18:25:21.390Z"
  },
  {
    "location": [
      34.019951,
      -6.833265
    ],
    "_id": "676b01c495fa6025007c69d8",
    "name": "Tangerino",
    "cuisine": "Mediterranean, Seafood",
    "address": "Rabat, Morocco",
    "reviews": 4.5,
    "logo": "https://lh5.googleusercontent.com/p/AF1QipN-wA32VOtYDgjCdFVsDJn4KBCt_GdXy7mvjPCH=w408-h306-k-no",
    "__v": 0,
    "createdAt": "2024-12-24T18:47:32.014Z",
    "updatedAt": "2024-12-24T18:47:32.014Z"
  },
  {
    "location": [
      34.019003,
      -6.835421
    ],
    "_id": "676b01c495fa6025007c69d9",
    "name": "El Chapo",
    "cuisine": "Mediterranean, Moroccan",
    "address": "Rabat, Morocco",
    "reviews": 4.4,
    "logo": "https://dynamic-media-cdn.tripadvisor.com/media/photo-o/19/10/e7/7a/restaurant-marocain-gastronomi.jpg?w=700&h=-1&s=1",
    "__v": 0,
    "createdAt": "2024-12-24T18:47:32.015Z",
    "updatedAt": "2024-12-24T18:47:32.015Z"
  },
  {
    "location": [
      34.021572,
      -6.841138
    ],
    "_id": "676b01c495fa6025007c69da",
    "name": "Baiana Lounge",
    "cuisine": "International",
    "address": "Rabat, Morocco",
    "reviews": 4.3,
    "logo": "https://lh5.googleusercontent.com/p/AF1QipM3AvkvCGXP0Oek6Xc2TuLH_Eur9SmerahyYz4Q=w408-h506-k-no",
    "__v": 0,
    "createdAt": "2024-12-24T18:47:32.016Z",
    "updatedAt": "2024-12-24T18:47:32.016Z"
  },
  {
    "location": [
      34.035451,
      -6.826237
    ],
    "_id": "676b01c495fa6025007c69db",
    "name": "Al Warda",
    "cuisine": "Moroccan",
    "address": "Sofitel, Rabat, Morocco",
    "reviews": 4.5,
    "logo": "https://lh5.googleusercontent.com/p/AF1QipPcCPZkfhrGPkSokNh-W3S5DFCdqPnzpMp16BCZ=w408-h544-k-no",
    "__v": 0,
    "createdAt": "2024-12-24T18:47:32.016Z",
    "updatedAt": "2024-12-24T18:47:32.016Z"
  },
  {
    "location": [
      34.03412,
      -6.82733
    ],
    "_id": "676b01c495fa6025007c69dc",
    "name": "Flamme",
    "cuisine": "International",
    "address": "Rabat, Morocco",
    "reviews": 4.2,
    "logo": "https://lh5.googleusercontent.com/p/AF1QipOMLD6TtPR318D2gxhqPFrVmxkzmeGjF0e6Wpc=w426-h240-k-no",
    "__v": 0,
    "createdAt": "2024-12-24T18:47:32.016Z",
    "updatedAt": "2024-12-24T18:47:32.016Z"
  },
  {
    "location": [
      34.021115,
      -6.83482
    ],
    "_id": "676b01c495fa6025007c69dd",
    "name": "Brasserie Marie",
    "cuisine": "French",
    "address": "Rabat, Morocco",
    "reviews": 4.3,
    "logo": "https://www.fourseasons.com/alt/img-opt/~70.1530.0,0000-312,4971-3000,0000-1687,5000/publish/content/dam/fourseasons/images/web/DJB/DJB_2111_original.jpg",
    "__v": 0,
    "createdAt": "2024-12-24T18:47:32.017Z",
    "updatedAt": "2024-12-24T18:47:32.017Z"
  },
  {
    "location": [
      34.03283,
      -6.82971
    ],
    "_id": "676b01c495fa6025007c69de",
    "name": "Noora Lobby Lounge",
    "cuisine": "Café, Moroccan Pastries",
    "address": "Rabat, Morocco",
    "reviews": 4.2,
    "logo": "https://lh5.googleusercontent.com/p/AF1QipOxVgIckWTqk081zmF89KsC5ZnIrA_4Xcq1Kj0=w426-h240-k-no",
    "__v": 0,
    "createdAt": "2024-12-24T18:47:32.017Z",
    "updatedAt": "2024-12-24T18:47:32.017Z"
  },
  {
    "location": [
      33.587428,
      -7.626575
    ],
    "_id": "676b029f95fa6025007c69e6",
    "name": "Iloli",
    "cuisine": "Japanese",
    "address": "33 angle rues Najib Mahfoud et Tawfik El Hakim, Quartier Gauthier, Casablanca, Morocco",
    "reviews": 4.3,
    "logo": "https://lh5.googleusercontent.com/p/AF1QipN-wA32VOtYDgjCdFVsDJn4KBCt_GdXy7mvjPCH=w408-h306-k-no",
    "__v": 0,
    "createdAt": "2024-12-24T18:51:11.787Z",
    "updatedAt": "2024-12-24T18:51:11.787Z"
  },
  {
    "location": [
      33.589886,
      -7.622267
    ],
    "_id": "676b029f95fa6025007c69e7",
    "name": "Vieilles Canailles",
    "cuisine": "French",
    "address": "20013 Casablanca, Morocco",
    "reviews": 4.6,
    "logo": "https://dynamic-media-cdn.tripadvisor.com/media/photo-o/19/10/e7/7a/restaurant-marocain-gastronomi.jpg?w=700&h=-1&s=1",
    "__v": 0,
    "createdAt": "2024-12-24T18:51:11.787Z",
    "updatedAt": "2024-12-24T18:51:11.787Z"
  },
  {
    "location": [
      33.593466,
      -7.618855
    ],
    "_id": "676b029f95fa6025007c69e8",
    "name": "El Gousto",
    "cuisine": "Italian",
    "address": "Casablanca, Morocco",
    "reviews": 4.2,
    "logo": "https://lh5.googleusercontent.com/p/AF1QipM3AvkvCGXP0Oek6Xc2TuLH_Eur9SmerahyYz4Q=w408-h506-k-no",
    "__v": 0,
    "createdAt": "2024-12-24T18:51:11.788Z",
    "updatedAt": "2024-12-24T18:51:11.788Z"
  },
  {
    "location": [
      33.58075,
      -7.620749
    ],
    "_id": "676b029f95fa6025007c69e9",
    "name": "Tony Hall",
    "cuisine": "Italian",
    "address": "20240 Casablanca, Morocco",
    "reviews": 4.4,
    "logo": "https://lh5.googleusercontent.com/p/AF1QipPcCPZkfhrGPkSokNh-W3S5DFCdqPnzpMp16BCZ=w408-h544-k-no",
    "__v": 0,
    "createdAt": "2024-12-24T18:51:11.788Z",
    "updatedAt": "2024-12-24T18:51:11.788Z"
  },
  {
    "location": [
      33.598057,
      -7.611833
    ],
    "_id": "676b029f95fa6025007c69ea",
    "name": "Brasserie la Bavaroise",
    "cuisine": "French",
    "address": "133, rue Allal Ben Abdellah, Casablanca, Morocco",
    "reviews": 4.5,
    "logo": "https://lh5.googleusercontent.com/p/AF1QipOMLD6TtPR318D2gxhqPFrVmxkzmeGjF0e6Wpc=w426-h240-k-no",
    "__v": 0,
    "createdAt": "2024-12-24T18:51:11.788Z",
    "updatedAt": "2024-12-24T18:51:11.788Z"
  },
  {
    "location": [
      33.59438,
      -7.624273
    ],
    "_id": "676b029f95fa6025007c69eb",
    "name": "Don Camillo",
    "cuisine": "Spanish",
    "address": "Casablanca, Morocco",
    "reviews": 3.7,
    "logo": "https://lh5.googleusercontent.com/p/AF1QipM5FNTINCH-93F5BpLU3VyNRT6m4tWbVofl4BA=w408-h306-k-no",
    "__v": 0,
    "createdAt": "2024-12-24T18:51:11.788Z",
    "updatedAt": "2024-12-24T18:51:11.788Z"
  },
  {
    "location": [
      33.588461,
      -7.613866
    ],
    "_id": "676b029f95fa6025007c69ec",
    "name": "Le QuatorZe",
    "cuisine": "French",
    "address": "Casablanca, Morocco",
    "reviews": 4.3,
    "logo": "https://www.fourseasons.com/alt/img-opt/~70.1530.0,0000-312,4971-3000,0000-1687,5000/publish/content/dam/fourseasons/images/web/DJB/DJB_2111_original.jpg",
    "__v": 0,
    "createdAt": "2024-12-24T18:51:11.788Z",
    "updatedAt": "2024-12-24T18:51:11.788Z"
  },
  {
    "location": [
      33.685012,
      -7.391068
    ],
    "_id": "676b02f795fa6025007c69ee",
    "name": "Marius Mohammedia",
    "cuisine": "Italian, French",
    "address": "Angle rue Bourgogne et Biranzarane, Mohammedia 28800, Morocco",
    "reviews": 4.5,
    "logo": "https://lh5.googleusercontent.com/p/AF1QipN-wA32VOtYDgjCdFVsDJn4KBCt_GdXy7mvjPCH=w408-h306-k-no",
    "__v": 0,
    "createdAt": "2024-12-24T18:52:39.660Z",
    "updatedAt": "2024-12-24T18:52:39.660Z"
  },
  {
    "location": [
      33.693729,
      -7.385129
    ],
    "_id": "676b02f795fa6025007c69ef",
    "name": "Restaurant du Port",
    "cuisine": "French, Seafood",
    "address": "1 Rue Du Port, Mohammedia 28810, Morocco",
    "reviews": 4.5,
    "logo": "https://lh5.googleusercontent.com/p/AF1QipM3AvkvCGXP0Oek6Xc2TuLH_Eur9SmerahyYz4Q=w408-h306-k-no",
    "__v": 0,
    "createdAt": "2024-12-24T18:52:39.660Z",
    "updatedAt": "2024-12-24T18:52:39.660Z"
  },
  {
    "location": [
      33.687578,
      -7.387012
    ],
    "_id": "676b02f795fa6025007c69f0",
    "name": "Pizzeria Paolo",
    "cuisine": "Italian, European",
    "address": "Mohammedia, Morocco",
    "reviews": 4.3,
    "logo": "https://lh5.googleusercontent.com/p/AF1QipPcCPZkfhrGPkSokNh-W3S5DFCdqPnzpMp16BCZ=w408-h544-k-no",
    "__v": 0,
    "createdAt": "2024-12-24T18:52:39.660Z",
    "updatedAt": "2024-12-24T18:52:39.660Z"
  },
  {
    "location": [
      33.690842,
      -7.388746
    ],
    "_id": "676b02f795fa6025007c69f1",
    "name": "Red Chilli",
    "cuisine": "French, International",
    "address": "618 Bd Abdelkrim Al Khattabi, Mohammedia, Morocco",
    "reviews": 4.2,
    "logo": "https://lh5.googleusercontent.com/p/AF1QipOMLD6TtPR318D2gxhqPFrVmxkzmeGjF0e6Wpc=w426-h240-k-no",
    "__v": 0,
    "createdAt": "2024-12-24T18:52:39.660Z",
    "updatedAt": "2024-12-24T18:52:39.660Z"
  },
  {
    "location": [
      33.688342,
      -7.386544
    ],
    "_id": "676b02f795fa6025007c69f2",
    "name": "SUNNY HOME",
    "cuisine": "Italian, French",
    "address": "Mohammedia, Morocco",
    "reviews": 4.3,
    "logo": "https://lh5.googleusercontent.com/p/AF1QipM5FNTINCH-93F5BpLU3VyNRT6m4tWbVofl4BA=w408-h306-k-no",
    "__v": 0,
    "createdAt": "2024-12-24T18:52:39.660Z",
    "updatedAt": "2024-12-24T18:52:39.660Z"
  },
  {
    "location": [
      33.691842,
      -7.389744
    ],
    "_id": "676b02f795fa6025007c69f3",
    "name": "Bistrot du Parc",
    "cuisine": "French, International",
    "address": "Mohammedia, Morocco",
    "reviews": 4.4,
    "logo": "https://lh5.googleusercontent.com/p/AF1QipM3AvkvCGXP0Oek6Xc2TuLH_Eur9SmerahyYz4Q=w408-h306-k-no",
    "__v": 0,
    "createdAt": "2024-12-24T18:52:39.660Z",
    "updatedAt": "2024-12-24T18:52:39.660Z"
  },
  {
    "location": [
      33.694842,
      -7.390744
    ],
    "_id": "676b02f795fa6025007c69f4",
    "name": "Big Bamboo Café",
    "cuisine": "Italian, European",
    "address": "Mohammedia, Morocco",
    "reviews": 4.5,
    "logo": "https://lh5.googleusercontent.com/p/AF1QipOMLD6TtPR318D2gxhqPFrVmxkzmeGjF0e6Wpc=w426-h240-k-no",
    "__v": 0,
    "createdAt": "2024-12-24T18:52:39.660Z",
    "updatedAt": "2024-12-24T18:52:39.660Z"
  },
  {
    "location": [
      33.692842,
      -7.387744
    ],
    "_id": "676b02f795fa6025007c69f5",
    "name": "Restaurant Elbao",
    "cuisine": "Moroccan, Seafood",
    "address": "Mohammedia, Morocco",
    "reviews": 4.2,
    "logo": "https://lh5.googleusercontent.com/p/AF1QipM5FNTINCH-93F5BpLU3VyNRT6m4tWbVofl4BA=w408-h306-k-no",
    "__v": 0,
    "createdAt": "2024-12-24T18:52:39.660Z",
    "updatedAt": "2024-12-24T18:52:39.660Z"
  },
  {
    "location": [
      33.689842,
      -7.386744
    ],
    "_id": "676b02f795fa6025007c69f6",
    "name": "Chez Madame Andrée - Hotel Sphinx",
    "cuisine": "French, Seafood",
    "address": "Mohammedia, Morocco",
    "reviews": 4.6,
    "logo": "https://lh5.googleusercontent.com/p/AF1QipOMLD6TtPR318D2gxhqPFrVmxkzmeGjF0e6Wpc=w426-h240-k-no",
    "__v": 0,
    "createdAt": "2024-12-24T18:52:39.661Z",
    "updatedAt": "2024-12-24T18:52:39.661Z"
  },
  {
    "location": [
      33.693842,
      -7.389744
    ],
    "_id": "676b02f795fa6025007c69f7",
    "name": "YOKA Sushi",
    "cuisine": "Chinese, Japanese",
    "address": "CENTER PARK 20800, Rue Tripoli, Mohammedia, Morocco",
    "reviews": 4.5,
    "logo": "https://lh5.googleusercontent.com/p/AF1QipM3AvkvCGXP0Oek6Xc2TuLH_Eur9SmerahyYz4Q=w408-h306-k-no",
    "__v": 0,
    "createdAt": "2024-12-24T18:52:39.661Z",
    "updatedAt": "2024-12-24T18:52:39.661Z"
  },
  {
    "location": [
      35.785609,
      -5.812751
    ],
    "_id": "676b03ef95fa6025007c6a00",
    "name": "El Morocco Club",
    "cuisine": "Mediterranean, Fusion",
    "address": "Kasbah, Tangier, Morocco",
    "reviews": 4.5,
    "logo": "https://tse3.mm.bing.net/th?id=OIP.goqPwBiHl8qmG1aSkMadvAHaFj&pid=Api",
    "__v": 0,
    "createdAt": "2024-12-24T18:56:47.835Z",
    "updatedAt": "2024-12-24T18:56:47.835Z"
  },
  {
    "location": [
      35.783985,
      -5.8112
    ],
    "_id": "676b03ef95fa6025007c6a01",
    "name": "Anna e Paolo",
    "cuisine": "Italian",
    "address": "Tangier, Morocco",
    "reviews": 4.3,
    "logo": "https://tse2.mm.bing.net/th?id=OIP.xFk5WhYBij2JVlWLp4quuQHaFj&pid=Api",
    "__v": 0,
    "createdAt": "2024-12-24T18:56:47.835Z",
    "updatedAt": "2024-12-24T18:56:47.835Z"
  },
  {
    "location": [
      35.778539,
      -5.813867
    ],
    "_id": "676b03ef95fa6025007c6a02",
    "name": "Le Saveur du Poisson",
    "cuisine": "Seafood",
    "address": "Escalier Waller 2, Rue de la Liberté, Tangier, Morocco",
    "reviews": 4.2,
    "logo": "https://tse4.mm.bing.net/th?id=OIP.9KVwU3Yk6xqjJD6qFVUwNwHaFj&pid=Api",
    "__v": 0,
    "createdAt": "2024-12-24T18:56:47.835Z",
    "updatedAt": "2024-12-24T18:56:47.835Z"
  },
  {
    "location": [
      35.7802,
      -5.8125
    ],
    "_id": "676b03ef95fa6025007c6a03",
    "name": "Dar Harruch",
    "cuisine": "Moroccan, Spanish",
    "address": "Mohammed Torres Medina, 90030 Tangier, Morocco",
    "reviews": 4.4,
    "logo": "https://tse4.mm.bing.net/th?id=OIP.eG3E1a_tTFCPrB8s5eoC4AHaFj&pid=Api",
    "__v": 0,
    "createdAt": "2024-12-24T18:56:47.835Z",
    "updatedAt": "2024-12-24T18:56:47.835Z"
  },
  {
    "location": [
      35.7805,
      -5.8089
    ],
    "_id": "676b03ef95fa6025007c6a04",
    "name": "El Tangerino",
    "cuisine": "Moroccan, International",
    "address": "186 Avenue Mohamed VI, Corniche de Tanger, 90000 Tangier, Morocco",
    "reviews": 4.3,
    "logo": "https://tse3.mm.bing.net/th?id=OIP.l3pIj--j9yY1bSXzBCHI8QHaFj&pid=Api",
    "__v": 0,
    "createdAt": "2024-12-24T18:56:47.835Z",
    "updatedAt": "2024-12-24T18:56:47.835Z"
  },
  {
    "location": [
      35.7896,
      -5.8322
    ],
    "_id": "676b03ef95fa6025007c6a05",
    "name": "Café Hafa",
    "cuisine": "Café, Moroccan",
    "address": "Rue Hafa, Tangier, Morocco",
    "reviews": 4.2,
    "logo": "https://tse3.mm.bing.net/th?id=OIP.3QUhCaiEOtKoRJo-9q8nAwHaEK&pid=Api",
    "__v": 0,
    "createdAt": "2024-12-24T18:56:47.835Z",
    "updatedAt": "2024-12-24T18:56:47.835Z"
  },
  {
    "location": [
      35.785,
      -5.812
    ],
    "_id": "676b03ef95fa6025007c6a06",
    "name": "Chez Hassan Bab Kasbah",
    "cuisine": "Moroccan",
    "address": "Rue de la Kasbah, 90000 Tangier Medina, Morocco",
    "reviews": 4.5,
    "logo": "https://tse3.mm.bing.net/th?id=OIP.uHwr6eo89Lnn2R1Q6Y7dFwHaEK&pid=Api",
    "__v": 0,
    "createdAt": "2024-12-24T18:56:47.835Z",
    "updatedAt": "2024-12-24T18:56:47.835Z"
  },
  {
    "location": [
      34.259922,
      -6.588244
    ],
    "_id": "676b043195fa6025007c6a08",
    "name": "Merzouga",
    "cuisine": "Seafood",
    "address": "Kenitra, Morocco",
    "reviews": 4.5,
    "logo": "https://tse4.mm.bing.net/th?id=OIP.XkeSOlFyVSpuZJzWfVaTnQHaEK&pid=Api",
    "__v": 0,
    "createdAt": "2024-12-24T18:57:53.988Z",
    "updatedAt": "2024-12-24T18:57:53.988Z"
  },
  {
    "location": [
      34.252231,
      -6.58992
    ],
    "_id": "676b043195fa6025007c6a09",
    "name": "O Cassecroute",
    "cuisine": "Fast Food, International",
    "address": "Kenitra, Morocco",
    "reviews": 4.3,
    "logo": "https://tse2.mm.bing.net/th?id=OIP.eZQXnGVvvKJMG7X7nMle5AHaE7&pid=Api",
    "__v": 0,
    "createdAt": "2024-12-24T18:57:53.988Z",
    "updatedAt": "2024-12-24T18:57:53.988Z"
  },
  {
    "location": [
      34.254321,
      -6.587942
    ],
    "_id": "676b043195fa6025007c6a0a",
    "name": "Metropole",
    "cuisine": "Moroccan, International",
    "address": "Kenitra, Morocco",
    "reviews": 4.2,
    "logo": "https://tse4.mm.bing.net/th?id=OIP.7hOTRuW3b-fg8ZCh7ZPnkAHaEK&pid=Api",
    "__v": 0,
    "createdAt": "2024-12-24T18:57:53.988Z",
    "updatedAt": "2024-12-24T18:57:53.988Z"
  },
  {
    "location": [
      34.253672,
      -6.5863
    ],
    "_id": "676b043195fa6025007c6a0b",
    "name": "River Club",
    "cuisine": "International",
    "address": "Kenitra, Morocco",
    "reviews": 4.4,
    "logo": "https://tse1.mm.bing.net/th?id=OIP.R7zMElOwBum5g9VmvwF42gHaEK&pid=Api",
    "__v": 0,
    "createdAt": "2024-12-24T18:57:53.989Z",
    "updatedAt": "2024-12-24T18:57:53.989Z"
  },
  {
    "location": [
      34.257862,
      -6.584903
    ],
    "_id": "676b043195fa6025007c6a0c",
    "name": "Delicia Ice",
    "cuisine": "Desserts",
    "address": "Kenitra, Morocco",
    "reviews": 4.6,
    "logo": "https://tse2.mm.bing.net/th?id=OIP.dGBLV9O3GB12Cbc3dFyuegHaEo&pid=Api",
    "__v": 0,
    "createdAt": "2024-12-24T18:57:53.989Z",
    "updatedAt": "2024-12-24T18:57:53.989Z"
  },
  {
    "location": [
      34.258291,
      -6.590242
    ],
    "_id": "676b043195fa6025007c6a0d",
    "name": "Yamal Acham Knitra",
    "cuisine": "Middle Eastern",
    "address": "Kenitra, Morocco",
    "reviews": 4.3,
    "logo": "https://tse3.mm.bing.net/th?id=OIP.ynQa1V7FwAvE6l3J1oPC6QHaEK&pid=Api",
    "__v": 0,
    "createdAt": "2024-12-24T18:57:53.989Z",
    "updatedAt": "2024-12-24T18:57:53.989Z"
  },
  {
    "location": [
      34.255472,
      -6.589213
    ],
    "_id": "676b043195fa6025007c6a0e",
    "name": "Chhiwate Ryad Naji",
    "cuisine": "Moroccan",
    "address": "Kenitra, Morocco",
    "reviews": 4.2,
    "logo": "https://tse4.mm.bing.net/th?id=OIP.PEm8cQX9CJNz62gkhR3xrAHaEK&pid=Api",
    "__v": 0,
    "createdAt": "2024-12-24T18:57:53.989Z",
    "updatedAt": "2024-12-24T18:57:53.989Z"
  },
  {
    "location": [
      34.252572,
      -6.590833
    ],
    "_id": "676b043195fa6025007c6a0f",
    "name": "Dar Tajine",
    "cuisine": "Moroccan",
    "address": "Kenitra, Morocco",
    "reviews": 4.5,
    "logo": "https://tse4.mm.bing.net/th?id=OIP.P89BvTth7WbQaL3CMg1aiQHaEK&pid=Api",
    "__v": 0,
    "createdAt": "2024-12-24T18:57:53.989Z",
    "updatedAt": "2024-12-24T18:57:53.989Z"
  },
  {
    "location": [
      34.253871,
      -6.588941
    ],
    "_id": "676b043195fa6025007c6a10",
    "name": "Yours Cafe Patisserie",
    "cuisine": "Café, Pastries",
    "address": "Kenitra, Morocco",
    "reviews": 4.4,
    "logo": "https://tse4.mm.bing.net/th?id=OIP.S4NhCgNNj-Jh9-yRyl6wqAHaE7&pid=Api",
    "__v": 0,
    "createdAt": "2024-12-24T18:57:53.989Z",
    "updatedAt": "2024-12-24T18:57:53.989Z"
  },
  {
    "location": [
      34.256712,
      -6.589402
    ],
    "_id": "676b043195fa6025007c6a11",
    "name": "Restaurant Chez L'italienne",
    "cuisine": "Italian, Mediterranean",
    "address": "Kenitra, Morocco",
    "reviews": 4.6,
    "logo": "https://tse3.mm.bing.net/th?id=OIP.TqVJ4syJjYqMwdmAj-QZPAHaE7&pid=Api",
    "__v": 0,
    "createdAt": "2024-12-24T18:57:53.989Z",
    "updatedAt": "2024-12-24T18:57:53.989Z"
  }
]
for item in data:
    transformed_item = {
        "name": item["name"],
        "cuisine": item["cuisine"],
        "location": {
            "type": "Point",
            "coordinates": [item["location"][1], item["location"][0]]  # Inversion des coordonnées
        },
        "address": item["address"],
        "reviews": item["reviews"],
        "logo": item["logo"]
    }
    transformed_data.append(transformed_item)

# Affichage du résultat transformé
print(json.dumps(transformed_data, indent=2))