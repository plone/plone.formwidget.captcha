from zope import interface
from z3c.form import form, field, button
from zope import schema
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
        return

CaptchaForm = wrap_form(BaseForm)