from setuptools import find_packages,setup
from typing import List


def get_requirements() -> List[str]:
    """
    This function will return a list of requirements
    from requirements.txt
    """
    requirement_lst: List[str] = []
    try:
        with open("requirements.txt", "r") as file:
            lines = file.readlines()
            for line in lines:
                requirement = line.strip()
                # Ignore empty lines and "-e ."
                if requirement and requirement != "-e .":
                    requirement_lst.append(requirement)
    except FileNotFoundError:
        print("requirements.txt file not found")

    return requirement_lst

setup(
    name="my_mltestproject",
    version="0.1.0",
    author="hema",
    author_email="your.email@example.com",
    description="A short description of your project",
    packages=find_packages(),  # Automatically includes all packages   //how it identify packages  in which folder __init__.py file is there it treats as package
    install_requires=get_requirements()
)