from django.views.generic import TemplateView,ListView
from library.models import Books
from library.forms import BookForm

class StudentHomeView(TemplateView):
    template_name = "student-home.html"

class StudentBookListView(ListView):
    model = Books
    context_object_name = "books"
    template_name = "student/booklist.html"

    def get_queryset(self):
        return self.model.objects.filter(active_status=True)