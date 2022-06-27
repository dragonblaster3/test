from setuptools import setup

def readme():
    with open('README.md') as f:
        return f.read()

setup ( name = 'mypackage' ,
version = '6.8.1',
description= 'project.' ,
classifiers=[
    'Development Status :: 5 Production / Stable ' ,
    'License :: OSI Approved :: MIT License'  ,
    'Programming Language :: Python :: 3' ,
    'Operating Systen : 05 Independent'
],
author = 'sid' ,
author_email='siddantkva8a@gmail.com' ,
keywords = ' core package ' ,
License= 'MIT' ,
packages =['mypackage'] ,
include_package_data= True ,
zip_safe = False )