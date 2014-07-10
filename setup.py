try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

requires = ['pysimplesoap']
packages = ['raumfeld']

with open('README.rst') as f:
    readme = f.read()

setup(
    name='raumfeld',
    version='0.2',
    description='A pythonic library for discovering and controlling Teufel '
                'Raumfeld devices.',
    license='MIT',
    author='Thomas Feldmann',
    author_email='feldmann.thomas@gmail.com',
    url='https://github.com/tfeldmann/python-raumfeld',
    long_description=readme,
    packages=packages,
    install_requires=requires,
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
