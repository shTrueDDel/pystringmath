from setuptools import setup, find_packages

def readme():
  with open('README.md', 'r') as f:
    return f.read()

setup(
  name='pystringmath',
  version='1.0.3',
  author='shTrueDDel',
  author_email='xeosscript@gmail.com',
  description='Package for string maths',
  long_description=readme(),
  long_description_content_type='text/markdown',
  url='https://github.com/shTrueDDel/pystringmath/',
  packages=find_packages(),
  install_requires=[''],
  classifiers=[
    'Programming Language :: Python :: 3.13',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent'
  ],
  keywords='math string mathstring crypto cryptography encoding decoding',
  project_urls={
    'Documentation': 'https://github.com/shTrueDDel/pystringmath/blob/main/README.MD'
  },
  python_requires='>=3.7'
)