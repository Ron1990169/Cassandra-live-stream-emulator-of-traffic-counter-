This document is an academic report submitted by Rohin Mehra for Assignment 3 at Griffith College Dublin, as part of the Big Data Analysis and Management department. The assignment focuses on analyzing a traffic counter dataset for the M50 motorway and storing the results in Cassandra, a distributed NoSQL database. Below is an overview of the tasks and solutions implemented in the assignment:

Q1: Emulating a Live-Stream of Traffic Data
The first task involved writing a Python script to simulate a live stream by reading 10 records at a time from a traffic counter dataset. 
This stream of data was then used for real-time analysis, which is crucial for tasks such as traffic monitoring and management.

Q2: Traffic Data Analysis
In this task, various analyses were performed on the streamed traffic data:

Total Counts by Vehicle Class: The total number of vehicle counts on each side of the M50 was computed, grouped by vehicle class.
Average Speed by Vehicle Class: The average speed of vehicles on each side of the M50 was calculated, again categorized by vehicle class.
Top 3 Busiest Counter Sites: The three busiest traffic counter sites on the M50 were identified based on vehicle counts.
Total HGV Counts: The total number of Heavy Goods Vehicles (HGVs) on the M50 was calculated.
Q3: Storing Results in Cassandra
The third task involved preparing Cassandra data structures and writing the results of the analysis into the database:

Cassandra Data Structures: Four tables were created to store the results of the analysis:

vehicle_group_M50: Stores vehicle counts by class and site.
Average_velocity_M50: Stores average speed by site.
Bussiest_Nodes_m50: Stores the counts for the top 3 busiest sites.
HGV_traffic_M50: Stores the total counts for HGVs.
These tables were designed with appropriate primary keys to efficiently manage and query the data.

Inserting Data into Cassandra: Python functions were written to insert the analysis results into the Cassandra tables:

insert_Q1: Inserts data into the vehicle_group_M50 table.
insert_Q2: Inserts average speed data into the Average_velocity_M50 table.
insert_Q3: Inserts the count data of the busiest sites into the Bussiest_Nodes_m50 table.
insert_Q4: Inserts HGV count data into the HGV_traffic_M50 table.
Each function prepares a Cassandra statement and executes it to store the corresponding analysis result in the appropriate table.

Key Features and Insights
Data Streaming: The assignment successfully emulates real-time data streaming, which is essential for dynamic traffic analysis.
Comprehensive Traffic Analysis: The analysis covered various aspects of traffic on the M50, providing insights into vehicle distribution, speed patterns, and congestion hotspots.
Efficient Data Storage: By storing the results in Cassandra, the assignment demonstrates the ability to manage large-scale traffic data in a scalable and efficient manner, 
ensuring that the system can handle high volumes of real-time data.
