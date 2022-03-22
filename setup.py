from setuptools import setup

setup(
   name='mlutils',
   version='0.1.1',
   description='Public ML Utilities',
   author='Dave',
   author_email='davetew@step-function.com',
   packages=['mlutils'],  #same as name
   install_requires=['matplotlib'], #external packages as dependencies
)
