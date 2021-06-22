# Expense-Tracker

Tracking of expense is very important for financial helalth of budget.
You need to keep a record of your daily expenses and stocks in a proper format 
so that you can analyze all your expenditures efficiently and correctly.
Expense tracker is a simple project developed using python which helps us to analyse 
our expenses by graph between expense and income.

Project uses Tkinter for GUI.

# Getting Started
### Project Prerequisites
- Basic concepts of Python
- Tkinter

### Installation Requirenments:
- pip install Pillow
- Pip install sqlite3

### Steps for database connectivity:

1. Import sqlite3

2. Create a connection object
conn=sqlite3.connect("income.db")
 conn=sqlite3.connect("expense.db")

3. Create cursor object
cur=conn.cursor()

4. Execute required query

5. Commit

# Running the tests

**View Expense tab:** It reads every row of expenses table displays on the tkinter window.

**Add income tab:** It takes input from user about amount and source of income and store it in the income.db table in database.

**income expense curve tab:** It contains button when clicked on it, it shows line graph between income and expense.

**Outputs:**

![Preview of Layout](https://github.com/VaibhaviKhachane/Expense-Tracker/blob/main/Capture1.JPG?raw=true)
![Preview of Layout](https://github.com/VaibhaviKhachane/Expense-Tracker/blob/main/Capture2.JPG?raw=true)
![Preview of Layout](https://github.com/VaibhaviKhachane/Expense-Tracker/blob/main/Capture3.JPG?raw=true)

