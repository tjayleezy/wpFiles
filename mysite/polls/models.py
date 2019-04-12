from django.db import models

# Create your models here.

class academic_dept(models.Model):
    dept_code = models.CharField(max_length=10,unique=True)
    dept_name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.dept_name

class academic_class(models.Model):
    class_code = models.CharField(max_length=5, unique=True)
    dept_code = models.ForeignKey(
        'academic_dept',
        on_delete=models.CASCADE,
    )
    class_name = models.CharField(max_length=30)
    def __str__(self):
        return self.class_code

class file_manager(models.Model):
    file_alias = models.CharField(max_length=30, unique=True)
    class_code = models.ForeignKey(
        'academic_class',
        on_delete=models.CASCADE,
    )
    document = models.FileField(upload_to='documents/')
    rating = models.IntegerField(null=True)
    downloads = models.IntegerField(default=0)
    flags = models.IntegerField(default=0)
    upload_date = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.document

    


