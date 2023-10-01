# -*- coding: utf-8 -*-

from Products.Five.browser import BrowserView
from zope.interface import implementer
from zope.interface import Interface


class IFormDemoView(Interface):
    """Marker Interface for IFormDemoView"""


@implementer(IFormDemoView)
class FormDemoView(BrowserView):

    def __call__(self):
        # Implement your own actions:
        self.submitted = False

        form = self.request.form
        print(form)

        if "Submit" in form:
            self.submitted = True
            self.name = form["name"]
            self.response_text = f"Hi {self.name}! Thank you for using this form."

        return self.index()
