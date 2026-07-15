# CUSTOMER Table

import os

os.makedirs("generated", exist_ok=True)

loan_products.to_csv("generated/loan_products.csv", index=False)

cities = {
    "Bangalore": "Karnataka",
    "Mumbai": "Maharashtra",
    "Delhi": "Delhi",
    "Hyderabad": "Telangana",
    "Chennai": "Tamil Nadu",
    "Pune": "Maharashtra",
    "Ahmedabad": "Gujarat",
    "Kolkata": "West Bengal",
    "Jaipur": "Rajasthan",
    "Lucknow": "Uttar Pradesh"
}

customers = []

for customer_id in range(1, 10001):

    city = random.choice(list(cities.keys()))

    employment = random.choices(
        ["Salaried", "Self-Employed"],
        weights=[70, 30]
    )[0]

    if employment == "Salaried":
        income = random.randint(25000, 150000)
    else:
        income = random.randint(30000, 300000)

    dob = fake.date_of_birth(
        minimum_age=21,
        maximum_age=60
    )

    customers.append({

        "id": customer_id,

        "first_name": fake.first_name(),

        "last_name": fake.last_name(),

        "gender": random.choice(["Male", "Female"]),

        "date_of_birth": dob,

        "phone_number": f"9{random.randint(100000000,999999999)}",

        "email": f"user{customer_id}@example.com",

        "city": city,

        "state": cities[city],

        "employment_type": employment,

        "monthly_income": income,

        "created_at": fake.date_between(
            start_date="-3y",
            end_date="-1y"
        ),

        "updated_at": datetime.today().date()

    })

customers = pd.DataFrame(customers)

customers.head()

customers.info()

customers["employment_type"].value_counts()

customers["city"].value_counts()

customers.to_csv(
    "generated/customers.csv",
    index=False
)

from google.colab import files

files.download("generated/customers.csv")
