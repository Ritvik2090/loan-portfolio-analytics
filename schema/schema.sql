-- ============================================
-- Loan Portfolio Analytics Database Schema
-- ============================================

-- =================
-- Customers Table
-- =================

CREATE TABLE customers (
    id INT PRIMARY KEY,
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
    created_at TIMESTAMP NOT NULL,
    updated_at TIMESTAMP NOT NULL
);

-- ====================
-- Loan Products Table
-- ====================

CREATE TABLE loan_products (
    id INT PRIMARY KEY,
    product_name VARCHAR(50) NOT NULL,
    interest_rate DECIMAL(5,2) NOT NULL,
    processing_fee_percent DECIMAL(5,2) NOT NULL,
    amount DECIMAL(12,2) NOT NULL,
    tenure_months INT NOT NULL,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP NOT NULL,
    updated_at TIMESTAMP NOT NULL
);

-- ============
-- Loans Table
-- ============

CREATE TABLE loans (
    id INT PRIMARY KEY,
    customer_id INT NOT NULL,
    product_id INT NOT NULL,
    loan_amount DECIMAL(12,2) NOT NULL,
    disbursed_at TIMESTAMP NOT NULL,
    loan_status VARCHAR(20) NOT NULL,
    closure_date TIMESTAMP,
    created_at TIMESTAMP NOT NULL,
    updated_at TIMESTAMP NOT NULL,

    FOREIGN KEY (customer_id) REFERENCES customers(id),
    FOREIGN KEY (product_id) REFERENCES loan_products(id)
);

-- ==========
-- EMI Table
-- ==========

CREATE TABLE emis (
    id INT PRIMARY KEY,
    loan_id INT NOT NULL,
    due_date DATE NOT NULL,
    emi_amount DECIMAL(12,2) NOT NULL,
    principal_amount DECIMAL(12,2) NOT NULL,
    interest_amount DECIMAL(12,2) NOT NULL,
    status VARCHAR(20) NOT NULL
        CHECK (status IN ('PENDING', 'PAID')),
    created_at TIMESTAMP NOT NULL,
    updated_at TIMESTAMP NOT NULL,

    FOREIGN KEY (loan_id) REFERENCES loans(id)
);

-- ===============
-- Payments Table
-- ===============

CREATE TABLE payments (
    id INT PRIMARY KEY,
    loan_id INT NOT NULL,
    emi_id INT NOT NULL,
    payment_event_id NOT NULL,
    principal_paid DECIMAL(12,2) NOT NULL,
    interest_paid DECIMAL(12,2) NOT NULL,
    created_at TIMESTAMP NOT NULL,
    updated_at TIMESTAMP NOT NULL,

    FOREIGN KEY (loan_id) REFERENCES loans(id),
    FOREIGN KEY (emi_id) REFERENCES emis(id),
    FOREIGN KEY (payment_event_id) REFERENCES payment_event(id)
);

-- ====================
-- Payment Events Table
-- ====================

CREATE TABLE payment_event (
    id INT PRIMARY KEY,
    paid_amount DECIMAL(12,2) NOT NULL,
    payment_date TIMESTAMP NOT NULL,
    payment_mode VARCHAR(20),
    created_at TIMESTAMP NOT NULL,
    updated_at TIMESTAMP NOT NULL,
);
    
