# -*- coding: utf-8 -*-
from django.test import TestCase

from cmsplugin_plain_text.models import Plaintext


class PlaintextTestCase(TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_str(self):
        Plaintext.objects.create(
            body="body value"
        )
        instance = Plaintext.objects.all()
        self.assertEqual(instance.count(), 1)
        instance = Plaintext.objects.first()
        self.assertEqual(instance.body, "body value")
        self.assertEqual(str(instance), "body value")
        self.assertEqual(instance.__unicode__(), "body value")
