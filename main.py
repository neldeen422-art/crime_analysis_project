from pyspark.sql import SparkSession
import matplotlib.pyplot as plt
import pandas as pd

# Start Spark session
spark = SparkSession.builder \
    .appName("Egypt Crime Analysis") \
    .config("spark.sql.session.timeZone", "Africa/Cairo") \
    .getOrCreate()

# Load data from relative path
csv_path = "file:///home/Nour/Pictures/crime_analysis_project/data/crimes_egypt.csv"
df = spark.read.csv(csv_path, header=True, inferSchema=True)

# Remove innocent entries
df = df.filter(df.CrimeType != "None")

# Convert to Pandas for plotting
pdf = df.toPandas()

# --- Figure 1: Crime Type Distribution ---
type_counts = pdf['CrimeType'].value_counts()
plt.figure(figsize=(8, 6))
plt.pie(type_counts.values, labels=type_counts.index, autopct='%1.1f%%')
plt.title("Crime Type Distribution in Egypt")
plt.axis('equal')

# --- Figure 2: Crimes per City ---
city_counts = pdf['City'].value_counts()
plt.figure(figsize=(10, 6))
plt.bar(city_counts.index, city_counts.values)
plt.title("Number of Crimes by City")
plt.xlabel("City")
plt.ylabel("Number of Crimes")
plt.xticks(rotation=45)
plt.tight_layout()

# --- Figure 3: Top 5 Offenders ---
offender_counts = pdf['Name'].value_counts().head(5)
plt.figure(figsize=(10, 6))
plt.bar(offender_counts.index, offender_counts.values)
plt.title("Top 5 Offenders (Most Crimes)")
plt.xlabel("Person Name")
plt.ylabel("Number of Crimes")
plt.xticks(rotation=45)
plt.tight_layout()

# --- Figure 4: Crimes per Year ---
pdf['CrimeDate'] = pd.to_datetime(pdf['CrimeDate'])
pdf['Year'] = pdf['CrimeDate'].dt.year
year_counts = pdf['Year'].value_counts().sort_index()
plt.figure(figsize=(10, 6))
plt.plot(year_counts.index, year_counts.values, marker='o')
plt.title("Number of Crimes per Year")
plt.xlabel("Year")
plt.ylabel("Number of Crimes")
plt.xticks(year_counts.index, rotation=45)
plt.tight_layout()

# Display all four figures
plt.show()

# --- Interactive: individual record lookup ---
name_input = input("Enter full name to view detailed record: ").strip()
person_pdf = pdf[pdf['Name'] == name_input]

if person_pdf.empty:
    print(f"No records found for '{name_input}'")
else:
    # Print detailed table
    print(f"\nDetailed Criminal Records for: {name_input}\n")
    print(person_pdf[['Name', 'CrimeType', 'CrimeDate', 'City', 'Gender']].to_string(index=False))

    # Keep only latest 4 crimes for timeline
    timeline = person_pdf.sort_values('CrimeDate', ascending=False).head(8).sort_values('CrimeDate')

    # Plot crime timeline
    plt.figure(figsize=(10, 4))
    plt.plot(timeline['CrimeDate'], timeline['CrimeType'], marker='o', linestyle='-')
    plt.title(f"Latest 8 Crimes Timeline for {name_input}")
    plt.xlabel("Date")
    plt.ylabel("Crime Type")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

spark.stop()
