from django.urls import path
from . import views

# SET THE NAMESPACE!
app_name = 'basic_app'

urlpatterns=[
    path('relative/',views.relative,name='index'),
    path('other/',views.other,name='other'),
]
