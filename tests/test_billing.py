# Unit Tests for Billing Module

import unittest
from billing import generate_quotation, create_sales_order, create_purchase_order, create_invoice, send_inspection_email_reminder

class TestBilling(unittest.TestCase):
    def test_generate_quotation(self):
        details = {"item": "Service", "amount": 100}
        result = generate_quotation(details)
        self.assertEqual(result, "Quotation generated successfully.")

    def test_create_sales_order(self):
        order_details = {"order_id": 1, "item": "Product", "quantity": 2}
        result = create_sales_order(order_details)
        self.assertEqual(result, "Sales order created successfully.")

    def test_create_purchase_order(self):
        order_details = {"order_id": 2, "item": "Service", "quantity": 1}
        result = create_purchase_order(order_details)
        self.assertEqual(result, "Purchase order created successfully.")

    def test_create_invoice(self):
        billing_details = {"invoice_id": 1, "amount": 200}
        result = create_invoice(billing_details)
        self.assertEqual(result, "Invoice created successfully.")

    def test_send_inspection_email_reminder(self):
        recipient = "test@example.com"
        inspection_details = {"date": "2023-12-01", "type": "Annual Inspection"}
        result = send_inspection_email_reminder(recipient, inspection_details)
        self.assertEqual(result, "Inspection email reminder sent successfully.")

if __name__ == '__main__':
    unittest.main()
