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
- Fact_Inventory_Daily_Snapshot  

### Dimension Tables
- Dim_Date  
- Dim_Customer  
- Dim_Film  
- Dim_Store  
- Dim_Staff  

## Schema Type
Star Schema is used to simplify the OLTP structure and improve query performance. All dimensions are denormalized.

## ETL Process

### Extract
Data is extracted from OLTP tables such as rental, payment, film, customer, inventory, store, and staff.

### Transform
- Join tables to create dimensions  
- Clean missing and invalid data  
- Convert date formats  
- Calculate rental duration and late return flag  
- Generate surrogate keys  

### Load
- Load dimension tables first  
- Load fact tables after  
- Replace operational IDs with surrogate keys  

## Data Quality Rules
- rental_id and customer_id must not be null  
- payment_amount must be positive  
- return_date must be after rental_date  
- All fact records must match dimension records  

## Author
Sama Haji
Dana Bustami
Malak Waged
