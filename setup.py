"""A setuptools based setup module.

See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
"""

# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

# Arguments marked as "Required" below must be included for upload to PyPI.
# Fields marked as "Optional" may be commented out.

setup(
    name='auth',  # Required
    version='0.1',  # Required
    description='A simple authentication system',  # Required
    long_description=long_description,  # Optional
    long_description_content_type='text/markdown',  # Optional (see note above)
    url='https://github.com/BCCN-Prog/2018_day5',  # Optional
    author='(almost) BCCN Master Students',  # Optional
    author_email='nospam',  # Optional
    classifiers=[  # Optional
        'Programming Language :: Python :: 3',
    ],

    packages=find_packages(),  # Required
    install_requires=['numpy'],  # Optional
    #package_data={  # Optional
    #    'sample': ['package_data.dat'],
    #},

    #data_files=[('my_data', ['data/data_file'])],  # Optional

    #entry_points={  # Optional
    #    'console_scripts': [
    #        'auth=auth:get_credentials',
    #    ],
    #},
)
