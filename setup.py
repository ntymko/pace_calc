from setuptools import setup, find_packages


def readme():
  with open('README.md', 'r') as f:
    return f.read()


setup(
  name='pace_calc',
  version='1.0.0',
  author='ntymko',
  author_email='ndilkova28@gmail.com',
  description='Библиотека для расчета темпа бега, скорости и времени',
  long_description=readme(),
  long_description_content_type='text/markdown',
  url='https://github.com/ntymko/pace_calc',
  packages=find_packages(),
  install_requires=[],
  classifiers=[
    'Programming Language :: Python :: 3.6',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent'
  ],
  keywords='pace calc ',
  project_urls={
    'GitHub': 'https://github.com/ntymko/pace_calc'
  },
  python_requires='>=3.6'
)