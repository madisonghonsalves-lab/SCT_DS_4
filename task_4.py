# Import libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Load Dataset
df = pd.read_csv("accident_sample.csv")
print("Dataset Shape:")
print(df.shape)
print("\nFirst 5 Rows:")
print(df.head())

# 2. Data Cleaning
print("\nMissing Values:")
print(df.isnull().sum().head())
# Remove rows with missing important values
df.dropna(
    subset=[
        "Start_Time",
        "Weather_Condition",
        "Start_Lat",
        "Start_Lng"
    ],
    inplace=True
)

# 3. Accident Trend by Time of Day
df["Start_Time"] = pd.to_datetime(df["Start_Time"])
df["Hour"] = df["Start_Time"].dt.hour
plt.figure(figsize=(10,5))
sns.histplot(
    df["Hour"],
    bins=24
)
plt.title("Accidents According to Time of Day")
plt.xlabel("Hour")
plt.ylabel("Number of Accidents")
plt.savefig("time_of_day.png")
plt.show()

# 4. Weather Condition Analysis
weather = (
    df["Weather_Condition"]
    .value_counts()
    .head(10)
)
plt.figure(figsize=(10,5))
weather.plot(kind="bar")
plt.title("Top Weather Conditions During Accidents")
plt.xlabel("Weather Condition")
plt.ylabel("Number of Accidents")
plt.xticks(rotation=45)
plt.savefig("weather_analysis.png")
plt.show()

# 5. Accident Severity Analysis
plt.figure(figsize=(7,5))
sns.countplot(
    data=df,
    x="Severity"
)
plt.title("Accident Severity Distribution")
plt.savefig("severity_analysis.png")
plt.show()

# 6. Road Related Factors
road_features = [
    "Junction",
    "Traffic_Signal",
    "Crossing",
    "Stop"
]
road_values=[]
for feature in road_features:

    road_values.append(
        df[feature].sum()
    )
plt.figure(figsize=(8,5))
sns.barplot(
    x=road_features,
    y=road_values
)
plt.title(
    "Road Features Contributing to Accidents"
)
plt.xlabel("Road Feature")
plt.ylabel("Accident Count")
plt.savefig("road_factors.png")
plt.show()

# 7. Accident Hotspot Visualization
# Use sample because dataset is huge
sample = df.sample(min(5000, len(df)))
plt.figure(figsize=(8,6))
sns.scatterplot(
    data=sample,
    x="Start_Lng",
    y="Start_Lat",
    hue="Severity",
    alpha=0.5
)
plt.title("Accident Hotspots Based on Location")
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.savefig("accident_hotspots.png")
plt.show()

# 8. Top Accident Cities
cities = (
    df["City"]
    .value_counts()
    .head(10)
)
plt.figure(figsize=(10,5))
cities.plot(kind="bar")
plt.title(
    "Cities With Highest Accident Count"
)
plt.xlabel("City")
plt.ylabel("Accidents")
plt.xticks(rotation=45)
plt.savefig("top_cities.png")
plt.show()

print("Analysis Completed Successfully!")
