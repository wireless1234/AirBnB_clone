from models.base_model import BaseModel
import unittest
from datetime import datetime


class TestBaseModel(unittest.TestCase):

    def setUp(self):
        self.myobject = BaseModel()
        self.myobject2 = BaseModel('name': "isa", 'age': 26)

    def tearDown(self):
        pass

    def test_id(self):
        self.assertTrue(len(self.myobject.id) != 0)

    def test_id_type(self):
        self.assertTrue(isinstance(self.myobject.id, str))

    def test_created_at(self):
        self.assertTrue(isinstance(self.myobject.created_at, datetime))

    def test_updated_at(self):
        self.assertTrue(isinstance(self.myobject.updated_at, datetime))

    def test_return_str(self):
        self.assertEqual(print(self.myobject),
                         print(f"[{type(self.myobject).__name__}] ({se\
                                 lf.myobject.id}) {self.myobject.__dict__}"))

    def test_save(self):
        last_save = self.myobject.updated_at
        self.myobject.save()
        self.assertNotEqual(last_save, self.myobject.updated_at)

    def test_dict_init(self):

        if __name__ == "__main__":
            unittest.main()
