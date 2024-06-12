// Dynamic UI Interaction 
frappe.ui.form.on('Sales Invoice', {
    refresh: function(frm) {
        let status = frm.doc.invoice_status;
        let color = status === 'Draft' ? 'yellow' : status === 'Issued' ? 'orange' : 'green';
        frm.page.wrapper.css('background-color', color);
    }
});


// Conditional Field Visibility 
frappe.ui.form.on('Sales Invoice', {
    refresh: function(frm) {
        frm.toggle_display('sales_representative', frm.doc.invoice_status !== 'Draft');
    }
});


// Real-time Total Calculation 
frappe.ui.form.on('Sales Invoice Item', {
    item_code: function(frm, cdt, cdn) {
        calculate_total(frm, cdt, cdn);
    },
    quantity: function(frm, cdt, cdn) {
        calculate_total(frm, cdt, cdn);
    },
    rate: function(frm, cdt, cdn) {
        calculate_total(frm, cdt, cdn);
    }
});

function calculate_total(frm, cdt, cdn) {
    let item = locals[cdt][cdn];
    item.total_amount = item.quantity * item.rate;
    frm.refresh_field('invoice_items');
}


// Interactive Invoice Status Change 
frappe.ui.form.on('Sales Invoice', {
    invoice_status: function(frm) {
        frappe.confirm(
            'Are you sure you want to change the invoice status?',
            function() {
                
            },
            function() {
                
                frm.set_value('invoice_status', frm.doc.previous_status);
            }
        );
    },
    before_save: function(frm) {
        frm.doc.previous_status = frm.doc.invoice_status;
    }
});


//Data Validation on Save 
frappe.ui.form.on('Sales Invoice', {
    validate: function(frm) {
        if (frm.doc.invoice_date > frappe.datetime.now_date()) {
            frappe.msgprint('Invoice date cannot be in the future.');
            frappe.validated = false;
        }
    }
});



