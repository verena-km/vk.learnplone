# -*- coding: utf-8 -*-

from Products.Five.browser import BrowserView
from zope.interface import implementer
from zope.interface import Interface


class IOutputDemoView(Interface):
    """Marker Interface for IOutputDemoView"""


@implementer(IOutputDemoView)
class OutputDemoView(BrowserView):
    def __call__(self):
        self.output_var = "This output comes from a variable."
        print(self.request.items())
        return self.index()

    def output_method(self):
        return "This output comes from a method"
