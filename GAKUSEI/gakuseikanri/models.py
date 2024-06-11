from django.db import models

class Student(models.Model):
    student_id = models.CharField(max_length=20, primary_key=True)
    name = models.CharField(max_length=100)
    number = models.CharField(max_length=15)
    email = models.EmailField()

    def __str__(self):
        return self.name
    class Meta:  
        db_table = "Student" 
 

