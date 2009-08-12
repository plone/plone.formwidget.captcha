Captcha widget
==============

plone.formwidget.captcha provides a captcha widget based on the
collective.captcha widget.

    >>> from plone.formwidget.captcha import CaptchaFieldWidget

First, set up a simple test form and context.

    >>> from zope.interface import alsoProvides
    >>> from zope.publisher.browser import TestRequest
    >>> from zope.annotation.interfaces import IAttributeAnnotatable
    >>> from z3c.form.interfaces import IFormLayer

    >>> def make_request(path, form={}):
    ...     request = TestRequest()
    ...     request.form.update(form)
    ...     alsoProvides(request, IFormLayer)
    ...     alsoProvides(request, IAttributeAnnotatable)
    ...     request._traversed_names = path.split('/')
    ...     return request

    >>> from zope.interface import Interface
    >>> from zope import schema
    >>> from z3c.form import form, field, button
    >>> from plone.z3cform.layout import wrap_form

    >>> class ICaptchaForm(Interface):
    ...     subject = schema.TextLine(title=u"Subject",
    ...                               description=u"",
    ...                               required=True)
    ...
    ...     captcha = schema.TextLine(title=u"Captcha",
    ...                               description=u"",
    ...                               required=False)

    >>> from z3c.form.interfaces import IFieldsForm
    >>> from zope.interface import implements
    >>> class CaptchaForm(form.Form):
    ...     implements(ICaptchaForm)
    ...     fields = field.Fields(ICaptchaForm)
    ...     fields['captcha'].widgetFactory = CaptchaFieldWidget
    ...
    ...     @button.buttonAndHandler(u'Apply')
    ...     def handleApply(self, action):
    ...         data, errors = self.extractData()
    ...         if data.has_key('captcha'):
    ...             # Verify the user input against the captcha
    ...             captcha = CaptchaValidator(self.context, self.request, None, ICaptchaForm['captcha'], None)
    ...             if data.has_key('subject') and captcha.validate(data['captcha']):
    ...                 # if captcha validation passes, print the subject
    ...                 print data['subject']
    ...         return


    >>> form_view = wrap_form(CaptchaForm)

    >>> from zope.component import provideAdapter
    >>> from zope.publisher.interfaces.browser import IBrowserRequest
    >>> from zope.interface import Interface

    >>> provideAdapter(adapts=(ICaptchaForm, IBrowserRequest),
    ...                provides=Interface,
    ...                factory=form_view,
    ...                name=u"captcha-form")

    >>> from OFS.SimpleItem import SimpleItem
    >>> class Bar(SimpleItem):
    ...     __allow_access_to_unprotected_subobjects__ = 1
    ...     implements(ICaptchaForm)
    ...
    ...     def __init__(self, id):
    ...         self.id = id
    ...         self.subject = u""
    ...         self.captcha = u""

Let us now look up the form and attempt to render the widget.

    >>> from zope.component import getMultiAdapter
    >>> from OFS.Application import Application
    >>> app = Application()
    >>> app.REQUEST = make_request('/') # eeeevil
    >>> context = Bar('bar').__of__(app)

Simulates traversal:

    >>> request = make_request('bar/@@captcha-form')
    >>> form_view = getMultiAdapter((context, request), name=u"captcha-form").__of__(context)
    >>> form_view.__name__ = 'captcha-form'

Todo
