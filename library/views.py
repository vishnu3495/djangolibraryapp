from django.shortcuts import render,redirect
from django.views.generic import TemplateView,CreateView,ListView,DetailView,UpdateView,DeleteView,FormView
from django.urls import reverse_lazy
from library.forms import BookForm,SignUpForm,LoginForm
from library.models import Books
from django.contrib.auth import authenticate,login,logout

class LibraryHomeView(TemplateView):
    template_name = "lib-home.html"

class AddLibraryBooksView(CreateView):
    model = Books
    form_class = BookForm
    template_name = "lib-addbook.html"
    success_url = reverse_lazy("lib-booklist")

    def form_valid(self, form):
        form.instance.library=self.request.user
        return super().form_valid(form)

class ListBookView(ListView):
    model = Books
    context_object_name = "books"
    template_name = "lib-listbook.html"

    def get_queryset(self):
        return Books.objects.filter(library=self.request.user)

class BookDetailView(DetailView):
    model = Books
    context_object_name = "book"
    template_name = "lib-bookdetail.html"
    pk_url_kwarg = "id"

class BookEditView(UpdateView):
    model = Books
    form_class = BookForm
    template_name = "lib-edit.html"
    success_url = reverse_lazy("lib-booklist")
    pk_url_kwarg = "id"

class BookDeleteView(DeleteView):
    model = Books
    template_name = "lib-confirmdelete.html"
    success_url = reverse_lazy("lib-booklist")
    pk_url_kwarg = "id"

class SignupView(CreateView):
    model = Books
    form_class = SignUpForm
    template_name = "usersignup.html"
    success_url = reverse_lazy("signin")

class SignInView(FormView):
    form_class = LoginForm
    template_name = "login.html"

    def post(self, request, *args, **kwargs):
        form=LoginForm(request.POST)
        if form.is_valid():
            uname=form.cleaned_data.get("username")
            pwd=form.cleaned_data.get("password")
            user=authenticate(request,username=uname,password=pwd)
            if user:
                login(request, user)
                if request.user.role=="library":
                    return redirect("lib-home")
                elif request.user.role=="student":
                    return redirect("student-home")
                else:
                    return redirect(request,"login.html",{"form":form})

def signout_view(request,*args,**kwargs):
    logout(request)
    return redirect("signin")


