from distutils.core import setup


setup(
    name='raumfeld',
    packages=['raumfeld'],  # this must be the same as the name above
    version='0.2',
    install_requires=['pysimplesoap'],
    license='MIT',
    description='A pythonic library for discovering and controlling Teufel '
                'Raumfeld devices.',
    author='Thomas Feldmann',
    author_email='feldmann.thomas@gmail.com',
    url='https://github.com/tfeldmann/python-raumfeld',
    keywords=['raumfeld', 'upnp', 'soap'],
    classifiers=[],
)
