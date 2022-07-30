import unittest

from ..fake import fake


class BaseTestCase(unittest.TestCase):
    fake = fake
