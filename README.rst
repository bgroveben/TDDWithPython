===================================
Test-Driven Development with Python
===================================
:Author:
    Harry J.W. Percival
**Thanks Harry!**

The code for this book can be found at http://www.obeythetestinggoat.com/pages/book.html#toc

I am currently at http://www.obeythetestinggoat.com/book/chapter_11.html#_using_the_form_in_our_views


**When a new version of Firefox breaks Selenium:**

In the server::

    ~/sites/$SITENAME/source => sudo apt-get install xvfb
    ~/sites/$SITENAME/source => ../virtualenv/bin/pip3 install pyvirtualdisplay

/functional_tests/base.py::

    from django.contrib.staticfiles.testing import StaticLiveServerTestCase
    from pyvirtualdisplay import Display
    from selenium import webdriver
    import sys

    display = Display(visible=0, size=(1024, 768))
    display.start()

    class FunctionalTest(StaticLiveServerTestCase):
    [...]
