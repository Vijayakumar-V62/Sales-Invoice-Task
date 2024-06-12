# Basic Data Retrieval
from settings import get_all_sales_invoices
get_all_sales_invoices()

# Filtering and Sorting
def fetch_invoices_by_customer(customer_name):
    invoices = frappe.get_all("Sales Invoice", filters={"customer": customer_name}, fields=["name", "invoice_date", "total_amount"], order_by="invoice_date asc")
    for invoice in invoices:
        print(f"Invoice Number: {invoice.name}, Date: {invoice.invoice_date}, Total Amount: {invoice.total_amount}")

fetch_invoices_by_customer("Customer Name")

# Data Aggregation
def calculate_total_revenue():
    invoices = frappe.get_all("Sales Invoice", fields=["total_amount"])
    total_revenue = sum(invoice.total_amount for invoice in invoices)
    print(f"Total Revenue: {total_revenue}")

calculate_total_revenue()

# Dynamic query with parameters
def fetch_invoices_by_date_range(start_date, end_date):
    invoices = frappe.get_all("Sales Invoice", filters={"invoice_date": ["between", [start_date, end_date]]}, fields=["name", "invoice_date", "total_amount"])
    for invoice in invoices:
        print(f"Invoice Number: {invoice.name}, Date: {invoice.invoice_date}, Total Amount: {invoice.total_amount}")

fetch_invoices_by_date_range("2023-01-01", "2023-12-31")

# Complex Data Processing
def sales_representative_with_highest_sales():
    invoices = frappe.get_all("Sales Invoice", fields=["sales_representative", "total_amount"])
    sales_data = {}
    for invoice in invoices:
        rep = invoice.sales_representative
        amount = invoice.total_amount
        if rep in sales_data:
            sales_data[rep] += amount
        else:
            sales_data[rep] = amount

    top_rep = max(sales_data, key=sales_data.get)
    print(f"Top Sales Representative: {top_rep}, Total Sales: {sales_data[top_rep]}")

sales_representative_with_highest_sales()



