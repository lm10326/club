import unittest


def add(list):
    return list[0]+list[1]
class MyTestCase(unittest.TestCase):
    def test_something(self):
        global a;
        a=[23,2,5]
        # print(self.a)
    def test_son(self):
        b=add(a)
        print(b)
    def test_list(self):
        l1=['2017-09-06', '00:00:00', 0.0]
        l2=['2017-09-06', '00:00:00', 0.00]
        self.assertEqual(l1,l2)


if __name__ == '__main__':
    unittest.main()

