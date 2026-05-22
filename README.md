# Expense Sharing & Settlement System

## Project Overview

This project is a Python-based expense sharing and settlement system designed to simplify group expense management among friends or teams. The application calculates shared expenses, tracks balances, and generates optimized settlements showing who owes money to whom.

The project demonstrates practical Python programming concepts including:

* Object-Oriented Programming (OOP)
* Dictionaries and lists
* Loops and conditional logic
* User input handling
* Financial calculation logic

This project is ideal for beginners learning Python through real-world financial use cases.

---

## Business Problem

Managing shared expenses manually during trips, events, or team activities can become complex and error-prone. This project automates:

* Expense splitting
* Balance tracking
* Debt calculation
* Optimized settlements

The system minimizes confusion and provides transparent payment tracking among participants.

---

## Project Objectives

The primary objectives of this project are:

* Build a real-world Python application
* Practice Object-Oriented Programming concepts
* Implement financial calculation logic
* Track shared expenses dynamically
* Generate optimized settlements
* Improve problem-solving and logical thinking

---

## Features

### Expense Management

* Add multiple friends
* Record expenses dynamically
* Track who paid
* Track participants involved in each expense

### Automatic Expense Splitting

* Divides expenses equally among participants
* Updates balances automatically

### Balance Tracking

* Maintains individual balances
* Identifies creditors and debtors

### Optimized Settlements

The program calculates:

* Who owes money
* Who should receive money
* Minimum transactions required for settlement

---

## Technologies Used

### Programming Language

* Python 3

### Core Concepts

* Classes & Objects
* Dictionaries
* Lists
* Loops
* Functions
* Conditional Statements
* Input Handling

---

## Project Workflow

### Step 1 — Add Friends

The user enters participant names.

Example:

```bash id="p1x4rm"
Enter the names of friends, separated by commas:
Arun, Kiran, Ravi
```

---

### Step 2 — Record Expenses

The program asks:

* Who paid?
* Amount paid
* Participants sharing the expense

Example:

```bash id="m8k2tv"
Who paid? Arun
How much did Arun pay? ₹1200
Who shared this expense? Arun, Kiran, Ravi
```

---

### Step 3 — Balance Calculation

The application:

* Splits expenses equally
* Updates balances automatically
* Tracks debtor and creditor amounts

---

### Step 4 — Settlement Generation

The system generates optimized settlement outputs.

Example:

```bash id="n7v3qp"
Ravi owes Arun: ₹400.00
Kiran owes Arun: ₹400.00
```

---

## Object-Oriented Design

### Main Class

```python id="j2t6yb"
class ExpenseSharing:
```

The class handles:

* Expense storage
* Balance calculation
* Settlement generation

---

## Core Methods

### add_expense()

Responsible for:

* Splitting expenses
* Updating balances

### calculate_settlements()

Responsible for:

* Identifying creditors
* Identifying debtors
* Generating optimized payments

---

## Data Structures Used

| Structure              | Purpose             |
| ---------------------- | ------------------- |
| Dictionary             | Store balances      |
| List                   | Store participants  |
| Loops                  | Process settlements |
| Conditional Statements | Validate logic      |

---

## Example Output

```bash id="v5m8xz"
--- Final Balances ---

Arun: ₹800.00
Kiran: -₹400.00
Ravi: -₹400.00

--- Optimized Settlements ---

Kiran owes Arun: ₹400.00
Ravi owes Arun: ₹400.00
```

---

## Repository Structure

```bash id="c7n4wy"
expense-sharing-system/
│
├── google2.py
├── README.md
├── requirements.txt
└── LICENSE
```

---

## Installation

### Clone Repository

```bash id="b6r2kp"
git clone https://github.com/your-username/expense-sharing-system.git
```

### Navigate to Project Folder

```bash id="t4v8xm"
cd expense-sharing-system
```

---

## Running the Program

Execute the Python file:

```bash id="r9m3qe"
python google2.py
```

---

## Learning Outcomes

This project helps practice:

* Python fundamentals
* OOP concepts
* Financial logic implementation
* Real-world automation workflows
* Data structure usage
* Problem-solving skills

---

## Future Enhancements

Potential future improvements:

* GUI using Tkinter or Streamlit
* Database integration
* Expense history tracking
* Currency conversion support
* Export settlement reports
* Mobile/web application deployment

---

## References

* [Python Official Documentation](https://docs.python.org/3/?utm_source=chatgpt.com)
* [Python Classes Documentation](https://docs.python.org/3/tutorial/classes.html?utm_source=chatgpt.com)

---

## License

This project is developed for educational, analytical, and portfolio-building purposes.

