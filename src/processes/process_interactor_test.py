import unittest

import mongomock
from mongoengine import connect, disconnect


class TestStringMethods(unittest.TestCase):
    @classmethod
    def setUpClass(cls):

        connect('mongoenginetest', host='mongomock://localhost')

    @classmethod
    def tearDownClass(cls):
        disconnect()

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

    def test_increase_votes(self):
        collection = mongomock.MongoClient().db.collection
        objects = [dict(votes=1), dict(votes=2)]
        for obj in objects:
            obj['_id'] = collection.insert_one(obj).inserted_id
        increase_votes(collection)
        for obj in objects:
            stored_obj = collection.find_one({'_id': obj['_id']})
            stored_obj['votes'] -= 1
            assert stored_obj == obj  # by comparing all fields we make sure only votes changed


def increase_votes(collection):
    collection.update_many({}, {'$inc': {'votes': 1}})
