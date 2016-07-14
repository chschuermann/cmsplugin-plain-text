# -*- coding: utf-8 -*-
from cms.models import CMSPlugin
from django.db import models
from django.utils.translation import ugettext_lazy as _


class Plaintext(CMSPlugin):
    body = models.TextField(_('Plaintext'))

    def __unicode__(self):
        return self.body

    def __str__(self):
        return self.body
