from django.urls import path
from student import views

urlpatterns=[
    path("home",views.StudentHomeView.as_view(),name="student-home"),
    path("books/all",views.StudentBookListView.as_view(),name="student-booklist"),
]