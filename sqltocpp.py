import click
from sqltocpp import convert


@click.command()
@click.argument('sql_schema_file')
@click.option('--target', default='schema.hpp', help='hpp file name')
@click.option('--database_name', default='db', help='db namepsace')
def execute(sql_schema_file, target):
    convert.write_hpp_file(sql_schema_file, target)

if __name__ == '__main__':
    execute()
