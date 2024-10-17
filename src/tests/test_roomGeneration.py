import unittest
from roomGeneration import generate_rooms

class TestRoomGeneration(unittest.TestCase):
    def test_room_generation_error1(self):
        try:
            generate_rooms(1,6,6,1)[0]
            assert False
        except ValueError:
            assert True
    def test_room_generation_error2(self):
        try:
            generate_rooms(2,30,30,2)[0]
            assert True
        except ValueError:
            assert False
    def test_room_generation1(self):
        result = len(generate_rooms(20,100,100,2)[0])
        expected = 20
        self.assertEqual(expected,result)

    def test_room_generation2(self):
        result = len(generate_rooms(3,500,500,32)[0])
        expected = 3
        self.assertEqual(expected,result)

if __name__ == "__main__":
    unittest.main()
