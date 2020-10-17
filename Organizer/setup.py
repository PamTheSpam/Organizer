from setuptools import setup, find_packages

def read_requierments():
    with open("requierments.txt") as req:
        content = req.read()
        requierments = content.split('\n')

    return requierments

setup(
    name='organize',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=read_requierments(),
    entry_points='''
    [console_scripts]
    organize=organize.cli:cli
    '''
)