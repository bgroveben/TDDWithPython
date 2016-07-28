from django.test import TestCase

from django.core.urlresolvers import resolve
from lists.views import home_page  # Which we haven't built yet -- tests first

class HomePageTest(TestCase):

    # Can we resolve the URL for the root of the site ('/') to a particular view function we have made?
    def test_root_url_resolvers_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)
