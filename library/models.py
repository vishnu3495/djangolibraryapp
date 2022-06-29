from django.db import models
from django.contrib.auth.models import User,AbstractUser

class User(AbstractUser):
    options=(
        ("library","library"),
        ("student","student")
    )
    role=models.CharField(max_length=150,choices=options,default="student")
    phone=models.CharField(max_length=12,null=True)

class Books(models.Model):
    book_title=models.CharField(max_length=150)
    library=models.ForeignKey(User,on_delete=models.CASCADE,related_name="library")
    Author=models.CharField(max_length=150)
    Cover_artist=models.CharField(max_length=150)
    Subject=models.CharField(max_length=150)
    Genre=models.CharField(max_length=150)
    Publisher=models.CharField(max_length=150)
    Publication_date=models.DateField(null=True)
    Media_type=models.CharField(max_length=150)
    Pages=models.PositiveIntegerField(default=0)
    active_status = models.BooleanField(default=True)


    def __str__(self):
        return self.book_title
