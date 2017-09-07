# -*- coding: utf-8 -*-
"""
This module contains the tool of collective.weightedportlets
"""
import os
from setuptools import setup, find_packages

def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

version = '1.2dev'

long_description = (
    read('README.rst')
    + '\n' +
    'Change history\n'
    '==============\n'
    + '\n' +
    read('CHANGES.txt')
    )

setup(name='collective.weightedportlets',
      version=version,
      description="Adds the ability to tweak portlet ordering by giving each portlet a weight.",
      long_description=long_description,
      # Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        'Framework :: Plone',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        ],
      keywords='plone portlets',
      author='David Glick',
      author_email='david@glicksoftware.com',
      url='http://plone.org/products/collective.weightedportlets',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['collective', ],
      include_package_data=True,
      zip_safe=False,
      install_requires=['setuptools',
                        'plone.app.portlets',
                        # -*- Extra requirements: -*-
                        ],
      extras_require=dict(test=['plone.app.testing', 'unittest2']),
      entry_points="""
      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
