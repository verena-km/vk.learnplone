# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from vk.learnplone.testing import VK_LEARNPLONE_INTEGRATION_TESTING  # noqa: E501

import unittest


try:
    from Products.CMFPlone.utils import get_installer
except ImportError:
    get_installer = None


class TestSetup(unittest.TestCase):
    """Test that vk.learnplone is properly installed."""

    layer = VK_LEARNPLONE_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer["portal"]
        if get_installer:
            self.installer = get_installer(self.portal, self.layer["request"])
        else:
            self.installer = api.portal.get_tool("portal_quickinstaller")

    def test_product_installed(self):
        """Test if vk.learnplone is installed."""
        self.assertTrue(self.installer.is_product_installed("vk.learnplone"))

    def test_browserlayer(self):
        """Test that IVkLearnploneLayer is registered."""
        from plone.browserlayer import utils
        from vk.learnplone.interfaces import IVkLearnploneLayer

        self.assertIn(IVkLearnploneLayer, utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = VK_LEARNPLONE_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer["portal"]
        if get_installer:
            self.installer = get_installer(self.portal, self.layer["request"])
        else:
            self.installer = api.portal.get_tool("portal_quickinstaller")
        roles_before = api.user.get_roles(TEST_USER_ID)
        setRoles(self.portal, TEST_USER_ID, ["Manager"])
        self.installer.uninstall_product("vk.learnplone")
        setRoles(self.portal, TEST_USER_ID, roles_before)

    def test_product_uninstalled(self):
        """Test if vk.learnplone is cleanly uninstalled."""
        self.assertFalse(self.installer.is_product_installed("vk.learnplone"))

    def test_browserlayer_removed(self):
        """Test that IVkLearnploneLayer is removed."""
        from plone.browserlayer import utils
        from vk.learnplone.interfaces import IVkLearnploneLayer

        self.assertNotIn(IVkLearnploneLayer, utils.registered_layers())
