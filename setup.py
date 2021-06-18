import os
from setuptools import setup

setup(
    name = "Nabocoin",
    version = "0.0.1",
    author = "https://github.com/zerodois-bcc/",
    description = ("O blockchain-as-a-service mais simples que existe, implementado em Python e Flask. Projeto para as matérias SSC0158 e SSC0147."),
    license = "BSD",
    url = "https://github.com/zerodois-bcc/NaboCoin",
    requires = [
        "flask",
        "flask_sqlalchemy",
        "werkzeug"
    ],
    classifiers=[
        "Development Status :: Initial Mockup",
        "License :: BSD License",
    ]
)