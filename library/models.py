from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class admin_info(models.Model):
    book_name = models.CharField(max_length=30)
    author_name = models.CharField(max_length=30)
    category = models.CharField(max_length=30)
    isbn = models.IntegerField()
    quantity = models.IntegerField()
    def __str__(self):
        return self.book_name
class student_signup(models.Model):

    user = models.OneToOneField(User, on_delete = models.CASCADE)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    department = models.CharField(max_length=30)
    roll = models.IntegerField()
    pic = models.ImageField(upload_to='pic',blank = True)
    email = models.EmailField(null=True)
    
    def __str__(self):
        return self.user.username    
    
class admin_student_connect(models.Model):

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    book_name = models.CharField(max_length=30)
    issued_date = models.DateField()
    return_date = models.DateField()
    email = models.EmailField()
    fine = models.IntegerField()
    
    def __str__(self):
        return self.first_name
    


    