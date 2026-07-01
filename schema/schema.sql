-- ============================================
-- Loan Portfolio Analytics Database Schema
-- ============================================

CREATE TABLE customers (
    customer_id INT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    gender VARCHAR(10),
    date_of_birth DATE,
    phone_number VARCHAR(15) UNIQUE,
    email VARCHAR(100) UNIQUE,
    city VARCHAR(50),
    state VARCHAR(50),
    employment_type VARCHAR(30),
    monthly_income DECIMAL(12,2),
    created_at DATE
);
