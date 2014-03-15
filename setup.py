from distutils.core import setup

import datecalc

version = datecalc.__version__
author = datecalc.__author__

setup(name='datecalc',
      description='Python module to calculate the day of the week of any date',
      license='BSD',
      version=version,
      author=author,
      author_email="violet@pariahvi.com",
      maintainer=author,
      maintainer_email='violet@pariahvi.com',
      url='http://bitbucket.org/PariahVi/datecalc',
      py_modules=["datecalc"],
      platforms='No particular restrictions',
      classifiers=[
           'Development Status :: 5 - Production/Stable',
           'Intended Audience :: Developers',
           'License :: OSI Approved :: BSD License',
           'Programming Language :: Python',
           'Programming Language :: Python :: 2',
           'Programming Language :: Python :: 3',
           'Programming Language :: Python :: 2.4',
           'Programming Language :: Python :: 2.5',
           'Programming Language :: Python :: 2.6',
           'Programming Language :: Python :: 2.7',
           'Programming Language :: Python :: 3.0',
           'Programming Language :: Python :: 3.1',
           'Programming Language :: Python :: 3.2',
           'Programming Language :: Python :: 3.3',
           'Operating System :: OS Independent',
           'Topic :: Software Development :: Libraries :: Python Modules'
          ]
      )
