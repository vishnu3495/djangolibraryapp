from django.urls import path
from library import views

urlpatterns = [
    path("home",views.LibraryHomeView.as_view(),name="lib-home"),
    path("books/add",views.AddLibraryBooksView.as_view(),name="lib-addbook"),
    path("books/list",views.ListBookView.as_view(),name="lib-booklist"),
    path("books/detail/<int:id>",views.BookDetailView.as_view(),name="lib-bookdetail"),
    path("books/edit/<int:id>",views.BookEditView.as_view(),name="lib-bookedit"),
    path("book/delete/<int:id>",views.BookDeleteView.as_view(),name="lib-bookdelete"),
    path("users/account/signup",views.SignupView.as_view(),name="signup"),
    path("users/account/signin",views.SignInView.as_view(),name="signin"),
    path("users/accounts/signout",views.signout_view,name="signout"),
]