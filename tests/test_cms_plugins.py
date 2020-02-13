#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import warnings

from django.conf import settings
from cms.api import add_plugin
from cms.models import Placeholder
from cms.plugin_rendering import ContentRenderer
from django.test import TestCase
from django.test.client import RequestFactory

from cmsplugin_plain_text.cms_plugins import PlaintextPlugin


class CmsPluginPlainTextTestCase(TestCase):

    def setUp(self):
        self.plaintext_body = 'Plaintext'
        self.language = settings.LANGUAGES[0][0]

    def test_plugin_context(self):
        placeholder = Placeholder.objects.create(slot='content')
        model_instance = add_plugin(
            placeholder,
            PlaintextPlugin,
            self.language,
            body=self.plaintext_body,
        )
        plugin_instance = model_instance.get_plugin_class_instance()
        context = plugin_instance.render({}, model_instance, None)
        self.assertIn('body', context)
        self.assertEqual(context['body'], self.plaintext_body)

    def test_plugin_html(self):
        placeholder = Placeholder.objects.create(slot='content')
        model_instance = add_plugin(
            placeholder,
            PlaintextPlugin,
            self.language,
            body=self.plaintext_body,
        )
        renderer = ContentRenderer(request=RequestFactory())
        html = renderer.render_plugin(model_instance, {})
        self.assertEqual(html, self.plaintext_body)
