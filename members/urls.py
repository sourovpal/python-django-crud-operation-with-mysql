from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('member/<int:id>', views.index, name='index_id'),
    path('member/<int:id>/update', views.update, name='update_id'),
]
