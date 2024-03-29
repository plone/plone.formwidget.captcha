This repository is archived and read only.

If you want to unarchive it, then post to the [Admin & Infrastructure (AI) Team category on the Plone Community Forum](https://community.plone.org/c/aiteam/55).

Introduction
============

.. image:: https://secure.travis-ci.org/plone/plone.formwidget.captcha.png?branch=master
    :target: http://travis-ci.org/plone/plone.formwidget.captcha

.. image:: https://coveralls.io/repos/plone/plone.formwidget.captcha/badge.png?branch=master
    :target: https://coveralls.io/r/plone/plone.formwidget.captcha

plone.formwidget.captcha is a z3c.form captcha widget for use with Plone. It is
a z3c.form re-implementation of the `collective.captcha` package written by
Martijn Pieters.

.. _collective.captcha: http://pypi.python.org/pypi/collective.captcha

Buildout Installation
---------------------

Add the following code to your buildout.cfg to install plone.formwidget.captcha::

    [buildout]
    ...
    eggs =
        ...
        plone.formwidget.captcha
        ...

    ...
    [instance]
    ...
    zcml =
        ...
        plone.formwidget.captcha
    ...


Captchas without server state
-----------------------------

(From collective.captcha)

A view to generate a captcha image and/or wav file, and to verify user input
against it.

A cookie is used to transfer state from one request to the next. The state is
used, together with a server-side secret, to create a random string of
characters, which in turn is displayed as a captcha image, or transformed to
an audio file. Verification happens case-insensitively.

Note that the captcha 'word' is only usable for 5-10 minutes, after which the
view will not accept it any more. Moreover, a different word will be generated
for a given session key every 5 minutes.

This makes these captchas replayable for up to 10 minutes if a determined
user keeps sending the same session id. Because of the server-secret though,
captchas are not transferrable between sites.
