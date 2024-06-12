import frappe

def fetch_sales_invoices():
    invoices = frappe.get_all('Sales Invoice', fields=['name', 'invoice_date', 'total'])
    for invoice in invoices:
        print(f"Invoice Number: {invoice.name}, Date: {invoice.invoice_date}, Total Amount: {invoice.total}")



