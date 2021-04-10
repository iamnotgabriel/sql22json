from setuptools import setup, find_packages

setup(
    name='sql22json',
    author='Gabriel Fr. Borges',
    author_email='gabrielfr.borges@gmail.com',
    url='https://github.com/gfborges/sql2json',
    packages=find_packages(),
    entry_points= {
        'console_scripts':{
            'sql2json = sql2json.main:main'
        }
    }
)