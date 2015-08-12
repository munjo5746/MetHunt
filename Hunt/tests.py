# import modules
from Hunt.views import Main
from Hunt.views import HuntBegin


from django.test import TestCase
import unittest2 as utest
import mock
# Create your tests here.


class HuntTest(utest.TestCase):

    def setUp(self):
        self.request = mock.MagicMock()
        self.request.user = mock.MagicMock(return_value = mock.MagicMock())

    @mock.patch('Hunt.views.render_to_response')
    def test_HuntMain(self, render):
        Main(self.request)
        render.assert_called_with('HuntMain.html', {'user' : self.request.user, 'error' : None})

    @utest.expectedFailure
    @mock.patch('Hunt.views.json')
    @mock.patch('Hunt.views.HuntBeginSerializer')
    @mock.patch('Hunt.views.render_to_response')
    def test_invalidHuntPkForHuntBegin(self, render, serializer, json):
        serializer.return_value = mock.MagicMock()
        serializer.return_value.data = "data"
        json.return_value = mock.MagicMock()
        json.return_value.loads = mock.MagicMock(return_value = "loads")

        # call the function
        HuntBegin(self.request, -1)

    @mock.patch('Hunt.views.json')
    @mock.patch('Hunt.views.HuntBeginSerializer')
    @mock.patch('Hunt.views.render_to_response')
    @mock.patch('Hunt.views.Hunt')
    def test_validHuntPkReturnsRenderedPage(self, hunt,  render, serializer, json):
        serializer.return_value = mock.MagicMock()
        serializer.return_value.data = "data"
        json.return_value = mock.MagicMock()
        json.return_value.loads = mock.MagicMock(return_value = "loads")
        serializer.return_value = mock.MagicMock()
        serializer.return_value.data = "data"
        hunt.objects.get = mock.MagicMock()

        HuntBegin(self.request, 1)
        render.assert_called_with("HuntBegin.html", {'Hunt' : "data", "CurrentIndex" : 0, 'url' : "/Hunt/HuntDetail/" + str(1) + "/" + str(0)})
