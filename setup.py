from setuptools import setup, find_packages
from typing import List

HYPEN_E_DOT = "-e ."
def get_requirements(filename:str)-> List[str]:

    requirements = []
    with open(filename,"r") as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements

setup(
    name="gem_stone_price_prediction",
    version="0.0.1",
    description="This package use for pridiction of gem stone price using various input vectors.",
    author="Ambar Gharat",
    author_email="ambargharat9@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt")
)