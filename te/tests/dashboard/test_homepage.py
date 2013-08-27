from django.core.urlresolvers import resolve
from django.http import HttpRequest
from django.template.loader import render_to_string
from django.test import TestCase
from dashboard.views import home_page


class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = home_page(request)
        ctx = {
            'js': 'index.js.html',
            'css': 'index.css.html',
        }
        expected_html = render_to_string('index.html', ctx)
        self.assertEqual(response.content.decode(), expected_html)
