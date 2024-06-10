from django.urls import path
from .views import todo_list
from . import views

app_name="todoapp"
urlpatterns=[
        path('',todo_list,name="all"),
        path('create/',views.TodoappCreateView.as_view(),name='todoapp_create'),
        path("update/<int:todo_id>/",views.TodoappUpdateView.as_view(),name="todoapp_update"),
        path("delete/<int:todo_id>/",views.TodoappDeleteView.as_view(),name="todoapp_delete"),
        path('search/', views.TodoappSearchView.as_view(), name='todoapp_search'),

    ]