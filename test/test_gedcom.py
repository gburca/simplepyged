import unittest
from gedcom import *

class Test(unittest.TestCase):
    """Unit tests for gedcom.py."""

    def setUp(self):
        self.g = Gedcom('/home/nick/code/gedrep/test/mcintyre.ged')

    def test_matches(self):
        for e in self.g.element_list():
            if e.individual():
                if e.surname_match('Merriman'):
                    self.assertEqual(e.name()[0], 'Lucy')
                if e.given_match('Archibald'):
                    self.assertEqual(e.name()[1], 'McIntyre')
                    self.assertEqual(e.birth_range_match(1810,1820), True)
                    self.assertEqual(e.birth_year_match(1819), True)
                if e.birth_year_match(1904):
                    self.assertEqual(e.name(), ('Carrie Lee', 'Horney'))
                    self.assertEqual(e.death_range_match(1970,1980), True)
                    self.assertEqual(e.death_year_match(1979), True)
                    self.assertEqual(e.death_year_match(1978), False)
                if e.marriage_year_match(1821):
                    if e.marriage_range_match(1820,1825):
                        if e.surname_match('McIntyre'):
                            self.assertEqual(e.name(), ('John M', 'McIntyre'))

    def test_criteria(self):
        criteria = "surname=McIntyre:birthrange=1820-1840:deathrange=1865-1870"
        for e in self.g.element_list():
            if e.individual():
                if e.criteria_match(criteria):
                    self.assertEqual(e.name(), ('Calvin Colin', 'McIntyre'))

        criteria = "surname=McIntyre:birth=1890:death=1953"
        for e in self.g.element_list():
            if e.individual():
                if e.criteria_match(criteria):
                    self.assertEqual(e.name(), ('Ernest R', 'McIntyre'))

        criteria = "surname=McIntyre:marriage=1821"
        for e in self.g.element_list():
            if e.individual():
                if e.criteria_match(criteria):
                    self.assertEqual(e.name(), ('John M', 'McIntyre'))

        criteria = "surname=McIntyre:marriagerange=1820-1825"
        for e in self.g.element_list():
            if e.individual():
                if e.criteria_match(criteria):
                    self.assertEqual(e.name(), ('John M', 'McIntyre'))


    def test_missing_pointer(self):
        """I don't really know what this does..."""
        for e in self.g.element_list():
            if e.value().startswith('@'):
                f = self.g.element_dict().get(e.value(),None)
                if f == None:
                    print e.value()

        for e in self.g.element_list():
            if e.pointer() == "@I99@":
                print e.name()

if __name__ == '__main__':
    unittest.main()