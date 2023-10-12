# -*- coding: utf-8 -*-
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.portlets.interfaces import IPortletType
from vk.learnplone.testing import VK_LEARNPLONE_FUNCTIONAL_TESTING
from vk.learnplone.testing import VK_LEARNPLONE_INTEGRATION_TESTING
from zope.component import getUtility

import unittest


class PortletIntegrationTest(unittest.TestCase):

    layer = VK_LEARNPLONE_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer["portal"]
        self.app = self.layer["app"]
        self.request = self.app.REQUEST
        setRoles(self.portal, TEST_USER_ID, ["Manager"])

    def test_example_is_registered(self):
        portlet = getUtility(
            IPortletType,
            name="vk.learnplone.portlets.Example",
        )
        self.assertEqual(portlet.addview, "vk.learnplone.portlets.Example")


class PortletFunctionalTest(unittest.TestCase):

    layer = VK_LEARNPLONE_FUNCTIONAL_TESTING

    def setUp(self):
        self.portal = self.layer["portal"]
        setRoles(self.portal, TEST_USER_ID, ["Manager"])
