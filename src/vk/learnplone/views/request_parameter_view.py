# -*- coding: utf-8 -*-

from Products.Five.browser import BrowserView
from zope.interface import implementer
from zope.interface import Interface


class IRequestParameterView(Interface):
    """Marker Interface for IRequestParameterView"""


@implementer(IRequestParameterView)
class RequestParameterView(BrowserView):
    def __call__(self):
        return self.index()
