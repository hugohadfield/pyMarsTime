#!/usr/bin/env python

from setuptools import setup
import os

here = os.path.abspath(os.path.dirname(__file__))
exec(open(os.path.join(here, 'marstime/version.py')).read())


requirements = [
    # package requirements go here
]
setup(name="marstime",
      version=__version__,
      cmdclass=versioneer.get_cmdclass(),
      description='marstime library, implements the Mars24 algorithm [Allison and McEwan, 2000]',
      author="Christopher Lee",
      url="http://code.foldmountain.com/marstime",
      download_url="https://bitbucket.org/eelsirhc/marstime/downloads",
      author_email="lee@foldmountain.com",
      packages=["marstime"],
      license="LICENSE.txt",
      setup_requires=["setuptools"],
      long_description=open("README.txt").read(),
      classifiers=["License :: OSI Approved :: BSD License",
                  "Intended Audience :: Science/Research",
                  "Programming Language :: Python :: 2.7",
                  "Programming Language :: Python :: 3",
                  "Topic :: Scientific/Engineering :: Astronomy"],
      zip_safe=False,
      install_requires=requirements,
)
