from unittest import TestCase
import sys, os

sys.path.append(os.getcwd())
print(os.getcwd())

from Model import star_system_objects
class Test_UniverseObject(TestCase):
    def test_UniObj_good_name(self):
        test_star_system = star_system_objects.Universe_object()

        self.assertEqual(test_star_system.set_name("Solar"), True)
        self.assertEqual(test_star_system.set_name("1234"), True)
        self.assertEqual(test_star_system.set_name("sjd23"), True)

    def test_UniObj_recieveName_List(self):
        test_star_system = star_system_objects.Universe_object()

        self.assertEqual(test_star_system.set_name([12, "jh"]), False)
        self.assertEqual(test_star_system.set_name([]), False)

    def test_UniObj_recieveAge_good(self):
        test_star_system = star_system_objects.Universe_object()

        self.assertEqual(test_star_system.set_age(0), True)
        self.assertEqual(test_star_system.set_age("0"), True)
        self.assertEqual(test_star_system.set_age(5), True)
        self.assertEqual(test_star_system.set_age("5"), True)
        self.assertEqual(test_star_system.set_age(45.5), True)
        self.assertEqual(test_star_system.set_age("45.5"), True)

    def test_UniObj_recieveAge_aboveZero(self):
        test_star_system = star_system_objects.Universe_object()

        self.assertEqual(test_star_system.set_age(-1), False)
        self.assertEqual(test_star_system.set_age(-0.5), False)
        self.assertEqual(test_star_system.set_age(-1.5), False)

    def test_UniObj_recieveAge_string(self):
        test_star_system = star_system_objects.Universe_object()

        self.assertEqual(test_star_system.set_age(''), False)
        self.assertEqual(test_star_system.set_age('asd'), False)
        self.assertEqual(test_star_system.set_age('23ds'), False)
        self.assertEqual(test_star_system.set_age('@#$'), False)

