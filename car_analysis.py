import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


#------1.Load dataset------
df = pd.read_csv("car_sales_data.csv")

print(df.head()) #first 5 rows
print(df.info()) #data types
print(df.describe()) #summary for numbers

#------2.Key Statistics------


# Count total numbers per manufacture
print(df['Manufacturer'].value_counts())

#Calculate average price by fuel type
print(df.groupby("Fuel type")['Price'].mean())

# Find oldest and newst car year
print("Oldest year : ", df['Year of manufacture'].min())
print("Newest year : ", df['Year of manufacture'].max())

#Top 5 most common models
print(df['Model'].value_counts().head(5))

with open("statistics_report.txt","w") as f:
    f.write("Car Sales Dataset Analysis: \n")
    f.write(f"\n1.Total Count numbers per Manufacture :\n{df['Manufacturer'].value_counts()} \n")
    f.write(f"\n2.Average Price by Fuel Type :\n{df.groupby("Fuel type")['Price'].mean()} \n")
    f.write(f"\n3.Oldest Year :  {df['Year of manufacture'].min()}\n")
    f.write(f"\n4.Newest Year :  {df['Year of manufacture'].max()}\n")
    f.write(f"\n5.Top 5 most common models :\n{df['Model'].value_counts().head(5)} \n")



#------3. Price distribution Visualization------

#Histogram of Car Prices
plt.figure(figsize=(8,5))
plt.hist(df['Price'], bins = 30 , color='skyblue' , edgecolor='black')
plt.title("Distribution of Car Prices ")
plt.xlabel("Price")
plt.ylabel("Number of Cars ")
plt.show()

#Box plot by Manufacture
plt.figure(figsize=(12,6))
sns.boxplot(x="Manufacturer", y = "Price", data = df)
plt.xticks(rotation=45)
plt.title("Car price Distribution by Manufacturer")
plt.show()

#Scatter Plot (Price vs Year)
plt.figure(figsize=(8,5))
plt.scatter(df['Year of manufacture'],df['Price'], alpha=0.5 , color="green")
plt.title("Price vs Year of Car")
plt.xlabel("Year")
plt.ylabel("Price")
plt.show()

#------4.Mileage Analysis------

observations = []

#Average mileage by year
avg_mileage_year = df.groupby('Year of manufacture')['Mileage'].mean()
print("\n Average mileage by year : \n",avg_mileage_year)

observations.append("Average Mileage by Year : \n")
observations.append(str(avg_mileage_year))
observations.append("\n Observations : Newer cars usually have ___ mileage compared to older cars. \n ")

#Top 5 highest mileage cars
top5_highest = df.nlargest(5,'Mileage')[['Manufacturer', 'Model' ,'Year of manufacture' , 'Mileage']]
print("\nTop 5 Highest mileage cars : \n", top5_highest)

observations.append("Top 5 Highest Mileage Cars : \n")
observations.append(str(top5_highest))
observations.append(" \n ")

#Top 5 lowest mileage cars
top5_lowest = df.nsmallest(5,'Mileage')[['Manufacturer', 'Model' ,'Year of manufacture' , 'Mileage']]
print("\nTop 5 lowest mileage cars : \n", top5_lowest)

observations.append("Top 5 Lowest Mileage Cars : \n")
observations.append(str(top5_lowest))
observations.append(" \n ")

#Compare diesel vs Petrol mileage
fuel_mileage = df.groupby('Fuel type')['Mileage'].mean()
print("\nAverage mileage by fuel type : \n",fuel_mileage)

observations.append("Average Mileage by Fuel Type : \n")
observations.append(str(fuel_mileage))
observations.append(" \n ")

#File for the Mileage analysis
with open("mileage_report.txt", "w") as f:
    f.write("Mileage Analysis Report\n\n")
    #f.write("="*20+ "\n\n")
    for line in observations:
        f.write(line + "\n")

avg_mileage_year.plot(kind='line', marker='o', title="Average Mileage by Year")
plt.xlabel("Year")
plt.ylabel("Average Mileage")
plt.show()


