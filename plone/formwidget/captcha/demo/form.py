from Acquisition import aq_inner

from zope import interface
from zope import schema

from zope.component import getMultiAdapter, provideAdapter

from z3c.form import form, field, button, validator

from plone.z3cform.layout import wrap_form

from plone.formwidget.captcha.widget import CaptchaFieldWidget
from plone.formwidget.captcha.validator import CaptchaValidator

class ICaptchaForm(interface.Interface):
    subject = schema.TextLine(title=u"Subject",
                              description=u"",
                              required=True)

    captcha = schema.TextLine(title=u"Captcha",
                              description=u"",
                              required=False)

class Captcha(object):
    subject = u""
    captcha = u""
    def __init__(self, context):
        self.context = context

class BaseForm(form.Form):
    """Example captcha form
    """
    fields = field.Fields(ICaptchaForm)
    fields['captcha'].widgetFactory = CaptchaFieldWidget

    @button.buttonAndHandler(u'Save')
    def handleApply(self, action):
        data, errors = self.extractData()
        if data.has_key('captcha'):
            # Verify the user input against the captcha
            captcha = CaptchaValidator(self.context, self.request, None, ICaptchaForm['captcha'], None)
            if data.has_key('subject') and captcha.validate(data['captcha']):
                # if captcha validation passes, print the subject
                print data['subject']
        return

CaptchaForm = wrap_form(BaseForm)

# Register Captcha validator for the captcha field in the ICaptchaForm
validator.WidgetValidatorDiscriminators(CaptchaValidator, field=ICaptchaForm['captcha'])