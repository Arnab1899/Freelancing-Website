from django.db import models

from post_work.models import PostWork


class FindWork(models.Model):
    user = models.OneToOneField(PostWork, on_delete=models.CASCADE, db_column="User")
