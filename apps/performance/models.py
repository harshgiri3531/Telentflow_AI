from django.db import models
from apps.employees.models import Employee
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


class Goal(models.Model):
    class GoalStatus(models.TextChoices):
        IN_PROGRESS = 'IN_PROGRESS', 'In Progress'
        COMPLETED = 'COMPLETED', 'Completed'
        MISSED = 'MISSED', 'Missed'

    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='goals')
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    due_date = models.DateField()
    status = models.CharField(max_length=20, choices=GoalStatus.choices, default=GoalStatus.IN_PROGRESS)

    def __str__(self):
        return f"{self.title} - {self.employee.employee_id}"


class PerformanceReview(models.Model):
    class Sentiment(models.TextChoices):
        POSITIVE = 'POSITIVE', 'Positive'
        NEUTRAL = 'NEUTRAL', 'Neutral'
        NEGATIVE = 'NEGATIVE', 'Negative'

    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='reviews')
    reviewer = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, related_name='reviews_given')
    rating = models.PositiveSmallIntegerField()
    feedback = models.TextField()
    sentiment = models.CharField(max_length=20, choices=Sentiment.choices, blank=True)
    sentiment_score = models.FloatField(null=True, blank=True)
    review_date = models.DateField(auto_now_add=True)

    def save(self, *args, **kwargs):
        analyzer = SentimentIntensityAnalyzer()
        scores = analyzer.polarity_scores(self.feedback)
        compound = scores['compound']
        self.sentiment_score = compound

        if compound >= 0.05:
            self.sentiment = self.Sentiment.POSITIVE
        elif compound <= -0.05:
            self.sentiment = self.Sentiment.NEGATIVE
        else:
            self.sentiment = self.Sentiment.NEUTRAL

        super().save(*args, **kwargs)

    def __str__(self):
        return f"Review for {self.employee.employee_id} by {self.reviewer}"