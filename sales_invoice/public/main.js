// Dynamic UI Interaction 
frappe.ui.form.on('Sales Invoice', {
    refresh(frm) {
        if (frm.doc.invoice_status == 'Draft') {
            frm.$wrapper.css('background-color', '#f9f9f9');
        } else if (frm.doc.invoice_status == 'Issued') {
            frm.$wrapper.css('background-color', '#fff5e6');
        } else if (frm.doc.invoice_status == 'Paid') {
            frm.$wrapper.css('background-color', '#e6fff5');
        }
    }
});

// Conditional Field Visibility 
frappe.ui.form.on('Sales Invoice', {
    refresh(frm) {
        if (frm.doc.invoice_status == 'Draft') {
            frm.toggle_display('sales_representative', false);
        } else {
            frm.toggle_display('sales_representative', true);
        }
    }
});

// Real-time Total Calculation 
frappe.ui.form.on('Sales Invoice Item', {
    item_code(frm) {
        frm.trigger('calculate_total_amount');
    },
    quantity(frm) {
        frm.trigger('calculate_total_amount');
    },
    rate(frm) {
        frm.trigger('calculate_total_amount');
    }
});

frappe.ui.form.on('Sales Invoice', {
    calculate_total_amount(frm) {
        let total = 0;
        frm.doc.invoice_items.forEach(item => {
            total += (item.quantity * item.rate);
        });
        frm.set_value('total_amount', total);
    }
});

// Interactive Invoice Status Change 
frappe.ui.form.on('Sales Invoice', {
    invoice_status(frm) {
        frappe.confirm(
            'Are you sure you want to change the status?',
            function() {
            },
            function() {
                frm.set_value('invoice_status', frm.doc.previous_status);
            }
        );
    },
    before_save(frm) {
        frm.doc.previous_status = frm.doc.invoice_status;
    }
});

//Data Validation on Save 
frappe.ui.form.on('Sales Invoice', {
    before_save(frm) {
        if (new Date(frm.doc.invoice_date) > new Date()) {
            frappe.msgprint(__('Invoice Date cannot be in the future'));
            frappe.validated = false;
        }
    }
});


