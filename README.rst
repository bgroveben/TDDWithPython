===================================
Test-Driven Development with Python
===================================
:Author:
    Harry J.W. Percival
**Thanks Harry!**

The code for this book can be found at http://www.obeythetestinggoat.com/pages/book.html#toc

I am currently at http://www.obeythetestinggoat.com/book/chapter_19.html#_listen_to_your_tests_ugly_tests_signal_a_need_to_refactor


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
