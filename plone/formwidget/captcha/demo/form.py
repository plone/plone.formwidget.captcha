from Acquisition import aq_inner
from zope import interface
from zope import schema
from zope.component import getMultiAdapter
from z3c.form import form, field, button
from plone.z3cform.layout import wrap_form
from plone.formwidget.captcha.widget import CaptchaFieldWidget


class ICaptchaForm(interface.Interface):
    captcha = schema.TextLine(title=u"Captcha",
                              description=u"",
                              required=False)

class Captcha(object):
    captcha = ''
    def __init__(self, context):
        self.context = context

class BaseForm(form.Form):
    """ example captcha form """
    fields = field.Fields(ICaptchaForm)
    fields['captcha'].widgetFactory = CaptchaFieldWidget

    @button.buttonAndHandler(u'Save')
    def handleApply(self, action):
        data, errors = self.extractData()
        if data.has_key('captcha'):
            # Verify the user input against the captcha
            captcha = getMultiAdapter((aq_inner(self.context), self.request), name='captcha')
            if captcha.verify(data['captcha']):
                print 'Captcha validation passed.'
            else:
                print 'The code you entered was wrong, please enter the new one.'
        return

CaptchaForm = wrap_form(BaseForm)