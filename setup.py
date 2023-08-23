from setuptools import setup, find_packages

setup(
    name='upyuns3client',
    version='0.1.0',
    url='https://github.com/evansuner/upyuns3client',
    author='Evan',
    author_email='zhidong.s@outlook.com',
    description='Description of my package',
    packages=find_packages(),
    install_requires=[
        'boto3==1.28.30',
    ],
)
