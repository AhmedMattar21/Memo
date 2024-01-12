from django.db import models

class notes(models.Model):
    title = models.CharField(max_length=50)
    text = models.TextField()
    time = models.DateTimeField(auto_now_add=True)
  # user = models.ForeignKey(user)

    def __str__(self) -> str:
        return self.title
    

