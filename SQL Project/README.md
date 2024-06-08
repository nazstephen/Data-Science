# SQL Project

## Project Description

You're working as an analyst for Zuber, a new ride-sharing company that's launching in Chicago. Your task is to find patterns in the available information. You want to understand passenger preferences and the impact of external factors on rides.

Working with a database, you'll analyze data from competitors and test a hypothesis about the impact of weather on ride frequency.

## Instructions on Completing the Project

### Step 1: Open the Data File and Study the General Information
- File path: 
  - /datasets/games.csv

### Step 2: Prepare the Data
- Replace the column names (make them lowercase).
- Convert the data to the required types.
- Describe the columns where the data types have been changed and why.
- If necessary, decide how to deal with missing values:
  - Explain why you filled in the missing values as you did or why you decided to leave them blank.
  - Why do you think the values are missing? Give possible reasons.
  - Pay attention to the abbreviation TBD (to be determined). Specify how you intend to handle such cases.
- Calculate the total sales (the sum of sales in all regions) for each game and put these values in a separate column.

### Step 3: Analyze the Data
- Look at how many games were released in different years. Is the data for every period significant?
- Look at how sales varied from platform to platform. Choose the platforms with the greatest total sales and build a distribution based on data for each year. Find platforms that used to be popular but now have zero sales. How long does it generally take for new platforms to appear and old ones to fade?
- Determine what period you should take data for. To do so, look at your answers to the previous questions. The data should allow you to build a model for 2017.
- Work only with the data that you've decided is relevant. Disregard the data for previous years.
- Which platforms are leading in sales? Which ones are growing or shrinking? Select several potentially profitable platforms.
- Build a box plot for the global sales of all games, broken down by platform. Are the differences in sales significant? What about average sales on various platforms? Describe your findings.
- Take a look at how user and professional reviews affect sales for one popular platform (you choose). Build a scatter plot and calculate the correlation between reviews and sales. Draw conclusions.
- Keeping your conclusions in mind, compare the sales of the same games on other platforms.
- Take a look at the general distribution of games by genre. What can we say about the most profitable genres? Can you generalize about genres with high and low sales?

### Step 4: Create User Profile for Each Region
- For each region (NA, EU, JP), determine:
  - The top five platforms. Describe variations in their market shares from region to region.
  - The top five genres. Explain the difference.
  - Do ESRB ratings affect sales in individual regions?

### Step 5: Test Hypotheses
- Average user ratings of the Xbox One and PC platforms are the same. 
- Average user ratings for the Action and Sports genres are different.
- Set the alpha threshold value yourself.
- Explain:
  - How you formulated the null and alternative hypotheses 
  - What significance level you chose to test the hypotheses, and why

### Step 6: Write General Conclusion

## Description of the data
A database with info on taxi rides in Chicago:

neighborhoods table: data on city neighborhoods
- name: name of the neighborhood
- neighborhood_id: neighborhood code

cabs table: data on taxis
- cab_id: vehicle code
- vehicle_id: the vehicle's technical ID
- company_name: the company that owns the vehicle

trips table: data on rides
- trip_id: ride code
- cab_id: code of the vehicle operating the ride
- start_ts: date and time of the beginning of the ride (time rounded to the hour)
- end_ts: date and time of the end of the ride (time rounded to the hour)
- duration_seconds: ride duration in seconds
- distance_miles: ride distance in miles
- pickup_location_id: pickup neighborhood code
- dropoff_location_id: dropoff neighborhood code

weather_records table: data on weather
- record_id: weather record code
- ts: record date and time (time rounded to the hour)
- temperature: temperature when the record was taken
- description: brief description of weather conditions, e.g. "light rain" or "scattered clouds"
