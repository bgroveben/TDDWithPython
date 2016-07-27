from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Ben has heard about a tutorial that uses an online to-do app (Yay! Time to build stuff!)
        # Ben goes to check out the homepage of the to-do list app.
        self.browser.get('http://localhost:8000')

        # He notices that the page title and header mention a to-do list
        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the test!')

        # Ben sees that he is invited to enter an item on the list right away, and he gets excited.

        # He types "Start building to-do app" into a text box.

        # When Ben hits enter, the page updates, and now the page lists
        # "1: Start building to-do app" as an item in the to-do list.

        # There is still a text box inviting, daring, coercing Ben to add another item.
        # He enters "Write a bunch of tests for the to-do list app".

        # The page updates again, and now shows both items on the list.

        # Ben wonders if the site will remember his list.
        # Then he sees that the site has generated a unique URL for him -- there is some text that explains it.

        # Ben visits that URL - his to-do-list is still there.

        # Satisfied, Ben can finally go to sleep for the night.
if __name__ == '__main__':
    unittest.main()
