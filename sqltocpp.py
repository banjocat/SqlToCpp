import click
from sqltocpp import convert


@click.command()
@click.argument('sql_schema_file')
@click.option('--target', default='schema.hpp', help='hpp file name')
def execute(sql_schema_file, target):
    convert.schema_to_struct(sql_schema_file, target)



if __name__ == '__main__':
    execute()
