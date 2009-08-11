import unittest
from zope.component import provideUtility
from zope.testing import doctest, cleanup
from plone.keyring.interfaces import IKeyManager

# Set the secret and test time to constants to keep the tests workable
import plone.formwidget.captcha.browser.captcha as captcha
captcha._TEST_TIME = 5

# Use a real Request and Response; there are too many subtleties
from ZPublisher.Request import Request
from ZPublisher.Response import Response

class DummyRequest(Request):
    def __init__(self):
        env = {'SERVER_NAME': 'nohost',
               'SERVER_PORT': '80',
               'REQUEST_METHOD': 'GET'}
        Request.__init__(self, None, env, Response())

class DummyContext(object):
    def absolute_url(self):
        return 'dummyurl'

class DummyKeyManager(object):
    def secret(self):
        return 'tests-only-stable-value'

def captchaSetUp(test):
    provideUtility(DummyKeyManager(), IKeyManager)

def tearDown(test):
    cleanup.cleanUp()

def test_suite():
    return unittest.TestSuite((
        doctest.DocFileSuite('captcha.txt', globs=globals(),
                             setUp=captchaSetUp, tearDown=tearDown),
        ))

if __name__ == '__main__':
    unittest.main(defaultTest="test_suite")
