from setuptools import find_packages, setup
from typing import List


HYPEN_E_DOT = '-e .'
def get_requirements(file_path: str) -> List[str]:
    '''
    This function returns a list of requirements from a requirements file.
    :param file_path:
    :return:
    '''
    requirements = []
    with open(file_path, "r") as requirements_file:
        requirements = requirements_file.readlines()
        requirements = requirements = [req.strip() for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements



setup(
    name='mlproject',
    version='0.0.1',
    author='Cavidan',
    author_email='behremlicavidan7@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
)