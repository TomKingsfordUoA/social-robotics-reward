from setuptools import setup, find_packages  # type: ignore


__version__ = '0.1.0'

with open('requirements.txt') as f_requirements:
    requirements = f_requirements.read().splitlines()

setup(
    name='social-robotics-reward',
    version=__version__,
    author='Tom Kingsford',
    author_email='tkin063@aucklanduni.ac.nz',
    url='https://github.com/TomKingsfordUoA/social-robotics-reward',
    packages=find_packages(),
    entry_points={
        'console_scripts': ['srr=social_robotics_reward.srr:main']
    },
    include_package_data=True,
    install_requires=requirements,
)
