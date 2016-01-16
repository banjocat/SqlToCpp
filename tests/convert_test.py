
from __future__ import unicode_literals
from nose.tools import *
from sqltocpp import convert

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



