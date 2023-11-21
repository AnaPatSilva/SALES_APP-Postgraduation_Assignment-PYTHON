![Image](https://github.com/AnaPatSilva/Sales_App-Python/blob/main/Captura%20de%20ecr%C3%A3%202023-11-21%20115257.jpg)
# Sales App (Postgraduation Assignment)
# PYTHON

## My Intro
For the algorithm and programming in python module of my postgraduation I had to make an sales app in Python.

This was my first assignment using Python.

## Intro
**Aim:** Development of a Sales app

The application consists of processing information from a Sales data structure (part1) and the corresponding data outputs (part2).

- **PART 1 - The Sales structure is defined by:**

o Sales ID (integer: incremental 1 / 2 / 3 / 4 / ...)

o Salesman Code (integer: 100 / 200 / 300 / ...)

o Customer Name (string; "Customer1", "Customer2", ...)

o Zone (string: North("N") / Center("C") / South("S") / Islands("I"))

o Date (string with format "dd/mm/yyyy")

o Product code (string: "ABC100", "XYAS12", "XPTO1", ...)

o Quantity (integer: 1 / 2 / 5 / 7 / ...)

o Sale value (float €)

Example of sales records in a list:

[[1, 100, "N", "Customer1", "02/01/2021", 1234.45, "ABC100"],

[2, 100, "S", "Customer1", "02/01/2021", 234.2, "XPTO1"],

[3, 200, "C", "Customer3", "02/01/2021", 1142.64, "XPTO1"],

[4, 300, "C", "Client4", "03/01/2021", 1253.9, "XYAS12"], ... ]

The logic of relationships is that a seller can sell several products. They can do so on the same date (or on different dates), in the same area (or in different areas) and at the same or different prices. Each sale generates an incremental sales record. The same customer can exist in different zones.

o Planned functions: Insert / Consult / List / Change / Delete

- **PART2 - Expected outputs:**

o Total sales by Salesperson

o Total sales by Customer

o Total sales by Product

o Total sales by Zone

o Total sales per month for each salesperson

o ---

o Total Sales and Quantities by Customer / Salesperson

o Total Sales and Quantities by Zone / Product

o Total Sales and Quantities by Customer / Product

o ---

o Total Sales by Salesperson / Month

o Total Sales per Customer in the month: x

o List of Customers above the global sales average

o List of Salespeople below the salespeople's sales average


**Restrictions:**

o Consider only Sales for the year 2022

o Work with a list: lv

o Create a data file with enough volume to obtain the outputs listed

o Save the information in a text file in CSV format (comma separated value: ";") and allow the list to be read and written to a text file

o Validate numerical entries



## Structure
**1. Imported Libraries:**
- datetime: for working with dates
- pandas: for data manipulation and analysis

**2. Functions:**
- valnumero(msg): Validates numerical input.
- valvend(msg): Validates vendor code input.
- valzona(msg): Validates zone input.
- valdata(msg): Validates date input.
- Several menu-related functions (menu, menu_cons, menu_list, menu_alt, menu_eli, menu_out) for user interaction.

**3. Data Structure:**
- List "lv" is used to store records of sales, where each record is a list containing various details like ID, vendor code, client designation, zone, date, product code, quantity, and sale value.

**4. Menu Options:**
- User can choose from options like inserting, consulting, listing, altering, deleting, saving to a file, reading from a file, and generating outputs.

**5. User Interaction:**
- The program uses a loop to repeatedly present a menu to the user until they choose to exit.
- Various input validations are implemented to ensure correct user input.

**6. Data Manipulation:**
- The code allows users to insert, consult, list, alter, and delete sales records.
- Sales records can be saved to a file (dados_vendas.csv) and read from it.
- Outputs can be generated, such as total sales per vendor, client, product, zone, and various combinations.

**7. Pandas DataFrame:**
- Utilizes the Pandas library to create a DataFrame (df) for data manipulation and analysis.

**8. File Handling:**
- Saves and loads sales data to/from a CSV file.

**9. Output Generation:**
- Generates various types of outputs based on user selection using Pandas groupby operations.

**10. Statistical Analysis:**
- Computes and displays statistics such as clients above the global average of sales and vendors below the average of sales.

**11. Exception Handling:**
- The code includes exception handling to deal with potential errors during user input.

## Conclusions
It was a very challenging assignment, forcing me to spend many hours researching and frustrated attempts. But it was the best thing for me to learn and feel more comfortable working in Python.
