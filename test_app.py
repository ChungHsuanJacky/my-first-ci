import unittest
from app import check_temperature

class TestEquipmentTemperature(unittest.TestCase):
    def test_normal_temp(self):
        self.assertEqual(check_temperature(50), "Status: Normal")

    def test_high_temp(self):
        self.assertEqual(check_temperature(90), "Warning: Overheating")

if __name__ == '__main__':
    unittest.main()
