try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Sql To Cpp Bridge',
    'author': 'Jack Muratore',
    'url': 'URL to get it at.',
    'download_url': 'https://github.com/banjocat/SqlToCpp',
    'author_email': 'jackmuratore@gmail.com',
    'version': '0.1',
    'install_requires': ['nose', 'wheel'],
    'packages': ['sqltocpp', 'Jinja2', 'MarkupSafe', 'nose', 'wheel', 'click']
    'scripts': [],
    'name': 'SqlToCpp'
}

setup(**config)
