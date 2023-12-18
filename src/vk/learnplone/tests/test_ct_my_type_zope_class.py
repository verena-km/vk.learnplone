# -*- coding: utf-8 -*-
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.dexterity.interfaces import IDexterityFTI
from vk.learnplone.content.my_type_zope_class import IMyTypeZopeClass  # NOQA E501
from vk.learnplone.testing import VK_LEARNPLONE_INTEGRATION_TESTING  # noqa
from zope.component import createObject
from zope.component import queryUtility

import unittest


class MyTypeZopeClassIntegrationTest(unittest.TestCase):

    layer = VK_LEARNPLONE_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer["portal"]
        setRoles(self.portal, TEST_USER_ID, ["Manager"])
        self.parent = self.portal

    def test_ct_my_type_zope_class_schema(self):
        fti = queryUtility(IDexterityFTI, name="MyTypeZopeClass")
        schema = fti.lookupSchema()
        self.assertEqual(IMyTypeZopeClass, schema)

    def test_ct_my_type_zope_class_fti(self):
        fti = queryUtility(IDexterityFTI, name="MyTypeZopeClass")
        self.assertTrue(fti)

    def test_ct_my_type_zope_class_factory(self):
        fti = queryUtility(IDexterityFTI, name="MyTypeZopeClass")
        factory = fti.factory
        obj = createObject(factory)

        self.assertTrue(
            IMyTypeZopeClass.providedBy(obj),
            "IMyTypeZopeClass not provided by {0}!".format(
                obj,
            ),
        )

    def test_ct_my_type_zope_class_adding(self):
        setRoles(self.portal, TEST_USER_ID, ["Contributor"])
        obj = api.content.create(
            container=self.portal,
            type="MyTypeZopeClass",
            id="my_type_zope_class",
        )

        self.assertTrue(
            IMyTypeZopeClass.providedBy(obj),
            "IMyTypeZopeClass not provided by {0}!".format(
                obj.id,
            ),
        )

        parent = obj.__parent__
        self.assertIn("my_type_zope_class", parent.objectIds())

        # check that deleting the object works too
        api.content.delete(obj=obj)
        self.assertNotIn("my_type_zope_class", parent.objectIds())

    def test_ct_my_type_zope_class_globally_addable(self):
        setRoles(self.portal, TEST_USER_ID, ["Contributor"])
        fti = queryUtility(IDexterityFTI, name="MyTypeZopeClass")
        self.assertTrue(fti.global_allow, "{0} is not globally addable!".format(fti.id))
