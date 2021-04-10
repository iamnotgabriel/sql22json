import unittest
from  sql22json.main import sql2json

from typing import Dict

class TestSql2Json(unittest.TestCase):

    def assertResult(self, stmt: str, expected: Dict[str,str]):
        self.assertEqual(sql2json(stmt), expected)

    def test_one_column(self):
        stmt = "insert into table( column ) values(1)"
        expected = {
            'column': '1'
        }
        self.assertResult(stmt, expected)

    def test_many_columns(self):
        stmt = "insert into person( id, name, type, salary ) values (1, 'Obi Wan', 'Jedi', 1.12)"
        expected = {
            'id': '1',
            'name': "'Obi Wan'",
            'type': "'Jedi'",
            'salary':'1.12'
        }
        self.assertResult(stmt, expected)
    
    def test_function_value(self):
        stmt = "insert into event( id, date ) values (1, curdate('now'))"
        expected = {
            'id': '1',
            'date': "curdate('now')",
        }
        self.assertResult(stmt, expected)
    
        

if __name__ == "__main__":
    unittest.main()