import datetime

from django.db import models
from django.utils import timezone
from django.db.models import UUIDField


class Poll(models.Model):
    question = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __unicode__(self):
        return self.question

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'


class Choice(models.Model):
    poll = models.ForeignKey(Poll)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField()

    def __unicode__(self):
        return self.choice_text


class Comment(models.Model):
    uuid = UUIDField(primary_key=True)
    comment = models.TextField(null=True, blank=True)

    def __unicode__(self):
        return self.comment or ''
