# -*- coding: utf-8 -*-
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.dexterity.interfaces import IDexterityFTI
from vk.learnplone.content.my_type_zope import IMyTypeZope  # NOQA E501
from vk.learnplone.testing import VK_LEARNPLONE_INTEGRATION_TESTING  # noqa
from zope.component import createObject
from zope.component import queryUtility

import unittest


class MyTypeZopeIntegrationTest(unittest.TestCase):

    layer = VK_LEARNPLONE_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer["portal"]
        setRoles(self.portal, TEST_USER_ID, ["Manager"])
        self.parent = self.portal

    def test_ct_my_type_zope_schema(self):
        fti = queryUtility(IDexterityFTI, name="MyType zope")
        schema = fti.lookupSchema()
        self.assertEqual(IMyTypeZope, schema)

    def test_ct_my_type_zope_fti(self):
        fti = queryUtility(IDexterityFTI, name="MyType zope")
        self.assertTrue(fti)

    def test_ct_my_type_zope_factory(self):
        fti = queryUtility(IDexterityFTI, name="MyType zope")
        factory = fti.factory
        obj = createObject(factory)

    def test_ct_my_type_zope_adding(self):
        setRoles(self.portal, TEST_USER_ID, ["Contributor"])
        obj = api.content.create(
            container=self.portal,
            type="MyType zope",
            id="my_type_zope",
        )

        parent = obj.__parent__
        self.assertIn("my_type_zope", parent.objectIds())

        # check that deleting the object works too
        api.content.delete(obj=obj)
        self.assertNotIn("my_type_zope", parent.objectIds())

    def test_ct_my_type_zope_globally_addable(self):
        setRoles(self.portal, TEST_USER_ID, ["Contributor"])
        fti = queryUtility(IDexterityFTI, name="MyType zope")
        self.assertTrue(fti.global_allow, "{0} is not globally addable!".format(fti.id))
