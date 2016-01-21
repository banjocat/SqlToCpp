
from __future__ import unicode_literals
from nose.tools import *
from sqltocpp import convert


assert_equals.__self__.maxDiff = None

def setup():
    pass

def teardown():
    pass

def test_basic():
    sql = '''
CREATE TABLE pizza (
id INTEGER PRIMARY_KEY,
topping TEXT,
cost REAL
);
'''

    expected = '''
struct pizza
{
    int id;
    std::string topping;
    double cost;
};
'''

    assert_equals(convert.table_to_struct(sql),expected)

def test_one_line():
    sql = 'CREATE TABLE pizza (id INTEGER PRIMARY_KEY, topping TEXT, cost REAL);'

    expected = '''
struct pizza
{
    int id;
    std::string topping;
    double cost;
};
'''
    
    assert_equals(convert.table_to_struct(sql),expected)

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

def test_schema_to_struct():

    convert.schema_to_struct('tests/schema1.sql')
    with open('schema.hpp', 'r') as schema:
        with open('tests/schemaTest.hpp', 'r') as test:
            assert_equals(schema.readlines(), test.readlines())


def test_table_to_sql_callback():

    sql ='''
CREATE TABLE home
(
    id INTEGER PRIMARY KEY,
    address TEXT,
    zip_code INTEGER,
    state TEXT
);
'''

    expected ='''
int sql_callback(void *pArg, int argc, char **text, char **columnName)
{
    if (!columnName)
        return -1;

    if (!text)
        return -2;

    auto * list = (std::vector<home>*) pArg;
    home temp;
    string column(columnName);
    stringstream value;
    value.str(text);

    if (column == "id")
        home.id << value;
    if (column == "address")
        home.address << value;
    if (column == "zip_code")
        home.zip_code << value;
    if (column == "state")
        home.state << value;

    return 0;
}'''

    assert_equals(convert.table_to_sql_callback(sql), expected)



                    
            
            



