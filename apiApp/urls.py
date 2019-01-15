from django.urls import path
from .views import ContactList,ContactCreate,ContactUpdate,ContactDelete

urlpatterns = [
    path('',ContactList.as_view()),
    path('create' ,ContactCreate.as_view()),
    path('update/<int:pk>' ,ContactUpdate.as_view()),
    path('delete/<int:pk>' ,ContactDelete.as_view()),

]
