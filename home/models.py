# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Asset(models.Model):

    #__Asset_FIELDS__
    name = models.CharField(max_length=255, null=True, blank=True)
    group = models.ForeignKey(assetgroup, on_delete=models.CASCADE)

    #__Asset_FIELDS__END

    class Meta:
        verbose_name        = _("Asset")
        verbose_name_plural = _("Asset")


class Assetgroup(models.Model):

    #__Assetgroup_FIELDS__
    name = models.CharField(max_length=255, null=True, blank=True)

    #__Assetgroup_FIELDS__END

    class Meta:
        verbose_name        = _("Assetgroup")
        verbose_name_plural = _("Assetgroup")


class Request(models.Model):

    #__Request_FIELDS__
    description = models.CharField(max_length=255, null=True, blank=True)
    start_date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    end_date = models.DateTimeField(blank=True, null=True, default=timezone.now)

    #__Request_FIELDS__END

    class Meta:
        verbose_name        = _("Request")
        verbose_name_plural = _("Request")


class Checkout(models.Model):

    #__Checkout_FIELDS__
    request_id = models.ForeignKey(request, on_delete=models.CASCADE)
    date = models.DateTimeField(blank=True, null=True, default=timezone.now)

    #__Checkout_FIELDS__END

    class Meta:
        verbose_name        = _("Checkout")
        verbose_name_plural = _("Checkout")



#__MODELS__END
