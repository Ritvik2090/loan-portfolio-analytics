# Business Rules

## Customer

- A customer can have multiple loans.
- Every loan belongs to exactly one customer.

## Loan

- Every loan has a unique loan ID.
- A loan is associated with one product.
- A loan has a fixed tenure and interest rate.
- A loan can be Active, Closed, or Written Off.

## EMI

- Every loan consists of multiple EMIs.
- Each EMI has a due date.
- Each EMI contains principal and interest components.
- Each EMI can be Paid, Pending, or Overdue.

## Payment

- A customer can make multiple payments.
- One payment may settle one or more EMIs.
- Payments can be Partial or Full.

## Collection

- Collections are recorded only when an EMI becomes overdue.
- Every collection activity is assigned to an agent.
- Multiple collection attempts may exist for the same loan.

## Collection Agent

- An agent may handle many loans.
- Every collection record belongs to one agent.
