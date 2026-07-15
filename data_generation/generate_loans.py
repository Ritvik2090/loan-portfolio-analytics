# LOAN Table

customers = pd.read_csv("generated/customers.csv")
loan_products = pd.read_csv("generated/loan_products.csv")

NUM_LOANS = 15000

product_weights = {
    2: 40,   # Personal Loan
    3: 15,   # Gold Loan
    4: 10,   # Business Loan
    5: 3,    # Education Loan
    6: 10,   # Consumer Durable Loan
    7: 8,    # Medical Loan
    8: 4     # Travel Loan
}

product_ids = list(product_weights.keys())
weights = list(product_weights.values())

loans = []

for loan_id in range(1, NUM_LOANS + 1):

    # -----------------------------
    # Random Customer
    # -----------------------------

    customer = customers.sample(1).iloc[0]

    # -----------------------------
    # Portfolio Growth
    # -----------------------------

    year = random.choices(
        [2023, 2024, 2025],
        weights=[20, 35, 45],
        k=1
    )[0]

    disbursed_date = fake.date_between_dates(
        date_start=datetime(year, 1, 1),
        date_end=datetime(year, 12, 31)
    )

    # -----------------------------
    # Select Loan Product
    # -----------------------------

    selected_product_id = random.choices(
        product_ids,
        weights=weights,
        k=1
    )[0]

    # Historical Personal Loan Logic
    if selected_product_id == 2 and disbursed_date < datetime(2024, 1, 1).date():
        selected_product_id = 1

    product = loan_products[
        loan_products["id"] == selected_product_id
    ].iloc[0]

    # -----------------------------
    # Loan Amount
    # -----------------------------

    loan_amount = random.randrange(
        int(product["min_loan_amount"]),
        int(product["max_loan_amount"]) + 1,
        500
    )

    # -----------------------------
    # Loan Tenure
    # -----------------------------

    tenure_months = random.randint(
        2,
        int(product["max_tenure_months"])
    )

    # -----------------------------
    # Loan Status
    # -----------------------------

    loan_status = random.choices(
        ["ACTIVE", "CLOSED"],
        weights=[70, 30],
        k=1
    )[0]

    closure_date = None

    if loan_status == "CLOSED":
        closure_date = fake.date_between_dates(
            date_start=disbursed_date,
            date_end=datetime.today()
        )

    # -----------------------------
    # Append Record
    # -----------------------------

    loans.append({
        "id": loan_id,
        "customer_id": customer["id"],
        "product_id": selected_product_id,
        "loan_amount": loan_amount,
        "tenure_months": tenure_months,
        "disbursed_date": disbursed_date,
        "loan_status": loan_status,
        "closure_date": closure_date,
        "created_at": disbursed_date,
        "updated_at": datetime.today().date()
    })

loans = pd.DataFrame(loans)

loans.head()

loans.info()

loans["loan_status"].value_counts()

loans["product_id"].value_counts().sort_index()

loans["tenure_months"].describe()

import os

os.makedirs("generated", exist_ok=True)

loans.to_csv("generated/loans.csv", index=False)

from google.colab import files

files.download("generated/loans.csv")
