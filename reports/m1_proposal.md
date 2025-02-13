## Section 1
### Motivation and Purpose

Hong Kong is a major global hub with complex cross-border movement patterns, making efficient passenger traffic management crucial for both policymakers and public service agencies. 
Our team, acting as data science consultants, aims to provide actionable insights through a well-structured, interactive dashboard.

### Target Audience:

This dashboard is designed for public policymakers, transportation authorities, and border control agencies who need real-time, data-driven insights to manage the daily inflow and outflow of passengers at control points.

### Problem Statement:

Hong Kong’s control points facilitate a large volume of cross-border movements, but without clear visualization tools, identifying trends and making informed decisions can be challenging. 
Fragmented or outdated data makes it difficult to allocate resources effectively, anticipate surges in passenger flow, or detect anomalies in travel patterns. 
Additionally, with ongoing travel restrictions, policymakers require a data-driven approach to evaluate the impact of regulatory measures on cross-border mobility.

### Dashboard Purpose:

Our proposed dashboard will integrate and visually represent key passenger movement statistics, breaking them down by entry points, traveler categories 
(Hong Kong residents, Mainland visitors, other visitors), and trends over time. 
By offering dynamic filtering, historical comparisons, and real-time insights, our dashboard will help stakeholders optimize immigration policies, streamline transportation planning, and anticipate shifts in cross-border travel demand. 
With intuitive data visualization, decision-makers can allocate resources more effectively, ensuring a seamless and efficient movement of people through Hong Kong’s borders.
This initiative bridges the gap between raw data and strategic policymaking, fostering smarter governance and improved public services.

## Section 2
### Data Source
The [Daily Passenger Traffic](https://data.gov.hk/en-data/dataset/hk-immd-set5-statistics-daily-passenger-traffic) dataset is a public dataset provided by the Immigration Department of the Hong Kong SAR Government. It tracks the daily flow of passengers entering and exiting the city at each border control point since 2021. The dataset is updated daily and can be accessed via API requests. By Jan 2025, there are around 45,000 rows. 

#### Dataset Columns  
The dataset contains the following columns:  

- **Date**: The date of the record.  
- **Control Point**: The name of the border control point, such as the airport, ferry terminals, and railway stations.  
- **Arrival / Departure**: Indicates whether the passenger is entering or leaving Hong Kong.  
- **Hong Kong Residents**: The number of passengers who are Hong Kong residents.  
- **Mainland Visitors**: The number of passengers who are residents of Mainland China.  
- **Other Visitors**: The number of foreign passengers.  
- **Total**: The total number of passengers.

#### Cleaned & Formatted Data  
We cleaned and formatted the data into the following columns:  

- **`date`**: Extracted from the original **Date** column.  
- **`control_point`**: Extracted from the original **Control Point** column.  
- **`travel_type`**: Extracted from the original **Arrival / Departure** column.  
- **`passenger_origin`**: Categorized as `Hong Kong Residents`, `Mainland Visitors`, or `Other Visitors`.  
- **`passenger_count`**: The number of passengers in each category.  

After data wrangling, there are 136,000 rows (by Jan 2025) and 5 variables. We will utilize all the variables in our visualization.

#### New Variables
Additionally, we will engine the following variables.

- **`net_passenger_inflow`**: The number of passengers entering the city minus the number of passengers exiting the city. A positive value means more people are entering than leaving, while a negative value means the opposite. It can help track trends during holidays and major events.
- **`vistor_population_ratio`**: The number of passengers divided by the city’s population. This variable can indicate the tourism intensity and the relative impact of visitors on the city’s infrastructure. In this project, we will use 7.54 million as the population in Hong Kong [(source)](https://www.gov.hk/en/about/abouthk/facts.htm).
- **`travel_method`**: Derived from the `control_point` variable, indicating whether the passenger travels by sea, air, or land. It helps us analyze travel trends by transport mode, especially for seasonal or event-driven changes.

#### How Does the Data Solve the Problem?
The number of passengers crossing the border in both directions is a key metric for monitoring cross-border movements. Additionally, we incorporate secondary information in our dataset, including **which border passengers use**, **their mode of travel**, and **their origin**. This enables the government to allocate resources effectively, especially during major events, ensuring a smooth border-crossing experience for all travelers. For example, for land borders, if the government notices an increasing trend of passengers leaving the city through a land control point, they can extend its operating hours and notify the authorities on the other side.

Furthermore, the newly introduced variable, `visitor_population_ratio`, reflects the proportion of visitors relative to the total population. This metric helps the government assess the impact of visitors on the city’s infrastructure. For example, it can help the government make decisions on whether to increase the frequency of metro and bus services connecting downtown and the airport to accommodate higher passenger volumes.

## Section 3

### Persona

It is expected that a user from the intended target audience might not be well-versed in the
technical aspects of the data. However, these users will need to know which control points are
the most popular so that decisions regarding the budget can be made. Therefore, they will focus
on ensuring the government does not underfund key control points.

For the users who are more aware of the technical aspects, they are likely to be looking for key
metrics such as throughput through a particular control point and looking for bottlenecks in the
transportation of people. Having real-time access to this information allows them to better
coordinate key personnel to ensure smooth operations even with congestion in some control points.

### Example Scenario

Ming Choi is a public policy maker with some technical knowledge who is working in the Hong Kong
government and he wants to know which control points of Hong Kong are the most used to better
assign funds to support these high-traffic control points. Additionally, Choi might also wish to
[explore] which time of the year is the busiest historically so that there are additional funds
set aside for the future.

Choi might also want to [compare] multiple control points simultaneously for data over time to
gain better insight into optimal times to increase or decrease funds. Therefore, then Choi logs
into this Hong Kong Tracker app, he will be able to see an overview of the people traffic for the
city using the dataset that has been collected by the government already. He can filter the data
to see an overview of people traveling through certain control points and compare between each
control point. He might find that the airport is the most popular control point in the city.

Based on his findings using the app, Choi would then know that it is more prudent to allocate
more funds to the airport to ensure that there is enough staff to handle the number of people 
arriving and departing through the airport.

## Section 4