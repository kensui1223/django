from django.db import models
class Student(models.Model):
    student_id = models.CharField(max_length=20)
    student_name = models.CharField(max_length=100)
    student_number = models.CharField(max_length=15)
    student_email = models.EmailField()

    def __str__(self):
        return "%s " %(self.student_name)
    class Meta:
        db_table = "Student"
        