import json
from decimal import Decimal

from django.test import TestCase
from django.urls import reverse

from .models import Customer, Invoice, Product


class InvoiceWorkflowTests(TestCase):
	def setUp(self):
		self.customer = Customer.objects.create(
			name='Asha Retail',
			email='asha@example.com',
		)
		self.product = Product.objects.create(
			name='Notebook',
			price=Decimal('100.00'),
			stock=5,
		)

	def post_invoice(self, **overrides):
		payload = {
			'customer': self.customer.id,
			'tax_rate': '18',
			'discount_amount': '10',
			'items': [
				{'product_id': self.product.id, 'quantity': 2, 'price': '1.00'},
			],
		}
		payload.update(overrides)
		return self.client.post(
			reverse('invoice_add'),
			data=json.dumps(payload),
			content_type='application/json',
		)

	def test_invoice_uses_database_price_and_reduces_stock(self):
		response = self.post_invoice()

		self.assertEqual(response.status_code, 200)
		invoice = Invoice.objects.get()
		self.assertEqual(invoice.subtotal, Decimal('200.00'))
		self.assertEqual(invoice.tax_amount, Decimal('36.00'))
		self.assertEqual(invoice.total_amount, Decimal('226.00'))
		self.assertEqual(invoice.items.get().unit_price, Decimal('100.00'))
		self.product.refresh_from_db()
		self.assertEqual(self.product.stock, 3)

	def test_invoice_rejects_discount_above_subtotal(self):
		response = self.post_invoice(discount_amount='999')

		self.assertEqual(response.status_code, 400)
		self.assertEqual(Invoice.objects.count(), 0)
		self.product.refresh_from_db()
		self.assertEqual(self.product.stock, 5)
