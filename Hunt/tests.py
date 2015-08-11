# import modules
from Hunt.views import Main


from django.test import TestCase
import unittest2 as utest
import mock
# Create your tests here.


class HuntTest(utest.TestCase):

    def setUp(self):
        self.request = mock.MagicMock()

    @mock.patch('Hunt.views.render_to_response')
    def test_HuntMain(self, render):
        Main(r)
        render.assert_called_with()
