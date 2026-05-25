# DataBase2
# Movie Rental Data Warehouse

## Overview
This project presents a high-level Data Warehouse (DWH) design for a movie rental system. The goal is to transform an OLTP database into a dimensional model (Star Schema) that supports analytical queries and decision-making.

## Objectives
- Understand the difference between OLTP and Data Warehouse systems
- Design a dimensional model (Star Schema)
- Identify fact tables and dimension tables
- Define grain and measures
- Design an ETL process

## Business Processes
- Rental Transactions  
- Payment Transactions  
- Inventory Snapshot  

## Dimensional Model

### Fact Tables
- Fact_Rental  
- Fact_Payment  
- Fact_Inventory

### Dimension Tables
- Dim_Date  
- Dim_Customer  
- Dim_Film  
- Dim_Store  
- Dim_Staff  

## Schema Type
Star Schema is used to simplify the OLTP structure and improve query performance. All dimensions are denormalized and linked to fact tables using surrogate keys.

## ETL Process

### Extract
Data is extracted from OLTP tables such as:
rental, payment, customer, film, inventory, store, and staff.

### Transform
- Join multiple OLTP tables to build dimensions
- Generate surrogate keys (customer_key, film_key, store_key, staff_key)
- Convert dates into date_key format
- Handle missing values (e.g., return_date)
- Calculate measures:
   -rental duration (actual_duration)
   -late return flag (is_late)
-Standardize data for analysis

### Load
- Load dimension tables first (customer, film, store, staff, date)
- Load fact tables after
- Replace operational IDs with surrogate keys in fact tables
- Ensure relationships between facts and dimensions are valid

## Data Quality Rules
- customer_id and film_id must not be null
- payment amount must be positive
- return_date must be greater than or equal to rental_date
- All fact records must match valid dimension keys
- No missing surrogate keys in fact tables

## Author
Sama Haji
Dana Bustami
Malak Waged
