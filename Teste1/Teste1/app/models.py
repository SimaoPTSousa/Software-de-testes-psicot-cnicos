from django.db import models
from django.utils import timezone
from datetime import timedelta

class question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField()
    def __str__(self):
        return self.question_text
    def is_old_question(self):
        now = timezone.now()
        return now - self.pub_date > timedelta(days=1)
    
class choice(models.Model):
    votes =  models.IntegerField(default=0)
    question = models.ForeignKey(question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    def __str__(self):
        return self.choice_text
