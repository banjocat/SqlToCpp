import click
from sqltocpp import convert


@click.command()
@click.option('--sql', help='schema file name')
@click.option('--target', default='schema.hpp', help='hpp file name')
def execute(sql, target):
    convert.schema_to_struct(sql, target)



if __name__ == '__main__':
    try:
        execute()
    except:
        execute("--help")
