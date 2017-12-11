#!/usr/bin/env python3

from setuptools import setup

packages = ['example','example/core']
package_dir = {p: 'src/' + p for p in packages}

setup(name='example',
      version='0.1.0',
      description='Example Python package.',
      author='Steve Norum',
      author_email='stevenorum@gmail.com',
      url='www.stevenorum.com',
      packages=packages,
      package_dir=package_dir,
      scripts=['scripts/example_script'],
      test_suite='tests'
)
