"""superlists URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
# from django.contrib import admin
from lists import views

urlpatterns = [
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.home_page, name='home'),
    url(r'^lists/new$', views.new_list, name='new_list'),
    url(r'^lists/(\d+)/$', views.view_list, name='view_list'),
    url(r'^lists/(\d+)/add_item$', views.add_item, name='add_item'),

    # url(r'^lists/(.+)/$', 'lists.views.view_list', name='view_list'),

    # Django has some built-in code to issue a permanent redirect (301) whenever someone asks for a URL which is
    # almost right, except for a missing slash.
    # In the above case, /lists/1/add_item/ would be a match for lists/(.+)/, with the (.+) capturing 1/add_item,
    # which is why test_redirects_to_list_view(self) throws an AssertionError: 301 != 302.
    # The reason we don't get the expected failure of 404 != 302 is because Django is trying to be helpful by
    # guessing that we actually wanted the URL with the trailing slash.

    # We can fix that by making our URL pattern explicitly capture only numerical digits by using the
    # regular expression \d instead
    # url(r'^lists/(\d+)/$', views.view_list, name='view_list'),

]
