from django.test import TestCase
from django.http import HttpRequest

from myapp.views import index, fill_order_model, generate_report

# Create your tests here.

class GenerateReportTest(TestCase):

    def test_root_url_resolves_to_index(self):
        print('Executing test_root_url_resolves_to_index...')
        request = HttpRequest()
        response = index(request)
        json_response = response.content.decode('utf8')
        self.assertEqual('[]', json_response)

    def test_correct_filename_at_fill_order_model(self):
        print('Executing test_correct_filename_at_fill_order_model...')
        response = fill_order_model(HttpRequest())
        json_response = response.content.decode('utf8')
        self.assertIn('was processed successfully', json_response)

    def test_invalid_date(self):
        print('Executing test_invalid_date...')
        request = HttpRequest()
        request.GET['date'] = '2019-0a8-01'
        response = generate_report(request)
        json_response = response.content.decode('utf8')
        self.assertIn('Incorrectly formatted date', json_response)

    def test_valid_date(self):
        print('Executing test_valid_date...')
        request = HttpRequest()
        request.GET['date'] = '2019-08-01'
        response = generate_report(request)
        json_response = response.content.decode('utf8')
        self.assertIn('items', json_response)
