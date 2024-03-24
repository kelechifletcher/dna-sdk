from setuptools import setup

with open("./requirements.txt") as requirements_file:
    requirements = list(requirements_file.readlines())

setup(
    name="dna",
    version="0.0.1",
    install_requires=requirements,
    entry_points={
        'console_scripts': [
            'dna = dna.cli:main',
        ],
    }
)
