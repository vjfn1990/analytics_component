from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('generate_report', views.generate_report, name = 'generate_report'),
    path('fill_order_model', views.fill_order_model, name = 'fill_order_model'),
    path('fill_order_line_model', views.fill_order_line_model, name = 'fill_order_line_model'),
]
