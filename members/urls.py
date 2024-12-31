from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('members_table/', views.members_table, name='display_db_table'),
    path('add/', views.add, name='display_form'),
    path('add/add_record/', views.added_record, name='add_record'),
    path('delete/<int:id>', views.delete, name='delete_record'),
    path('update/<int:id>', views.update, name='update_record'),
    path('update/updaterecord/<int:id>', views.updaterecord, name='updated_record'),
    path('testing/', views.testing, name='testing'),
    path('testing1/', views.testing1, name='testing1'),
]