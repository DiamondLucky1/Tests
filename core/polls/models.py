from django.db import models

from core.core import settings


class Question(models.Model):
    title = models.CharField(max_length=4000)
    visible = models.BooleanField(default=False)
    max_points = models.FloatField()

    def __str__(self):
        return self.title

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=4000)
    point = models.FloatField()
    lock_other = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class Answer(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING)
    question = models.ForeignKey(Question, on_delete=models.DO_NOTHING)
    choice = models.ForeignKey(Choice, on_delete=models.DO_NOTHING)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.choice.title