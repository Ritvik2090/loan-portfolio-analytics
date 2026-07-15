# LOAN PRODUCT Table

!pip install faker

import pandas as pd
import numpy as np

from faker import Faker

import random
from datetime import datetime, timedelta

fake = Faker("en_IN")

random.seed(42)
np.random.seed(42)
Faker.seed(42)

import os

os.makedirs("generated", exist_ok=True)

import pandas as pd

loan_products = pd.DataFrame([
    {
        "id": 1,
        "product_name": "Personal Loan",
        "interest_rate": 18.0,
        "processing_fee_percent": 2.0,
        "min_loan_amount": 10000,
        "max_loan_amount": 500000,
        "max_tenure_months": 24,
        "prepayment_allowed": True,
        "is_active": 0,
        "created_at": "2023-01-01",
        "updated_at": "2024-01-01"
    },
    {
        "id": 2,
        "product_name": "Personal Loan",
        "interest_rate": 20.0,
        "processing_fee_percent": 2.0,
        "min_loan_amount": 10000,
        "max_loan_amount": 500000,
        "max_tenure_months": 24,
        "prepayment_allowed": True,
        "is_active": 1,
        "created_at": "2024-01-01",
        "updated_at": "2024-01-01"
    },
    {
        "id": 3,
        "product_name": "Gold Loan",
        "interest_rate": 12.0,
        "processing_fee_percent": 1.0,
        "min_loan_amount": 5000,
        "max_loan_amount": 300000,
        "max_tenure_months": 12,
        "prepayment_allowed": True,
        "is_active": 1,
        "created_at": "2024-01-01",
        "updated_at": "2024-01-01"
    },
    {
        "id": 4,
        "product_name": "Business Loan",
        "interest_rate": 16.0,
        "processing_fee_percent": 2.5,
        "min_loan_amount": 50000,
        "max_loan_amount": 1000000,
        "max_tenure_months": 36,
        "prepayment_allowed": True,
        "is_active": 1,
        "created_at": "2024-01-01",
        "updated_at": "2024-01-01"
    },
    {
        "id": 5,
        "product_name": "Education Loan",
        "interest_rate": 11.0,
        "processing_fee_percent": 1.0,
        "min_loan_amount": 50000,
        "max_loan_amount": 1000000,
        "max_tenure_months": 60,
        "prepayment_allowed": False,
        "is_active": 1,
        "created_at": "2024-01-01",
        "updated_at": "2024-01-01"
    },
    {
        "id": 6,
        "product_name": "Consumer Durable Loan",
        "interest_rate": 22.0,
        "processing_fee_percent": 3.0,
        "min_loan_amount": 5000,
        "max_loan_amount": 100000,
        "max_tenure_months": 18,
        "prepayment_allowed": True,
        "is_active": 1,
        "created_at": "2024-01-01",
        "updated_at": "2024-01-01"
    },
    {
        "id": 7,
        "product_name": "Medical Loan",
        "interest_rate": 15.0,
        "processing_fee_percent": 1.5,
        "min_loan_amount": 10000,
        "max_loan_amount": 500000,
        "max_tenure_months": 36,
        "prepayment_allowed": True,
        "is_active": 1,
        "created_at": "2024-01-01",
        "updated_at": "2024-01-01"
    },
    {
        "id": 8,
        "product_name": "Travel Loan",
        "interest_rate": 19.0,
        "processing_fee_percent": 2.0,
        "min_loan_amount": 10000,
        "max_loan_amount": 300000,
        "max_tenure_months": 24,
        "prepayment_allowed": True,
        "is_active": 1,
        "created_at": "2024-01-01",
        "updated_at": "2024-01-01"
    }
])

loan_products

loan_products.to_csv("loan_products.csv", index=False)

from google.colab import files

files.download("loan_products.csv")
