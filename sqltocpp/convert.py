from __future__ import unicode_literals
import re
import jinja2



def table_to_struct(sql):
    """
    Takes a SQL table schema defined as a text
    and returns a text of a C structure to represent it
    """

    #mapping SQL names to C types
    sql_to_ctype = {
            'INTEGER': 'int',
            'REAL': 'double',
            'TEXT': 'std::string',
            'BLOB': 'std::string'
            }

    # Setup jinja to not insert excess newlines
    j2 = jinja2.Environment(trim_blocks=True, lstrip_blocks=True)
    struct = j2.from_string('''
    struct {{ name }}
    {
        {% for member in members %}
        {{member.c_type}} {{ member.name }};
        {% endfor %}
    };
    ''')

    #get table name
    match_tablename = re.match('\s*CREATE TABLE\s+(\S+)', sql, re.MULTILINE)
    if match_tablename == None:
        raise Exception('No CREATE TABLE found in string:', sql)

    tablename = match_tablename.group(1)

    #loop through each definnition
    #convert SQL definition to struct
    regex_column = r'\s*\(?(\S+)\s+((?:INTEGER)|(?:REAL)|(?:TEXT)|(?:BLOB))'
    members = []
    for (name, sql_type) in re.findall(regex_column, sql, re.IGNORECASE):
        c_type = sql_to_ctype[sql_type.upper()]
        members.append({'name': name, 'c_type': c_type})

    return struct.render({'name': tablename, 'members': members})


def map_tablename_to_sql(sql):
    """
    Returns an array of dictionaries that map each tablename to its sql
    """
    regex = r'(CREATE TABLE\s+(\S+)\s+[^;]+;)'

    tables_with_sql = []
    for (sql, tablename) in re.findall(regex, sql):
        tables_with_sql.append({
            'tablename': tablename,
            'sql': sql
            })

    print(tables_with_sql)
    return tables_with_sql



