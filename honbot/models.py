from django.db import models


class Matches(models.Model):
    match_id = models.PositiveIntegerField(primary_key=True, null=False, unique=True)
    date = models.DateTimeField()
    replay_url = models.URLField(max_length=120, default="")
    realtime = models.CharField(max_length=10, default="")
    mode = models.CharField(max_length=10, default="")
    _map = models.CharField(max_length=10, default="")
    major = models.PositiveSmallIntegerField(default=0)
    minor = models.PositiveSmallIntegerField(default=0)
    revision = models.PositiveSmallIntegerField(default=0)
    build = models.PositiveSmallIntegerField(default=0)

