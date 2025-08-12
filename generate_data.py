import csv
import random
import os
from datetime import datetime, timedelta

# Ensure the data folder exists
os.makedirs("data", exist_ok=True)

# Realistic Egyptian names
egyptian_names = [
    "Ahmed Mohamed", "Mohamed Ali", "Fatma Hassan", "Sara Ibrahim",
    "Omar Youssef", "Mona Adel", "Hussein Khaled", "Nadia Mostafa",
    "Mahmoud Samir", "Yasmin Farouk", "Tamer Hany", "Dina Sherif"
]

crime_types = ["Theft", "Assault", "Fraud", "Forgery", "Vandalism", "None"]
cities     = ["Cairo", "Giza", "Alexandria", "Aswan", "Luxor", "Hurghada"]
genders    = ["Male", "Female"]

num_records = 1000
start_date  = datetime(2015, 1, 1)
end_date    = datetime(2025, 8, 1)

def random_date(start, end):
    delta = end - start
    return start + timedelta(days=random.randint(0, delta.days))

csv_path = "data/crimes_egypt.csv"

with open(csv_path, 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(["Name", "CrimeType", "CrimeDate", "City", "Gender"])
    for _ in range(num_records):
        name   = random.choice(egyptian_names)
        crime  = random.choices(crime_types, weights=[3,2,2,1,1,3])[0]
        date   = random_date(start_date, end_date).strftime('%Y-%m-%d')
        city   = random.choice(cities)
        gender = random.choice(genders)
        writer.writerow([name, crime, date, city, gender])

print(f"Generated data with Egyptian names at `{csv_path}`")
import csv
import random
import os
from datetime import datetime, timedelta

# Ensure we use the local data/ folder
os.makedirs("data", exist_ok=True)

#  Egyptian names
egyptian_names = [
    "Ahmed Mohamed", "Mohamed Ali", "Fatma Hassan", "Sara Ibrahim",
    "Omar Youssef", "Mona Adel", "Hussein Khaled", "Nadia Mostafa",
    "Mahmoud Samir", "Yasmin Farouk", "Tamer Hany", "Dina Sherif"
]

crime_types = ["Theft", "Assault", "Fraud", "Forgery", "Vandalism", "None"]
cities     = ["Cairo", "Giza", "Alexandria", "Aswan", "Luxor", "Hurghada"]
genders    = ["Male", "Female"]

num_records = 1000
start_date  = datetime(2015, 1, 1)
end_date    = datetime(2025, 8, 1)

def random_date(start, end):
    delta = end - start
    return start + timedelta(days=random.randint(0, delta.days))

csv_path = "data/crimes_egypt.csv"

with open(csv_path, 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(["Name", "CrimeType", "CrimeDate", "City", "Gender"])
    for _ in range(num_records):
        name   = random.choice(egyptian_names)
        crime  = random.choices(crime_types, weights=[3,2,2,1,1,3])[0]
        date   = random_date(start_date, end_date).strftime('%Y-%m-%d')
        city   = random.choice(cities)
        gender = random.choice(genders)
        writer.writerow([name, crime, date, city, gender])

print(f" Generated data with Egyptian names in `{csv_path}`")
