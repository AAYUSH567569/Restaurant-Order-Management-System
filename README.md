# Restaurant Order Management System

**PS No.: 31**

## 1. Introduction
The Restaurant Order Management System is a console-based Python application designed to manage restaurant orders and generate customer bills. It allows a waiter to select a table, enter food orders, view the running order, and calculate the final bill.

## 2. Objectives
- To manage restaurant orders efficiently.
- To store menu items and prices using a dictionary.
- To maintain orders for tables using lists.
- To calculate the subtotal, service charge, GST, and final bill.
- To validate table numbers, item names, and quantities.

## 3. Technologies Used
- Programming Language: Python 3
- Interface: Console
- Concepts: Lists, Dictionaries, Loops, Conditional Statements, Exception Handling, and Billing Calculations.

## 4. Menu

| Item | Price |
|---|---:|
| Burger | Rs. 100 |
| Pizza | Rs. 200 |
| Coffee | Rs. 50 |

Table numbers range from 1 to 20.

## 5. Working of the System
1. Display the restaurant menu.
2. Ask the waiter to enter a table number.
3. Validate the table number.
4. Accept multiple food items and their quantities.
5. Display the running order and item amounts.
6. Calculate the subtotal.
7. Add a 10% service charge and 5% GST, both on the subtotal.
8. Display the final bill.

## 6. Billing Formula

Service Charge = Subtotal × 10%

GST = Subtotal × 5%

Final Total = Subtotal + Service Charge + GST

## 7. Test Cases

| Test | Input | Expected Result |
|---|---|---|
| Normal | Burger × 2 | Subtotal Rs. 200; Total Rs. 230 |
| Minimum | Coffee × 1 | Subtotal Rs. 50; Total Rs. 57.50 |
| Invalid item | Pasta | Display invalid menu item message |
| Invalid quantity | abc | Display invalid quantity message |
| Invalid table | 0 | Display invalid table number message |
| Multiple items | Burger × 2, Pizza × 1, Coffee × 4 | Subtotal Rs. 600; Total Rs. 690 |

## 8. Advantages
- Simple and easy-to-use console interface.
- Fast bill calculation.
- Supports multiple food items per order.
- Handles invalid inputs.
- Reduces manual billing errors.

## 9. Limitations
- The system does not use a database.
- Orders are stored only while the program is running.
- The application does not provide a graphical user interface.

## 10. Conclusion
The Restaurant Order Management System demonstrates the use of Python dictionaries, lists, loops, input validation, and arithmetic operations in a real-world restaurant billing scenario. It helps manage orders and generate accurate bills efficiently.
