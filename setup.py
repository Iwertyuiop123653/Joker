from setuptools import setup, find_packages

classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]

setup(
    project_urls={
      'Documentation': 'https://joking.readthedocs.io/en/latest/',
      'Say Thanks!': 'https://saythanks.io/to/Iwertyuiop123653/',
      'Source': 'https://github.com/Iwertyuiop123653/Joker/',
      'Tracker': 'https://github.com/Iwertyuiop123653/Joker/issues/',
    },
  name='Joking',
  version='2.8.0',
  description='Just-kidding is a python library for getting random dad jokes and more kinds of jokes',
  long_description=open('README.md').read() + '\n\n\n' + open('CHANGELOG.txt').read(),
  url='https://github.com/Iwertyuiop123653/Joker',
  author='Hasty shrimp452',
  author_email='hahacoolguystaco@gmail.com',
  license='MIT',
  classifiers=classifiers,
  keywords='Dad jokes',
  packages=find_packages(),
  install_requires=['bs4'],
  long_description_content_type='text/markdown'
)

