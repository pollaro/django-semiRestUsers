from __future__ import unicode_literals

from django.db import models

class Users(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    created_at = models.TimeDateField(auto_now_add=True)
