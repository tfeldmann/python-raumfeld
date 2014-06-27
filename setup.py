import os
from distutils.core import setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as f:
    readme = f.read()

setup(
    name='raumfeld',
    packages=['raumfeld'],
    version=__import__('raumfeld').__version__,
    install_requires=['pysimplesoap'],
    license='MIT',
    description='A pythonic library for discovering and controlling Teufel '
                'Raumfeld devices.',
    long_description=readme,
    author='Thomas Feldmann',
    author_email='feldmann.thomas@gmail.com',
    url='https://github.com/tfeldmann/python-raumfeld',
    keywords=['raumfeld', 'upnp', 'soap'],
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
