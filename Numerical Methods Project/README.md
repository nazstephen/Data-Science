# Numerical Methods Project

## Project Description

Rusty Bargain used car sales service is developing an app to attract new customers. In that app, you can quickly find out the market value of your car. You have access to historical data: technical specifications, trim versions, and prices. You need to build the model to determine the value. 

Rusty Bargain is interested in:

- the quality of the prediction;
- the speed of the prediction;
- the time required for training

## Project instructions
1) Download and look at the data.
2) Train different models with various hyperparameters. Compare gradient boosting methods with random forest, decision tree, and linear regression.
3) Analyze the speed and quality of the models.

## Data description
The dataset is stored in file `/datasets/car_data.csv`. download dataset.

### Features
- **DateCrawled** — date profile was downloaded from the database
- **VehicleType** — vehicle body type
- **RegistrationYear** — vehicle registration year
- **Gearbox** — gearbox type
- **Power** — power (hp)
- **Model** — vehicle model
- **Mileage** — mileage (measured in km due to dataset's regional specifics)
- **RegistrationMonth** — vehicle registration month
- **FuelType** — fuel type
- **Brand** — vehicle brand
- **NotRepaired** — vehicle repaired or not
- **DateCreated** — date of profile creation
- **NumberOfPictures** — number of vehicle pictures
- **PostalCode** — postal code of profile owner (user)
- **LastSeen** — date of the last activity of the user

###  Target
- **Price** — price (Euro)
