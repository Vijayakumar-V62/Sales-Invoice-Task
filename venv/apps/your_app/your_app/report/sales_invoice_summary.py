def execute(filters=None):
    columns, data = [], []
    columns = [
        {"label": "Total Revenue", "fieldtype": "Currency", "width": 120},
        {"label": "Average Invoice Value", "fieldtype": "Currency", "width": 120},
        {"label": "Sales Representative", "fieldtype": "Data", "width": 150},
        {"label": "Total Sales", "fieldtype": "Currency", "width": 120}
    ]

    invoices = frappe.get_all('Sales Invoice', fields=['total'])
    total_revenue = sum(invoice.total for invoice in invoices)
    average_invoice_value = total_revenue / len(invoices) if invoices else 0

    sales_reps = frappe.get_all('Sales Invoice', fields=['sales_representative', 'total'])
    sales_totals = {}

    for invoice in sales_reps:
        sales_rep = invoice.sales_representative
        total = invoice.total
        if sales_rep in sales_totals:
            sales_totals[sales_rep] += total
        else:
            sales_totals[sales_rep] = total

    data.append([total_revenue, average_invoice_value, "", ""])

    for sales_rep, total_sales in sales_totals.items():
        data.append(["", "", sales_rep, total_sales])

    return columns, data

def update_invoice_status(invoice_name):
    invoice = frappe.get_doc('Sales Invoice', invoice_name)
    if invoice.payment_status == 'Paid':
        invoice.invoice_status = 'Paid'
        invoice.save()
    elif invoice.payment_status == 'Pending':
        invoice.invoice_status = 'Pending Approval'
        invoice.save()

update_invoice_status('Invoice Name')

