from setuptools import find_packages,setup
from typing import List

def get_requirements(file_path: str) -> List[str]:
    """Return the requirements from the file."""
    
    requirements=[]
    
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace('\n','') for req in requirements]

    return requirements





setup(
    name='ML project',
    version='0.0.1',
    author='Vishal Singh',
    author_email='vishalchaudhary68981@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)