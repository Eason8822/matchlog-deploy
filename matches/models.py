from django.db import models
from django.contrib.auth.models import User

class Match(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="matches")
    date = models.DateField("日期")
    team = models.CharField("隊名", max_length=50)
    opponent = models.CharField("對手", max_length=50)
    score_for = models.PositiveIntegerField("我方得分")
    score_against = models.PositiveIntegerField("對方得分")
    note = models.TextField("備註", blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def result(self):
        if self.score_for > self.score_against:
            return "勝"
        if self.score_for < self.score_against:
            return "敗"
        return "和"

    def __str__(self):
        return f"{self.date} {self.team} vs {self.opponent} {self.score_for}:{self.score_against} ({self.result})"

# Create your models here.
