from django.db import models


class Matches(models.Model):
    match_id = models.PositiveIntegerField(primary_key=True, null=False, unique=True)
    date = models.DateField()
