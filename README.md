UCC Hostel Analysis & Decision Support

Project Overview
Finding suitable accommodation can be challenging for students searching for hostels around the University of Cape Coast (UCC). Students often have to consider several factors at the same time, including rent, distance from campus, room type, student ratings, availability, complaints, and hostel verification status.

This project analyzes hostel data around UCC to provide data-driven insights that can help students make more informed accommodation decisions.

The project combines Excel, SQL, Python, and Power BI to clean, analyze, visualize, and explore hostel information.


Project Objective

The main objective of this project is to analyze hostel data around UCC and identify useful patterns that can help students compare accommodation options based on their individual preferences.

The analysis focuses on questions such as:

* Which locations have the highest number of hostels?
* Which locations have the highest average rent?
* What are the cheapest hostels?
* Which hostels are closest to campus?
* Which hostels have the highest student ratings?
* Which hostels have the most reported complaints?
* Which hostels have the highest occupancy rates?
* What is the verification status of the hostels?
* How does rent vary across locations and room types?
* Is there a relationship between hostel rent and student ratings?
* Which hostels meet selected affordability, distance, rating, and verification criteria?

Dataset
The dataset contains 500 hostel records and includes information about hostel characteristics, accommodation, safety, verification, and student feedback.

Key Variables

Category	Variables
Hostel Information	Hostel ID, Hostel Name, Location
Accommodation	Room Type, Gender, Number of Rooms, Total Beds
Cost	Annual Rent (GHS)
Location	Distance from Campus (km)
Occupancy	Occupied Beds, Occupancy Rate
Facilities	Water, Electricity
Safety	Fire Safety Equipment
Verification	Documents Verified, Physical Inspection, Verification Status
Student Feedback	Student Rating, Reported Complaints
Inspection	Inspection Date, Last Verified By

Tools & Technologies
Microsoft Excel

Used for:
* Data preparation
* Initial data exploration
* KPI analysis
* Pivot-table analysis
* Summary tables
* Initial visualization

SQL

Used for:
* Data exploration
* Duplicate checking
* Aggregation
* Filtering
* Sorting
* Location analysis
* Rent analysis
* Rating analysis
* Hostel verification analysis
* Identifying hostels meeting selected criteria

Python

Used for:
* Exploratory Data Analysis (EDA)
* Data inspection
* Missing-value checks
* Duplicate checks
* Statistical analysis
* Correlation analysis
* Data filtering
* Data visualization
* Generating analytical output files

Libraries used:
* Pandas
* Matplotlib
* Seaborn

Power BI

Used to create an interactive dashboard for exploring hostel characteristics and key performance indicators.

GitHub

Used for:
* Version control
* Project documentation
* Portfolio presentation
* Sharing project files and analysis

Analysis Performed

1. Hostel Distribution
The project examines the number of hostels available across different locations around UCC.

2. Rent Analysis
The analysis compares:

* Average annual rent by location
* Rent by room type
* Cheapest hostels
* Most expensive hostels
* Overall rent distribution

3. Student Ratings
Hostels are analyzed based on student ratings to understand differences in perceived accommodation experience.

4. Occupancy Analysis
The project examines:

* Occupancy rates
* Total beds
* Occupied beds
* Available beds
* Hostels with high occupancy

5. Hostel Verification
The analysis considers hostel verification indicators including:

* Document verification
* Physical inspection
* Verification status
* Fire safety equipment

6. Complaints Analysis
Reported complaints are analyzed to identify hostels with relatively high numbers of complaints.

7. Location & Cost Analysis
The relationship between distance from campus and annual rent is explored to understand how accommodation cost varies with location.

8. Correlation Analysis
Python is used to examine relationships between numerical variables including:

* Distance from campus
* Annual rent
* Number of rooms
* Total beds
* Occupied beds
* Occupancy rate
* Student rating
* Reported complaints

Hostel Selection Criteria
The project also demonstrates how data can be used to filter hostels according to specific student requirements.

One example selection uses:
* Distance from campus ≤ 3 km
* Annual rent ≤ GHS 5,500
* Student rating ≥ 4.0
* Verification status = Verified

This is not intended to declare a single “best” hostel. Instead, it demonstrates how students could use different criteria to narrow down their accommodation options.

Power BI Dashboard
The Power BI dashboard provides an interactive way to explore the hostel dataset.

Users can investigate information such as:

* Hostel locations
* Average rent
* Student ratings
* Verification status
* Occupancy
* Complaints
* Accommodation characteristics

The dashboard is designed to support comparison and exploration rather than simply present static results.


Key Project Value
This project demonstrates how raw accommodation data can be transformed into useful information for decision-making.
Instead of relying on a single factor such as price, students can consider multiple dimensions including:

Cost + Distance + Rating + Verification + Availability + Complaints

This approach can help students compare accommodation options according to their own priorities.


Future Improvements
Future versions of the project could include:

* An interactive hostel-search website
* A recommendation system based on student preferences
* Map-based hostel visualization
* Real-time hostel availability
* Student reviews and sentiment analysis
* Price comparison tools
* Hostel contact information
* Advanced machine-learning recommendations
* Automated data collection and updating

⚠️ Disclaimer

This project is intended for educational and portfolio purposes.

The dataset is used for analytical demonstration and should not be treated as a real-time or authoritative directory of UCC hostels.

Students should independently verify hostel availability, prices, facilities, safety information, and other details before making accommodation decisions.

Author
Elliot Teye
IT Student | Aspiring Data Analyst & Data Scientist

Skills Demonstrated

Excel • SQL • Python • Pandas • Matplotlib • Seaborn • Power BI • Data Analysis • Data Visualization • Exploratory Data Analysis

⭐ If you find this project useful

Feel free to explore the analysis, review the SQL queries, run the Python code, and examine the Power BI dashboa
