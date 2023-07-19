from unittest import TestCase, main
import sys
import os

sys.path.append(os.getcwd())
print(os.getcwd())

from Model.star_system_objects import UniverseObject, CelestialBody


class TestUniverseObject(TestCase):
    def test_set_good_name(self):
        test_star_system = UniverseObject("Solar0", 0)

        test_star_system.name = "Solar"
        self.assertEqual(test_star_system.name, "Solar")

        test_star_system.name = "Solar2"
        self.assertEqual(test_star_system.name, "Solar2")

    def test_set_name_list(self):
        test_star_system = UniverseObject("Solar0", 0)

        with self.assertRaises(TypeError):
            test_star_system.name = [123, 515]

        with self.assertRaises(TypeError):
            test_star_system.name = ["wrq", "w;f2"]

    def test_set_age_good(self):
        test_star_system = UniverseObject()

        test_star_system.age = 0
        self.assertEqual(test_star_system.age, 0)

        test_star_system.age = 5
        self.assertEqual(test_star_system.age, 5)

        test_star_system.age = 555.664
        self.assertEqual(test_star_system.age, 555.664)

    def test_UniObj_set_age_aboveZero(self):
        test_star_system = UniverseObject()

        with self.assertRaises(AttributeError):
            test_star_system.age = -5

        with self.assertRaises(AttributeError):
            test_star_system.age = -0.5

    def test_UniObj_set_age_string(self):
        test_star_system = UniverseObject()

        with self.assertRaises(TypeError):
            test_star_system.age = ""

        with self.assertRaises(TypeError):
            test_star_system.age = "sdasd"


class TestCelestialBodyDiameter(TestCase):

    def test_CelBody_receive_good(self):
        test_star_system = CelestialBody(12, 12, "star")

        self.assertEqual(test_star_system.diameter, 12)
        test_star_system.diameter = "0"

        self.assertEqual(test_star_system.diameter, 0)

        test_star_system.diameter = "45.34"
        self.assertEqual(test_star_system.diameter, 45.34)

        test_star_system.diameter = 4512412412412412412412412414.34
        self.assertEqual(test_star_system.diameter, 4512412412412412412412412414.34)

    def test_CelBody_recieve_Char(self):
        test_star_system = CelestialBody(12, 12, "star")

        self.assertEqual(test_star_system.diameter("swqw2"), False)
        self.assertEqual(test_star_system.diameter("5+5"), False)

    def test_CelBody_recieve_List(self):
        test_star_system = CelestialBody(12, 12, "star")

        self.assertEqual(test_star_system.diameter([12, "jh"]), False)
        self.assertEqual(test_star_system.diameter([]), False)

    # def test_CelBody_receive_AboveZero(self):
    #     test_star_system = CelestialBody(12, 12, "gg")
    #
    #     self.assertEqual(test_star_system.(-23), False)
    #     self.assertEqual(test_star_system.("-23"), False)
    #     self.assertEqual(test_star_system.(-0), True)
    #     self.assertEqual(test_star_system.("-0"), True)
    #     self.assertEqual(test_star_system.(-1.4), False)
    #     self.assertEqual(test_star_system.("-1.4"), False)

    # class TestCelestialBodySetType(TestCase):

    def test_CelBody_receive_g2ood(self):
        test_star_system = CelestialBody(12, 12, "star")

        TYPES_OBJECTS = {"Unknown", "Star", "Worm Hole", "Blue Gigant", "Red Gigant"}

        self.assertEqual(test_star_system.set_type_object("Unknown", TYPES_OBJECTS), True)
        self.assertEqual(test_star_system.set_type_object("Worm Hole", TYPES_OBJECTS), True)
        self.assertEqual(test_star_system.set_type_object("Blue Gigant", TYPES_OBJECTS), True)

    def test_CelBody_receive_bad(self):
        test_star_system = CelestialBody(12, 12, "star")

        TYPES_OBJECTS = {"Unknown", "Star", "Worm Hole", "Blue Gigant", "Red Gigant"}

        with self.assertRaises(ValueError):
            test_star_system.set_type_object("UnkUnjk", TYPES_OBJECTS)


# class TestCelestialBodySetWeight(TestCase):
#     """Testing set_ methods"""
#
#     def test_CelBody_Set_good(self):
#         test_obj = CelestialBody(12, 12, "gg")
#
#         self.assertEqual(test_obj.set_weight(24), True)
#         self.assertEqual(test_obj.set_weight(2134.12), True)
#         self.assertEqual(test_obj.set_weight(0), True)
#         self.assertEqual(test_obj.set_weight("24"), True)
#         self.assertEqual(test_obj.set_weight("24.2412"), True)
#         self.assertEqual(test_obj.set_weight("0"), True)
#
#     def test_CelBody_Set_String(self):
#         test_obj = CelestialBody(12, 12, "gg")
#
#         self.assertEqual(test_obj.set_weight("sfq2"), False)
#         self.assertEqual(test_obj.set_weight("@wr"), False)
#
#     def test_CelBody_Set_Above_zero(self):
#         test_obj = CelestialBody(12, 12, "gg")
#
#         self.assertEqual(test_obj.set_weight(-2312), False)
#         self.assertEqual(test_obj.set_weight(-2312.245), False)
#         self.assertEqual(test_obj.set_weight("-2561"), False)
#         self.assertEqual(test_obj.set_weight("-2561.241"), False)


if __name__ == "__main__":
    main()
