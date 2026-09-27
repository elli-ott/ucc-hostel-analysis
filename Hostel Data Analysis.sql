-- Checking for duplicates
 Select 
	Hostel_ID, 
    count(*) As count
 From `hostel dataset r`
 Group By Hostel_ID
 Having count(*) > 1;
 
-- Count Of Hostels By Location
 Select 
	Location, 
    count(Hostel_ID) As Number_of_hostels
 From `hostel dataset r`
 Group By Location
 Order By Number_of_Hostels DESC;

-- Average Rent by Location
 Select 
	Location, 
    round(avg(Annual_Rent_GHS),2) As Average_rent
 From `hostel dataset r`
 Group By Location
 Order By average_rent DESC

-- Cheapest Hostels
Select 
	Hostel_Name,
	Location,Annual_Rent_GHS
From `hostel dataset r`
Order By Annual_Rent_GHS ASc
Limit 10

-- Most Expensive Hostels
Select 
	Hostel_Name,
    Location,
    Annual_Rent_GHS
From `hostel dataset r`
Order By Annual_Rent_GHS DESC
Limit 10

-- Average Rent by room type
Select 
	Room_Type,
	round(avg(Annual_Rent_GHS),2) As Average_Rent
From `hostel dataset r`
Group By Room_Type
Order By Average_Rent DESC

-- Average Student Rating
Select 
	Location,
    round(avg(Student_Rating),2) As Average_rating
From `hostel dataset r`
Group By Location
Order By Average_rating DESC

-- Hostels With Most Complaints
Select 
	Hostel_Name,
	Location,
	Reported_Complaints
From `hostel dataset r`
Order By Reported_Complaints DESC
Limit 10

-- Hostels With Hoghest Occupancy
Select 
	Hostel_Name,
    Location,
    `Occupancy_Rate_%`
From `hostel dataset r`
Order By `Occupancy_Rate_%` DESC
Limit 10

-- Verification Analysis
Select 
	Verification_Status,
    count(Hostel_ID) As Number_of_hostels
From `hostel dataset r`
Group By Verification_Status
Order By Number_of_hostels DESC

-- Unverified Hostels/Hostels That Failed Inspection
Select 
	Hostel_Name,
    Location,
    Annual_Rent_GHS,
    Student_Rating,
    Reported_Complaints,
    Verification_Status,
    Physical_Inspection_Passed
From `hostel dataset r`
Where Verification_Status<> 'Verified'
Or Physical_Inspection_Passed= 'No'
Order By Reported_Complaints DESC

-- Hostels Within 3km of Campus/Rent <= GHS 5,500/Rating >=4.0/Verified
Select
	Hostel_Name,
    Location,
    Distance_from_Campus_km,
    Annual_Rent_GHS,
    Student_Rating,
    Verification_Status
From `hostel dataset r`
Where Distance_from_Campus_km <= 3
And Annual_Rent_GHS<= 5500
And Student_Rating >= 4.0
And Verification_Status ='verified'
Order By Student_Rating DESC    