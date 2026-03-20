# Order Management System - Python Challenge

## Project Description

As a commercial operations manager, I need a Python system that allows registering and processing customer orders.  
The goal is to have structured control of the products sold, automatically calculate totals for each order, and generate consolidated sales reports at the end of the day.

This program replaces manual Excel and paper records with an automated console application that runs entirely in memory.

## System Architecture

The system is built using only **dictionaries** and **tuples** (lists are strictly forbidden as per the technical requirements).  
All data is stored in global dictionaries during program execution. The code is fully modularized with reusable functions that receive parameters and always return values.

## Data Structures Used

- **clients** (dictionary):  
  `client_id → {"name": str, "email": str}`

- **products** (dictionary of tuples):  
  `product_id → (product_id, name, unit_price)`  
  (Tuple used because product data is immutable)

- **orders** (dictionary):  
  `order_id → {"client_id": int, "product_id": int, "quantity": int, "total": float}`


```bash
python main.py
