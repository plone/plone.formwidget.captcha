from setuptools import setup, find_packages

version = '1.0a2'

setup(name='plone.formwidget.captcha',
      version=version,
      description="Captcha widget for Plone.",
      long_description=open("README.txt").read() + "\n" +
                       open("CHANGES.txt").read(),
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        ],
      keywords='',
      author='Timo Stollenwerk',
      author_email='timo@zmag.de',
      url='http://pypi.python.org/pypi/plone.formwidget.captcha',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['plone'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'skimpyGimpy',
          'plone.keyring',
          'plone.z3cform',
      ],
      entry_points="""
      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
