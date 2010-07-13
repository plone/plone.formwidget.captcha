from Acquisition import aq_inner

from z3c.form import validator

from z3c.form.interfaces import IValidator

from zope.component import getMultiAdapter, provideAdapter

from zope.schema import ValidationError

from plone.formwidget.captcha import CaptchaMessageFactory as _


class WrongCaptchaCode(ValidationError):
    __doc__ = _("""The code you entered was wrong, please enter the new one.""")


class CaptchaValidator(validator.SimpleFieldValidator):

    def validate(self, value):
        super(CaptchaValidator, self).validate(value)
        captcha = getMultiAdapter((aq_inner(self.context), self.request), 
                                  name='captcha')
        if value:
            if not captcha.verify(value):
                raise WrongCaptchaCode
            else:
                return True
        raise WrongCaptchaCode
