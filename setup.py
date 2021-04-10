from setuptools import setup, find_packages

setup(
    name='sql22json',
    version='0.1.0',
    license='MIT',
    author='Gabriel Fr. Borges',
    author_email='gabrielfr.borges@gmail.com',
    url='https://github.com/gfborges/sql22json',
    download_url = 'https://github.com/gfborges/sql22json/releases/download/0.1.0/sql22json-0.1.0.tar.gz',
    packages=find_packages(),
    entry_points= {
        'console_scripts':{
            'sql22json = sql22json.main:main'
        }
    }
)