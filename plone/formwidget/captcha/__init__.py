from zope.i18nmessageid import MessageFactory
CaptchaMessageFactory = MessageFactory('plone.formwidget.captcha')

from plone.formwidget.captcha.widget import CaptchaWidget
from plone.formwidget.captcha.widget import CaptchaFieldWidget
from plone.formwidget.captcha.validator import CaptchaValidator