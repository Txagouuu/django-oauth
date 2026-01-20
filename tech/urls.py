from django.urls import path
from tech.views import index
from tech.views import members

urlpatterns = [
    path('', index, name='index'),
    path('members/', members, name='members'),

]