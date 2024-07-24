from django.db import models
from django.forms import ModelForm

# Create your models here.
class Course(models.Model):
    courseCode = models.CharField(max_length=10)
    courseName = models.CharField(max_length=50)
    courseCredits = models.IntegerField()
    
    def __str__(self):
        return f"{self.courseCode} {self.courseName} {self.courseCredits}"

class Student(models.Model):
    usn = models.CharField(max_length=10)
    name = models.CharField(max_length=40)
    sem = models.IntegerField()
    courses = models.ManyToManyField(Course, related_name='student_set')
    
    def __str__(self):
        return f"{self.usn} {self.name} {self.sem}"

class ProjectReg(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    ptitle = models.CharField(max_length=30)
    planguage = models.CharField(max_length=30)
    pduration = models.IntegerField()

class ProjectForm(ModelForm):
    required_css_class = "required"
    class Meta:
        model = ProjectReg
        fields = ['student', 'ptitle', 'planguage', 'pduration']
