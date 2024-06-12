# Basic Data Retrieval
from settings import fetch_sales_invoices
fetch_sales_invoices()

# Filtering and Sorting
def fetch_sales_invoices_by_customer(customer_name):
    invoices = frappe.get_all('Sales Invoice', filters={'customer': customer_name}, fields=['name', 'invoice_date', 'total'], order_by='invoice_date')
    for invoice in invoices:
        print(f"Invoice Number: {invoice.name}, Date: {invoice.invoice_date}, Total Amount: {invoice.total}")

fetch_sales_invoices_by_customer('Customer Name')


# Data Aggregation
def calculate_total_revenue(customer_name):
    invoices = frappe.get_all('Sales Invoice', filters={'customer': customer_name}, fields=['total'])
    total_revenue = sum(invoice.total for invoice in invoices)
    print(f"Total Revenue: {total_revenue}")

calculate_total_revenue('Customer Name')


# Dynamic query with parameters
def fetch_invoices_by_date_range(start_date, end_date):
    invoices = frappe.get_all('Sales Invoice', filters={'invoice_date': ['between', (start_date, end_date)]}, fields=['name', 'invoice_date', 'total'])
    for invoice in invoices:
        print(f"Invoice Number: {invoice.name}, Date: {invoice.invoice_date}, Total Amount: {invoice.total}")

fetch_invoices_by_date_range('2023-01-01', '2023-12-31')


# Complex Data Processing
def find_top_sales_representative():
    sales_reps = frappe.get_all('Sales Invoice', fields=['sales_representative', 'total'])
    sales_totals = {}

    for invoice in sales_reps:
        sales_rep = invoice.sales_representative
        total = invoice.total
        if sales_rep in sales_totals:
            sales_totals[sales_rep] += total
        else:
            sales_totals[sales_rep] = total

    top_sales_rep = max(sales_totals, key=sales_totals.get)
    print(f"Top Sales Representative: {top_sales_rep}, Total Sales: {sales_totals[top_sales_rep]}")

find_top_sales_representative()


