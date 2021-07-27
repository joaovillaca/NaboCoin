from setuptools import setup

#setup da aplicação
setup(
    name='application',
    packages=['application'],
    include_package_data=True,
    install_requires=[
        'flask',
    ],
)