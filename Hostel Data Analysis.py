# STUDENT HOSTEL VERIFICATION ANALYSIS
# Python Exploratory Data Analysis (EDA)

# 1. IMPORT LIBRARIES
import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# 2. CREATE OUTPUT FOLDER
os.makedirs("outputs", exist_ok=True)


# 3. LOAD DATASET
file_name = "Hostel Dataset R.csv"

df = pd.read_csv(file_name)

print("=" * 60)
print("STUDENT HOSTEL VERIFICATION ANALYSIS")
print("=" * 60)


# 4. BASIC DATA INSPECTION


print("\n1. FIRST 5 ROWS")
print(df.head())

print("\n2. DATASET SHAPE")
print(df.shape)

print("\n3. COLUMN NAMES")
print(df.columns.tolist())

print("\n4. DATA TYPES")
print(df.dtypes)

print("\n5. DATASET INFORMATION")
print(df.info())


# 5. CHECK MISSING VALUES
print("\n6. MISSING VALUES")
print(df.isnull().sum())


# 6. CHECK DUPLICATES
print("\n7. DUPLICATE ROWS")
print(df.duplicated().sum())

print("\n8. DUPLICATE HOSTEL IDs")
print(df["Hostel_ID"].duplicated().sum())


# 7. STATISTICAL SUMMARY
print("\n9. STATISTICAL SUMMARY")
print(df.describe())


# 8. CREATE AVAILABLE BEDS
df["Available_Beds"] = (
    df["Total_Beds"] - df["Occupied_Beds"]
)

print("\n10. AVAILABLE BEDS")
print(
    df[
        [
            "Hostel_Name",
            "Total_Beds",
            "Occupied_Beds",
            "Available_Beds"
        ]
    ].head(10)
)


# ANALYSIS

# 9. HOSTELS BY LOCATION
print("\n11. NUMBER OF HOSTELS BY LOCATION")

location_counts = df["Location"].value_counts()

print(location_counts)


# 10. AVERAGE RENT BY LOCATION
print("\n12. AVERAGE RENT BY LOCATION")

average_rent_location = (
    df.groupby("Location")["Annual_Rent_GHS"]
    .mean()
    .sort_values(ascending=False)
)

print(average_rent_location)


# 11. AVERAGE RATING BY LOCATION
print("\n13. AVERAGE STUDENT RATING BY LOCATION")

average_rating_location = (
    df.groupby("Location")["Student_Rating"]
    .mean()
    .sort_values(ascending=False)
)

print(average_rating_location)


# 12. AVERAGE OCCUPANCY BY LOCATION
print("\n14. AVERAGE OCCUPANCY RATE BY LOCATION")

average_occupancy_location = (
    df.groupby("Location")["Occupancy_Rate_%"]
    .mean()
    .sort_values(ascending=False)
)

print(average_occupancy_location)



# 13. VERIFICATION STATUS
print("\n15. VERIFICATION STATUS")

verification_counts = (
    df["Verification_Status"]
    .value_counts()
)

print(verification_counts)


# 14. ROOM TYPE ANALYSIS
print("\n16. HOSTELS BY ROOM TYPE")

room_type_counts = df["Room_Type"].value_counts()

print(room_type_counts)


# 15. GENDER ANALYSIS
print("\n17. HOSTELS BY GENDER")

gender_counts = df["Gender"].value_counts()

print(gender_counts)


# 16. WATER AVAILABILITY
print("\n18. WATER AVAILABILITY")

print(df["Water_Available"].value_counts())


# 17. ELECTRICITY AVAILABILITY
print("\n19. ELECTRICITY AVAILABILITY")

print(df["Electricity_Available"].value_counts())


# 18. FIRE SAFETY EQUIPMENT
print("\n20. FIRE SAFETY EQUIPMENT")

print(df["Fire_Safety_Equipment"].value_counts())


# 19. PHYSICAL INSPECTION
print("\n21. PHYSICAL INSPECTION RESULTS")

print(df["Physical_Inspection_Passed"].value_counts())


# 20. DOCUMENT VERIFICATION
print("\n22. DOCUMENT VERIFICATION")

print(df["Documents_Verified"].value_counts())

#-------------------------
# HOSTEL RANKINGS / FILTERING
#-------------------------
# 21. CHEAPEST HOSTELS
print("\n23. 10 CHEAPEST HOSTELS")

cheapest_hostels = (
    df[
        [
            "Hostel_Name",
            "Location",
            "Annual_Rent_GHS",
            "Student_Rating"
        ]
    ]
    .sort_values("Annual_Rent_GHS")
    .head(10)
)

print(cheapest_hostels)


# 22. CLOSEST HOSTELS
print("\n24. 10 CLOSEST HOSTELS")

closest_hostels = (
    df[
        [
            "Hostel_Name",
            "Location",
            "Distance_from_Campus_km",
            "Annual_Rent_GHS"
        ]
    ]
    .sort_values("Distance_from_Campus_km")
    .head(10)
)

print(closest_hostels)


# 23. HOSTELS WITH MOST COMPLAINTS
print("\n25. HOSTELS WITH MOST COMPLAINTS")

most_complaints = (
    df[
        [
            "Hostel_Name",
            "Location",
            "Reported_Complaints",
            "Student_Rating"
        ]
    ]
    .sort_values(
        "Reported_Complaints",
        ascending=False
    )
    .head(10)
)

print(most_complaints)


# 24. HIGHEST RATED HOSTELS
print("\n26. HIGHEST RATED HOSTELS")

highest_rated = (
    df[
        [
            "Hostel_Name",
            "Location",
            "Student_Rating",
            "Annual_Rent_GHS"
        ]
    ]
    .sort_values(
        "Student_Rating",
        ascending=False
    )
    .head(10)
)

print(highest_rated)


# 25. MOST OCCUPIED HOSTELS

print("\n27. MOST OCCUPIED HOSTELS")

most_occupied = (
    df[
        [
            "Hostel_Name",
            "Location",
            "Occupancy_Rate_%",
            "Total_Beds",
            "Occupied_Beds"
        ]
    ]
    .sort_values(
        "Occupancy_Rate_%",
        ascending=False
    )
    .head(10)
)

print(most_occupied)


# SELECTED HOSTEL CRITERIA


# 26. AFFORDABLE + CLOSE + RATED + VERIFIED
print("\n28. HOSTELS MEETING SELECTED CRITERIA")

recommended_hostels = df[
    (df["Distance_from_Campus_km"] <= 3) &
    (df["Annual_Rent_GHS"] <= 5500) &
    (df["Student_Rating"] >= 4.0) &
    (
        df["Verification_Status"]
        .astype(str)
        .str.lower() == "verified"
    )
]

recommended_hostels = recommended_hostels[
    [
        "Hostel_Name",
        "Location",
        "Distance_from_Campus_km",
        "Annual_Rent_GHS",
        "Student_Rating",
        "Verification_Status"
    ]
].sort_values(
    "Student_Rating",
    ascending=False
)

print(recommended_hostels)

#--------------------------
#CORRELATION ANALYSIS
#--------------------------

# 27. CORRELATION MATRIX

numeric_columns = [
    "Distance_from_Campus_km",
    "Annual_Rent_GHS",
    "Number_of_Rooms",
    "Total_Beds",
    "Occupied_Beds",
    "Occupancy_Rate_%",
    "Student_Rating",
    "Reported_Complaints"
]

correlation = df[numeric_columns].corr()

print("\n29. CORRELATION MATRIX")

print(correlation)

#------------------------
# VISUALIZATIONS
#------------------------

# 28. HOSTELS BY LOCATION

plt.figure(figsize=(10, 6))

location_counts.plot(kind="bar")

plt.title("Number of Hostels by Location")
plt.xlabel("Location")
plt.ylabel("Number of Hostels")
plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig(
    "outputs/location_distribution.png",
    dpi=300
)

plt.show()


# 29. AVERAGE RENT BY LOCATION
plt.figure(figsize=(10, 6))

average_rent_location.sort_values().plot(
    kind="barh"
)

plt.title("Average Annual Rent by Location")
plt.xlabel("Average Annual Rent (GHS)")
plt.ylabel("Location")

plt.tight_layout()

plt.savefig(
    "outputs/average_rent_by_location.png",
    dpi=300
)

plt.show()


# 30. VERIFICATION STATUS

plt.figure(figsize=(8, 6))

verification_counts.plot(
    kind="bar"
)

plt.title("Hostel Verification Status")
plt.xlabel("Verification Status")
plt.ylabel("Number of Hostels")

plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig(
    "outputs/verification_status.png",
    dpi=300
)

plt.show()


# 31. RENT DISTRIBUTION

plt.figure(figsize=(10, 6))

sns.histplot(
    df["Annual_Rent_GHS"],
    kde=True
)

plt.title("Distribution of Annual Hostel Rent")
plt.xlabel("Annual Rent (GHS)")
plt.ylabel("Number of Hostels")

plt.tight_layout()

plt.savefig(
    "outputs/rent_distribution.png",
    dpi=300
)

plt.show()


# 32. STUDENT RATING DISTRIBUTION

plt.figure(figsize=(10, 6))

sns.histplot(
    df["Student_Rating"],
    kde=True
)

plt.title("Distribution of Student Ratings")
plt.xlabel("Student Rating")
plt.ylabel("Number of Hostels")

plt.tight_layout()

plt.savefig(
    "outputs/rating_distribution.png",
    dpi=300
)

plt.show()


# 33. OCCUPANCY DISTRIBUTION

plt.figure(figsize=(10, 6))

sns.histplot(
    df["Occupancy_Rate_%"],
    kde=True
)

plt.title("Distribution of Hostel Occupancy Rate")
plt.xlabel("Occupancy Rate (%)")
plt.ylabel("Number of Hostels")

plt.tight_layout()

plt.savefig(
    "outputs/occupancy_distribution.png",
    dpi=300
)

plt.show()


# 34. RENT VS STUDENT RATING

plt.figure(figsize=(10, 6))

sns.scatterplot(
    data=df,
    x="Annual_Rent_GHS",
    y="Student_Rating"
)

plt.title("Annual Rent vs Student Rating")
plt.xlabel("Annual Rent (GHS)")
plt.ylabel("Student Rating")

plt.tight_layout()

plt.savefig(
    "outputs/rent_vs_rating.png",
    dpi=300
)

plt.show()


# 35. DISTANCE VS RENT

plt.figure(figsize=(10, 6))

sns.scatterplot(
    data=df,
    x="Distance_from_Campus_km",
    y="Annual_Rent_GHS"
)

plt.title("Distance from Campus vs Annual Rent")
plt.xlabel("Distance from Campus (km)")
plt.ylabel("Annual Rent (GHS)")

plt.tight_layout()

plt.savefig(
    "outputs/distance_vs_rent.png",
    dpi=300
)

plt.show()


# 36. COMPLAINTS VS RATING

plt.figure(figsize=(10, 6))

sns.scatterplot(
    data=df,
    x="Reported_Complaints",
    y="Student_Rating"
)

plt.title("Reported Complaints vs Student Rating")
plt.xlabel("Reported Complaints")
plt.ylabel("Student Rating")

plt.tight_layout()

plt.savefig(
    "outputs/complaints_vs_rating.png",
    dpi=300
)

plt.show()


# 37. CORRELATION HEATMAP

plt.figure(figsize=(10, 8))

sns.heatmap(
    correlation,
    annot=True,
    cmap="coolwarm",
    fmt=".2f"
)

plt.title("Correlation Matrix")

plt.tight_layout()

plt.savefig(
    "outputs/correlation_matrix.png",
    dpi=300
)

plt.show()


# 38. SAVE SELECTED RESULTS

recommended_hostels.to_csv(
    "outputs/recommended_hostels.csv",
    index=False
)

cheapest_hostels.to_csv(
    "outputs/cheapest_hostels.csv",
    index=False
)

highest_rated.to_csv(
    "outputs/highest_rated_hostels.csv",
    index=False
)

most_complaints.to_csv(
    "outputs/most_complaints_hostels.csv",
    index=False
)


# END OF PROJECT

print("\n" + "=" * 60)
print("PYTHON ANALYSIS COMPLETED SUCCESSFULLY")
print("=" * 60)

print("\nYour charts and analysis files have been saved")
print("inside the 'outputs' folder.")