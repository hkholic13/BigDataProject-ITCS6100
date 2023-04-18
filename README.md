# BigDataProject-ITCS6100

# Team

## Members:
- Ramya Jampani
- Chetan Subhash Chunduru
- Himanshi Khatri
- Revanth Kumar Galla
- Satya Sai Rajesh Parvatareddy

## Communication plan to include project artifact repository:
Methods of communication :- e-mail, in-person(once a week)

Communication response times:- Same day

Meeting attendance:- After looking into everyone’s schedule we had decided to meet every Wednesday either virtual or in-person to discuss the progress of the project and attendance to this is mandatory.

Running meetings:- Virtual

Meeting preparation: We decided to come prepared to the meetings so that we can use the time in the most efficient way.

Version control: By creating pull requests, team members can push all of their modifications to the artifact, which are then assessed by their peers and merged. 
Git link(https://github.com/hkholic13/BigDataProject-ITCS6100)

Git link: [https://github.com/hkholic13/BigDataProject-ITCS6100](https://github.com/hkholic13/BigDataProject-ITCS6100)

## First Choice : 

# Selection of data to analyze

We will carefully select the domain and data for our project, which in this case, will be the "Porter Delivery Time Estimation" dataset provided by the competition organizers. We will analyze the dataset and understand its structure, features, and potential use cases for Delivery Time Prediction, Order Volume Analysis, Customer Satisfaction Analysis, Delivery Performance Analysis, Vendor Performance Analysis, Geographic Analysis, Seasonal Analysis.

Kaggle Link: [https://www.kaggle.com/datasets/ranitsarkar01/porter-delivery-time-estimation](https://www.kaggle.com/datasets/ranitsarkar01/porter-delivery-time-estimation)

## Files:
Each row in this file corresponds to one unique delivery. Each column corresponds to a feature as explained below

- market id: integer id for the market where the restaurant lies
- created at: the timestamp at which the order was placed
- actual delivery time: the timestamp when the order was delivered
- store_primary_category: category for the restaurant
- order protocol: integer code value for order protocol(how the order was placed le: through porter, call to   restaurant, pre booked, third part etc)
- total items subtotal: final price of the order
- num_distinct items: the number of distinct items in the order
- actual delivery time: the timestamp when the order was delivered
- store_primary_category: category for the restaurant
- order protocol: integer code value for order protocol(how the order was placed le: through porter, call to restaurant, pre booked, third part etc)
- total items subtotal: final price of the order
- num_distinct items: the number of distinct items in the order
- min_item_price: price of the cheapest item in the order
- max_item_price: price of the costliest item in order
- total_onshift_partners: number of delivery partners on duty at the time order was placed
- total_busy_partners: number of delivery partners attending to other tasks
- total outstanding_orders: total number of orders to be fulfilled at the moment

# Business Problem or Opportunity, Domain Knowledge

The dataset titled "Porter Delivery Time Estimation" available on Kaggle provides a prospect for data-driven analysis in the realm of food delivery by presenting a business problem. Food delivery enterprises, including restaurants, cafes, and food delivery platforms, encounter the difficulty of accurately predicting and controlling delivery durations to ensure a gratifying encounter for their clientele. Precise estimation of delivery time is critical for fulfilling customer demands, guaranteeing punctual deliveries, and upholding customer contentment.

The "Porter Delivery Time Estimation" dataset presents a valuable opportunity for businesses to utilize existing data in order to extract insights and arrive at well-informed decisions. The dataset can be analyzed and valuable insights can be derived by utilizing domain knowledge related to the food delivery industry, logistics, and customer preferences. Through an analysis of the variables that impact delivery time, discernment of patterns and trends in order volume, customer satisfaction, delivery performance, and vendor performance, enterprises can optimize their operational processes, enhance their customer service, and augment their competitive edge.

The interpretation of data and discovery of significant insights can be facilitated through the utilization of domain knowledge in fields such as transportation and logistics, customer behavior, and market trends. An instance of optimization for delivery routes and schedules in businesses can be achieved by comprehending the influence of weather conditions, traffic patterns, and distance on delivery time. Acquiring an understanding of customer preferences, including peak hours and days, can aid businesses in effectively strategizing their resource allocation and operational procedures. Familiarity with market trends and seasonal patterns can assist enterprises in adapting their tactics and advertising campaigns to accommodate evolving consumer preferences.

In general, the utilization of domain expertise and examination of the "Porter Delivery Time Estimation" dataset offers a prospect for enhancing delivery time estimation, streamlining operations, augmenting customer contentment, and attaining a competitive edge in the food delivery sector.

Link to domain data: [https://porter.in/about-us?landing_page=nw&utm_content=nw](https://porter.in/about-us?landing_page=nw&utm_content=nw)

## Business Problem/Opportunity: Improving Delivery time

### Domain Knowledge:
- Domain knowledge in market trends:

    The comprehension of market trends and seasonality is crucial for businesses to adapt their strategies and promotional activities to cater to the evolving demands of their customers. The identification of seasonal variations in demand for specific types of cuisine or food products can aid enterprises in devising appropriate strategies for inventory management, staffing, and promotional activities.

    Conducting competition analysis by monitoring market trends and scrutinizing the products, pricing, and promotional strategies of rivals can enable enterprises to maintain their competitiveness. The process may encompass the surveillance of the market for novel participants, the discernment of customer inclinations, and the comparison with rivals to pinpoint opportunities for enhancement and distinction.

    Market segmentation is a crucial strategy for businesses to comprehend the distinct customer segments and their preferences. This understanding enables businesses to customize their offerings and promotions to cater to the unique requirements of each segment. The process may entail scrutinizing data pertaining to customer demographics, preferences, and behaviors to discern prospects for targeting particular market segments through tailored strategies.

- Domain knowledge in Transportation and logistics

    Real-time traffic and weather data may be used to determine the shortest and most direct routes for vehicles. This involves evaluating information such as traffic patterns, road conditions, and weather forecasts to decide the most effective route for delivery to take. By optimizing delivery routes, businesses may reduce delays, save money on transportation costs, and ensure that items reach on time.

    By allocating delivery trucks to the appropriate jobs, planning routine maintenance, controlling fuel consumption, and utilizing tracking and monitoring systems, fleet management ensures that they are utilized effectively. This entails determining the efficiency of each vehicle, the amount of gasoline it consumes, and when maintenance is due. Businesses can ensure their drivers are secure and their cars aren't being misused by deploying tracking and monitoring technologies.

    Businesses must select the appropriate mode of transportation for their delivery since different modes of transportation have varied prices, benefits, and restrictions. For instance, when moving products over short distances, employing trucks is typically the most flexible and economical alternative, whereas air transportation is quicker but more expensive and less versatile.

- Domain knowledge in Customer Conduct:

    Businesses may better manage their resources and schedule deliveries to make sure they arrive on time during peak times by being aware of when consumers are most likely to place purchases. To find trends in consumer behavior, this entails analyzing data such as order history, transaction volume, and delivery timings. Businesses may prepare ahead of time and make sure they have adequate employees and inventory to satisfy demand by knowing when consumers are most likely to place orders.


    Businesses can learn how to better serve their customers and grow by looking at consumer purchase trends, such as the most popular days of the week or the most frequently requested items. This entails gathering and researching information such as order histories, menu choices, and client testimonials. Businesses may better meet consumer demands and enhance the overall experience by learning what customers love and dislike about their goods and services.

    Customer feedback and reviews: Analyzing customer feedback and reviews can provide valuable insights into customer behavior and preferences. This can involve identifying common complaints, feedback on delivery time, and overall satisfaction levels to pinpoint areas for improvement and make data-driven decisions.


##  Research Objectives and Question(s) (what you are trying to describe or predict with the data)

The team formulated research questions that guide the analysis and investigation. These questions align with their research objectives and are intended to address the identified business challenge or opportunity.
For example, 
- What are the key factors that influence the delivery time of orders placed through the Porter platform? Can we identify any patterns or trends in the data that can help optimize delivery operations and reduce delivery time?

- How does the order protocol (i.e., how the order was placed) affect the delivery time? Are there any significant differences in delivery time based on different order protocols, such as orders placed through Porter, call to restaurant, pre-booked, or third-party platforms?

- How do the restaurant's primary category and the total number of distinct items in an order impact the delivery time? Are certain restaurant categories or order sizes associated with longer or shorter delivery times?

- Can we develop a predictive model that accurately estimates the delivery time for orders based on features such as distance, weather conditions, order characteristics, and partner availability? How well can the model predict the actual delivery time?

- What is the relationship between the prices of items in an order (i.e., min_item_price, max_item_price) and the delivery time? Do higher or lower prices of items in an order have an impact on the delivery time?

- How do the number of on-shift and busy delivery partners at the time of order placement affect the delivery time? Can we identify any patterns or trends that can help optimize partner allocation and reduce delivery time?

- What is the impact of the total number of outstanding orders at the moment on the delivery time? Does a higher number of outstanding orders result in longer delivery times?

- Are there any seasonal or time-based trends in the data that affect the delivery time? How does the delivery time vary based on different days of the week, time of day, or month of the year?

- Can we identify any customer behavior patterns related to delivery time, such as peak hours or days for ordering, preferences for certain order protocols or restaurant categories, or preferences for higher or lower-priced items?

- How does the delivery time impact customer satisfaction? Can we quantify the relationship between delivery time and customer satisfaction scores, and identify any opportunities for improving customer satisfaction through optimizing delivery time?

- Comparison with other delivery systems available in the market to show the trends and to compare the differences.
