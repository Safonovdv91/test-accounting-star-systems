from unittest import TestCase, main
import sys
import os

sys.path.append(os.getcwd())
print(os.getcwd())

from Model import star_system_objects


class TestUniverseObject(TestCase):
    def test_set_good_name(self):
        test_star_system = star_system_objects.UniverseObject("Solar0", 0)

        test_star_system.name = "Solar"
        self.assertEqual(test_star_system.name, "Solar")

        test_star_system.name = "Solar2"
        self.assertEqual(test_star_system.name, "Solar2")

    def test_set_name_list(self):
        test_star_system = star_system_objects.UniverseObject("Solar0", 0)

        with self.assertRaises(TypeError):
            test_star_system.name = [123, 515]

        with self.assertRaises(TypeError):
            test_star_system.name = ["wrq", "w;f2"]

    def test_set_age_good(self):
        test_star_system = star_system_objects.UniverseObject()

        test_star_system.age = 0
        self.assertEqual(test_star_system.age, 0)

        test_star_system.age = 5
        self.assertEqual(test_star_system.age, 5)

        test_star_system.age = 555.664
        self.assertEqual(test_star_system.age, 555.664)

    def test_UniObj_set_age_aboveZero(self):
        test_star_system = star_system_objects.UniverseObject()

        with self.assertRaises(AttributeError):
            test_star_system.age = -5

        with self.assertRaises(AttributeError):
            test_star_system.age = -0.5

    def test_UniObj_set_age_string(self):
        test_star_system = star_system_objects.UniverseObject()

        with self.assertRaises(TypeError):
            test_star_system.age = ""

        with self.assertRaises(TypeError):
            test_star_system.age = "sdasd"


class TestCelestialBodyDiameter(TestCase):

    def test_CelBody_receive_good(self):
        test_star_system = star_system_objects.CelestialBody()

        self.assertEqual(test_star_system.set_diameter("45"), True)
        self.assertEqual(test_star_system.set_diameter(45), True)
        self.assertEqual(test_star_system.set_diameter("0"), True)
        self.assertEqual(test_star_system.set_diameter(0), True)
        self.assertEqual(test_star_system.set_diameter("45.34"), True)
        self.assertEqual(test_star_system.set_diameter(45.34), True)
        self.assertEqual(test_star_system.set_diameter(), True)

    def test_CelBody_recieve_Char(self):
        test_star_system = star_system_objects.CelestialBody()

        self.assertEqual(test_star_system.set_diameter("swqw2"), False)
        self.assertEqual(test_star_system.set_diameter("5+5"), False)

    def test_CelBody_recieve_List(self):
        test_star_system = star_system_objects.CelestialBody()

        self.assertEqual(test_star_system.set_diameter([12, "jh"]), False)
        self.assertEqual(test_star_system.set_diameter([]), False)

    def test_CelBody_receive_AboveZero(self):
        test_star_system = star_system_objects.CelestialBody()

        self.assertEqual(test_star_system.set_diameter(-23), False)
        self.assertEqual(test_star_system.set_diameter("-23"), False)
        self.assertEqual(test_star_system.set_diameter(-0), True)
        self.assertEqual(test_star_system.set_diameter("-0"), True)
        self.assertEqual(test_star_system.set_diameter(-1.4), False)
        self.assertEqual(test_star_system.set_diameter("-1.4"), False)


class TestCelestialBodySetType(TestCase):

    def test_CelBody_receive_good(self):
        test_star_system = star_system_objects.CelestialBody()

        TYPES_OBJECTS = {"Unknown", "Star", "Worm Hole", "Blue Gigant", "Red Gigant"}

        self.assertEqual(test_star_system.set_type_object("Unknown", TYPES_OBJECTS), True)
        self.assertEqual(test_star_system.set_type_object("Worm Hole", TYPES_OBJECTS), True)
        self.assertEqual(test_star_system.set_type_object("Blue Gigant", TYPES_OBJECTS), True)

    def test_CelBody_receive_bad(self):
        test_star_system = star_system_objects.CelestialBody()

        TYPES_OBJECTS = {"Unknown", "Star", "Worm Hole", "Blue Gigant", "Red Gigant"}

        with self.assertRaises(ValueError):
            test_star_system.set_type_object("UnkUnjk", TYPES_OBJECTS)


class TestCelestialBodySetWeight(TestCase):
    """Testing set_ methods"""

    def test_CelBody_Set_good(self):
        test_obj = star_system_objects.CelestialBody()

        self.assertEqual(test_obj.set_weight(24), True)
        self.assertEqual(test_obj.set_weight(2134.12), True)
        self.assertEqual(test_obj.set_weight(0), True)
        self.assertEqual(test_obj.set_weight("24"), True)
        self.assertEqual(test_obj.set_weight("24.2412"), True)
        self.assertEqual(test_obj.set_weight("0"), True)

    def test_CelBody_Set_String(self):
        test_obj = star_system_objects.CelestialBody()

        self.assertEqual(test_obj.set_weight("sfq2"), False)
        self.assertEqual(test_obj.set_weight("@wr"), False)

    def test_CelBody_Set_Above_zero(self):
        test_obj = star_system_objects.CelestialBody()

        self.assertEqual(test_obj.set_weight(-2312), False)
        self.assertEqual(test_obj.set_weight(-2312.245), False)
        self.assertEqual(test_obj.set_weight("-2561"), False)
        self.assertEqual(test_obj.set_weight("-2561.241"), False)


if __name__ == "__main__":
    main()
