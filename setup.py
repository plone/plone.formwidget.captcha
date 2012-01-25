from setuptools import setup, find_packages

version = '1.0.1'

setup(name='plone.formwidget.captcha',
      version=version,
      description="Captcha widget for Plone.",
      long_description=open("README.txt").read() + "\n" +
                       open("CHANGES.txt").read(),
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        ],
      keywords='plone discussion plone.app.discussion spam captcha',
      author='Timo Stollenwerk - Plone Foundation',
      author_email='plone-developers@lists.sourceforge.net',
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
