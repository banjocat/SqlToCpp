from nose.tools import *
import sqltocpp

def setup():
    pass

def teardown():
    pass

def test_basic():
    sql = '''
    CREATE TABLE pizza (
    id PRIMARY_KEY,
    topping TEXT,
    cost REAL
    );
    '''

    expected = '''
    struct pizza
    {
        PRIMARY_KEY id,
        std::string topping;
        double cost;
    };
    '''

    assert sqltocpp.table_to_struct(sql) == expected

def test_one_line():
    sql = 'CREATE TABLE pizza (id PRIMARY_KEY, topping TEXT, cost REAL);'

    expected = '''
    struct pizza
    {
        PRIMARY_KEY id,
        std::string topping;
        double cost;
    };
    '''
    
    assert sqltocpp.table_to_struct(sql) == expected


