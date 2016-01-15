try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'My Project',
    'author': 'Jack Muratore',
    'url': 'URL to get it at.',
    'download_url': 'Where to download it.',
    'author_email': 'My email.',
    'version': '0.1',
    'install_requires': ['nose', 'wheel'],
    'packages': ['SqlToCpp'],
    'scripts': [],
    'name': 'SqlToCpp'
}

setup(**config)
