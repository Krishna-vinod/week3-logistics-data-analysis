import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("Week2_Logistics_Cleaned_Data.csv")
df["Order_Date"] = pd.to_datetime(df["Order_Date"])

# Basic EDA
print(df.shape)
print(df.info())
print(df.describe())
print(df.isna().sum())

# Central tendencies
print(df[["Distance_km", "Shipment_Weight_kg", "Shipping_Cost",
          "Actual_Delivery_Days", "Delay_Days"]].agg(
              ["mean", "median", "std", "min", "max"]
          ))

# Correlations
num_cols = ["Distance_km", "Shipment_Weight_kg", "Order_Quantity",
            "Scheduled_Days", "Actual_Delivery_Days", "Shipping_Cost",
            "Sales_Value", "Delay_Days", "On_Time", "Cost_per_Unit"]
print(df[num_cols].corr())

# Grouped performance
print(df.groupby("Shipping_Mode").agg(
    shipments=("Shipment_ID", "count"),
    on_time_rate=("On_Time", "mean"),
    avg_delay=("Delay_Days", "mean"),
    avg_cost=("Shipping_Cost", "mean")
))

# Visualization 1: delivery distribution
plt.hist(df["Actual_Delivery_Days"], bins=np.arange(0.5, 9.5, 1), edgecolor="black")
plt.xlabel("Actual Delivery Days")
plt.ylabel("Shipments")
plt.title("Distribution of Actual Delivery Time")
plt.show()

# Visualization 2: shipping mode performance
mode = df.groupby("Shipping_Mode")["On_Time"].mean().sort_values(ascending=False)
plt.bar(mode.index, mode.values * 100)
plt.ylabel("On-Time Rate (%)")
plt.title("On-Time Delivery by Shipping Mode")
plt.xticks(rotation=20)
plt.show()

# Visualization 3: distance vs cost
plt.scatter(df["Distance_km"], df["Shipping_Cost"], alpha=0.35)
plt.xlabel("Distance (km)")
plt.ylabel("Shipping Cost")
plt.title("Distance vs Shipping Cost")
plt.show()

# Visualization 4: regional performance
region = df.groupby("Region")["On_Time"].mean().sort_values()
plt.bar(region.index, region.values * 100)
plt.ylabel("On-Time Rate (%)")
plt.title("On-Time Delivery Rate by Region")
plt.xticks(rotation=25)
plt.show()

# Visualization 5: monthly trend
df["Month"] = df["Order_Date"].dt.to_period("M").astype(str)
monthly = df[df["Order_Date"].dt.year == 2017].groupby("Month")["On_Time"].mean()
plt.plot(monthly.index, monthly.values * 100, marker="o")
plt.ylabel("On-Time Rate (%)")
plt.title("2017 Monthly On-Time Delivery Trend")
plt.xticks(rotation=45)
plt.show()

# Visualization 6: product category
cat = df.groupby("Product_Category").agg(
    on_time_rate=("On_Time", "mean"),
    avg_cost=("Shipping_Cost", "mean")
)
cat["on_time_rate"].mul(100).plot(kind="bar")
plt.ylabel("On-Time Rate (%)")
plt.title("On-Time Rate by Product Category")
plt.show()

# Visualization 7: correlation matrix
corr = df[num_cols].corr()
plt.figure(figsize=(9, 7))
plt.imshow(corr, aspect="auto")
plt.colorbar()
plt.xticks(range(len(corr.columns)), corr.columns, rotation=70)
plt.yticks(range(len(corr.index)), corr.index)
plt.title("Correlation Matrix")
plt.tight_layout()
plt.show()
