# -*- coding: utf-8 -*-
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.dexterity.interfaces import IDexterityFTI
from vk.learnplone.testing import VK_LEARNPLONE_INTEGRATION_TESTING  # noqa
from zope.component import createObject
from zope.component import queryUtility

import unittest


try:
    from plone.dexterity.schema import portalTypeToSchemaName
except ImportError:
    # Plone < 5
    from plone.dexterity.utils import portalTypeToSchemaName


class MyTypeSuperIntegrationTest(unittest.TestCase):

    layer = VK_LEARNPLONE_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer["portal"]
        setRoles(self.portal, TEST_USER_ID, ["Manager"])
        self.parent = self.portal

    def test_ct_my_type_super_schema(self):
        fti = queryUtility(IDexterityFTI, name="MyType Super")
        schema = fti.lookupSchema()
        schema_name = portalTypeToSchemaName("MyType Super")
        self.assertIn(schema_name.lstrip("plone_0_"), schema.getName())

    def test_ct_my_type_super_fti(self):
        fti = queryUtility(IDexterityFTI, name="MyType Super")
        self.assertTrue(fti)

    def test_ct_my_type_super_factory(self):
        fti = queryUtility(IDexterityFTI, name="MyType Super")
        factory = fti.factory
        obj = createObject(factory)

    def test_ct_my_type_super_adding(self):
        setRoles(self.portal, TEST_USER_ID, ["Contributor"])
        obj = api.content.create(
            container=self.portal,
            type="MyType Super",
            id="my_type_super",
        )

        parent = obj.__parent__
        self.assertIn("my_type_super", parent.objectIds())

        # check that deleting the object works too
        api.content.delete(obj=obj)
        self.assertNotIn("my_type_super", parent.objectIds())

    def test_ct_my_type_super_globally_addable(self):
        setRoles(self.portal, TEST_USER_ID, ["Contributor"])
        fti = queryUtility(IDexterityFTI, name="MyType Super")
        self.assertTrue(fti.global_allow, "{0} is not globally addable!".format(fti.id))
