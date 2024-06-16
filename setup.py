# setup.py

from setuptools import setup, find_packages

setup(
    name='math_operations',
    version='0.1',
    packages=find_packages(),
    description='A simple package for basic mathematical operations',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/Zakiyou/math_operations.git', 
    author='Ton Nom',
    author_email='ton.email@example.com',
    license='MIT',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
