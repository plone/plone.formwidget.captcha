Changelog
=========

1.0.3 (2016-03-04)
------------------

* Add empty ``plone.pot`` file for ``rebuild_i18n.sh`` script to work.
  [davidjb]

* Add Czech translation
  [naro]

* Add French translation
  [cedricmessiant]


1.0.2 (2013-10-31)
------------------

* Add Brazilian Portuguese and Spanish translations.
  [hvelarde]


1.0.1 (2012-01-26)
------------------

* Add i18n option and translate to dutch
  [maartenkling]

* Use widgets view class attributes in the template.
  [romanofski]


1.0 (2011-06-29)
----------------

* Use hashlib module by default.
  [thomasdesvenain]

* Zope 2.13 imports (removes warnings under Plone 4.1)
  [thomasdesvenain]


1.0b2 - 2010-09-02
------------------

* Specify allowed_attributes for the captcha view, so the image/audio pages
  are accessible in Zope 2.12.9+.
  [hannosch]

* Move to plone.app.discussion-captcha feature declaration to meta.zcml.
  [timo]

* Fix verify method for empty string input values. This is necessary for
  plone.app.discussion 1.0b5 compatibility.
  [timo]


1.0b1 - 2010-06-02
------------------

* Fix _generate_words method. The "nowish" variable tells us in which 5 minutes
  slot we are in. Therefore we increment the time slot by 1, not by 5 (minutes).
  [tbesluau]

* Declare that plone.formwidget.captcha provides a Captcha field that can be
  used by plone.app.discussion to add a Captcha field to comment forms.
  [timo]


1.0a2 - 2010-01-28
------------------

* Updated package metadata and marked this as a Plone add-on.
  [hannosch]


1.0a1 - 2009-08-28
------------------

* Initial release
  [timo]
