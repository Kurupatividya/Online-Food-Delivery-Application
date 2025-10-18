from django.urls import path
from .views import Home,AddEmployee,DeleteEmployee,EditEmployee,FirstPage,FeedBack
urlpatterns = [
    path('',FirstPage.as_view(),name='firstpage'),
    path('feedback',FeedBack.as_view(),name='feedback'),
    path('Home/',Home.as_view(),name = 'home'),
    path('AddEmployee/',AddEmployee.as_view(),name='AddEmployee'),
    path('DeleteEmployee/',DeleteEmployee.as_view(),name = 'DeleteEmployee'),
    path('EditEmployee/<int:id>/',EditEmployee.as_view(),name = 'EditEmployee')
]