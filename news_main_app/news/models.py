from django.db import models

class News(models.Model):
  title = models.CharField(max_length=150)
  news_text = models.TextField()
  author = models.CharField(max_length=50)
  publish_date = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.title

  class Meta:
    ordering = ['-publish_date']

  
