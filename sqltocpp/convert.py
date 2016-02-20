from __future__ import unicode_literals
import re
import jinja2
import os



def _sql_to_dict(sql):
    """
    Returns a dict with name and members of a create table sql statement
    """

    # mapping SQL names to CPP types
    sql_to_ctype = {
            'INTEGER': 'int',
            'REAL': 'double',
            'TEXT': 'std::string',
            'BLOB': 'std::string'
            }

    # get table name
    match_tablename = re.match('\s*CREATE TABLE\s+(\S+)', sql, re.MULTILINE)
    if match_tablename is None:
        raise Exception('No CREATE TABLE found in string:', sql)

    tablename = match_tablename.group(1)

    # loop through each definnition
    # convert SQL definition to struct
    regex_column = r'\s*\(?(\S+)\s+((?:INTEGER)|(?:REAL)|(?:TEXT)|(?:BLOB))'
    members = []
    for (name, sql_type) in re.findall(regex_column, sql, re.IGNORECASE):
        c_type = sql_to_ctype[sql_type.upper()]
        members.append({'name': name, 'c_type': c_type})

    return {'name': tablename, 'members': members}


def map_tablename_to_sql(sql):
    """
    Returns an array of dictionaries that map each tablename to its sql
    """
    regex = r'(CREATE TABLE\s+(\S+)\s+[^;]+;)'

    tables_with_sql = []
    for (sql, tablename) in re.findall(regex, sql, re.MULTILINE):
        tables_with_sql.append({
            'tablename': tablename,
            'sql': sql
            })

    return tables_with_sql


def create_dict_for_template(schema, database_name):
    """
    Creates a dict that will be inserted into the template
    dict = {
        database_name: "name",
        tables: [
           {
            name: "tablename"
            members: [
                {
                    name: 'col1',
                    c_type: 'int'}
                },
                {
                    name: 'col2',
                    c_type: 'std::string'}
                },
            ]
        ]
    }
    """
    schema_dict = {}
    schema_dict["database_name"] = database_name
    schema_dict["tables"] = []
    tablename_list = map_tablename_to_sql(schema)
    for table in tablename_list:
        table_dict = _sql_to_dict(table["sql"])
        table_dict["name"] = table["tablename"]
        schema_dict["tables"].append(table_dict)
        
    return schema_dict

def schema_to_template_dict(schema, template, db_name):
    """
    Takes the schema and template as strings and returns
    the rendered template
    """
    schema_dict = create_dict_for_template(schema, db_name)
    j2 = jinja2.Environment(trim_blocks=True, lstrip_blocks=True)
    cpp_template = j2.from_string(template)
    return cpp_template.render(schema_dict)


def write_hpp_file(db_name, schema_file, template_file, location='schema.hpp'):
    """
    This is the main function that does the full conversion
    from schema.sql to resulting template
    """
    
    with open(schema_file, 'r') as f:
        schema = f.read()

    with open(template_file, 'r') as f:
        template = f.read()

    result = schema_to_template_dict(schema, template, db_name)
            
    try:
        os.remove(location)
    except OSError:
        pass

    with open(location, 'w') as header:
        header.write(result)
    
