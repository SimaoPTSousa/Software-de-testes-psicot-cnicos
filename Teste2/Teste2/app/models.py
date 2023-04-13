from django.db import models
from django.contrib.auth.models import User

class School(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=300)
    contact_number = models.CharField(max_length=15)

    def str(self):
        return self.name

class Student(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    sex = models.CharField(max_length=1, choices=[("M", "Masculino"), ("F", "Feminino")])
    year = models.PositiveSmallIntegerField()

    def str(self):
        return f"{self.first_name} {self.last_name}"

class Test(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()

    def str(self):
        return self.name

class Question(models.Model):
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    text = models.CharField(max_length=500)

    def str(self):
        return self.text

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.CharField(max_length=500)
    is_correct = models.BooleanField(default=False)

    def str(self):
        return self.text

class TestResult(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    score = models.IntegerField()
    total_questions = models.IntegerField()
    date_taken = models.DateTimeField(auto_now_add=True)

    def str(self):
        return f"{self.student} - {self.test} - {self.score}/{self.total_questions}"