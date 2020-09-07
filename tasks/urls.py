from django.urls import path
from tasks import views 

urlpatterns = [
    path('',views.home, name="list"),
    path('update/<str:pk>/',views.UpdateTask, name="update"),
    path('delete/<str:pk>/',views.delete, name="delete"),
]
