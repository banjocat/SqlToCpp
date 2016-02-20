
from __future__ import unicode_literals
from nose.tools import *
from sqltocpp import convert


assert_equals.__self__.maxDiff = None

def setup():
    pass

def teardown():
    pass


def test_map_tablename_to_sql():

    with open('tests/schema1.sql', 'r') as fi:
        sql = fi.read()

    expected = [
            {'tablename': 'people', 'sql':
'''CREATE TABLE people
(
    id INTEGER PRIMARY KEY,
    first_name TEXT,
    last_name TEXT,
    age INTEGER,
    home INTEGER,

    FOREIGN KEY(home) REFERENCES home(id)
);'''
            },
            {'tablename': 'cats', 'sql':
'''CREATE TABLE cats
(
    id INTEGER PRIMARY KEY,
    first_name TEXT,
    owner INTEGER NOT NULL,
    color TEXT,

    FOREIGN KEY(owner) REFERENCES people(id)
);'''
            },
            {'tablename': 'home', 'sql':
'''CREATE TABLE home
(
    id INTEGER PRIMARY KEY,
    address TEXT,
    zip_code INTEGER,
    state INTEGER,

    FOREIGN KEY(state) REFERENCES state(id)
);'''},
            {'tablename': 'state', 'sql':
'''CREATE TABLE state
(
    id INTEGER PRIMARY KEY,
    name TEXT
);'''}
            ]

    assert_equals(convert.map_tablename_to_sql(sql), expected)


def test_write_hpp_file():

    convert.write_hpp_file('fun_db', 'tests/schema1.sql', 'templates/template.hpp')
    with open('schema.hpp', 'r') as schema:
        with open('tests/schemaTest.hpp', 'r') as test:
            assert_equals(schema.readlines(), test.readlines())




                    
            
            



