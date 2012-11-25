import os
from distutils.core import setup


CURRENT_DIR = os.path.abspath(os.path.dirname(__file__))
README_FILEPATH = os.path.join(CURRENT_DIR, 'README.rst')


setup(
    name='django-stored-filters',
    version='0.1.1',
    packages=[
        'stored_filters',
        'stored_filters.tests',
        'stored_filters.migrations'
    ],
    author='Kirill Sibirev',
    author_email='k.sibirev@gmail.com',
    url='https://github.com/l0kix2/django-stored_filters',
    description='Django model filters, stored in json',
    long_description=open(README_FILEPATH).read(),
    keywords=['django', 'filters', 'queryset', 'json'],
    license='MIT',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Programming Language :: Python',
        'Intended Audience :: Developers',
        'Development Status :: 4 - Beta',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: MIT License',
    ],
)
