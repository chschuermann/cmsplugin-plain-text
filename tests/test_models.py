# -*- coding: utf-8 -*-
from django.test import TestCase

from cmsplugin_plain_text.models import Plaintext


class PlaintextTestCase(TestCase):
    def setUp(self):
        self.plaintext_body = 'body value'

    def tearDown(self):
        pass

    def test_plaintext_instance(self):
        Plaintext.objects.create(
            body=self.plaintext_body
        )
        instance = Plaintext.objects.all()
        self.assertEqual(instance.count(), 1)
        instance = Plaintext.objects.first()
        self.assertEqual(instance.body, self.plaintext_body)
        self.assertEqual(str(instance), self.plaintext_body)
        self.assertEqual(instance.__unicode__(), self.plaintext_body)
