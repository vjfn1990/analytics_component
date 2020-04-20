import json
import pandas as pd
from dateutil.parser import parse

from django.http import HttpResponse
from django.conf import settings as conf_settings

from myapp.models import Order, OrderLine

# Create your views here.

def index(request):
    return HttpResponse(json.dumps([]), content_type = 'application/json')

def generate_report(request):
    report_date = request.GET.get('date', None)
    try:
        report_date = parse(report_date)
    except ValueError:
        return HttpResponse(json.dumps('Incorrectly formatted date'), content_type = 'application/json')
    orders = Order.objects.filter(created_at = report_date)
    total_orders = 0
    for order in orders:
        total_orders += OrderLine.objects.filter(order = order).count()
    return HttpResponse(json.dumps({'items': total_orders}), content_type = 'application/json')

def fill_order_model(request):
    Order.objects.all().delete()
    try:
        df = pd.read_csv(conf_settings.PROJECT_ROOT+'/myapp/data/orders.csv')
    except FileNotFoundError:
        return HttpResponse(json.dumps('orders.csv not found'), content_type = 'application/json')
    for index, row in df.iterrows():
        print('Processing line ' + str(index) + '...')
        Order(
            identifier = row['id'],
            created_at = row['created_at'][0:10],
            vendor_id = row['vendor_id'],
            customer_id = row['customer_id']
        ).save()
    return HttpResponse(json.dumps('orders.csv was processed successfully'), content_type = 'application/json')

def fill_order_line_model(request):
    OrderLine.objects.all().delete()
    try:
        df = pd.read_csv(conf_settings.PROJECT_ROOT+'/myapp/data/order_lines.csv')
    except FileNotFoundError:
        return HttpResponse(json.dumps('order_lines.csv not found'), content_type = 'application/json')
    for index, row in df.iterrows():
        print('Processing line ' + str(index) + '...')
        OrderLine(
            order = Order.objects.get(identifier = row['order_id']),
            product_id = row['product_id'],
            product_description = row['product_description'],
            product_price = row['product_price'],
            product_vat_rate = row['product_vat_rate'],
            discount_rate = row['discount_rate'],
            quantity = row['quantity'],
            full_price_amount = row['full_price_amount'],
            discounted_amount = row['discounted_amount'],
            vat_amount = row['vat_amount'],
            total_amount = row['total_amount']
        ).save()
    return HttpResponse(json.dumps('order_lines.csv was processed successfully'), content_type = 'application/json')
