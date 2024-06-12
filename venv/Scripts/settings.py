import frappe

def get_all_sales_invoices():
    invoices = frappe.get_all("Sales Invoice", fields=["name", "invoice_date", "total_amount"])
    for invoice in invoices:
        print(invoice)
