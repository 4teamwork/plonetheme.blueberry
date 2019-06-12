from ftw.builder import Builder
from ftw.builder import create
from ftw.testbrowser import browsing
from plone.app.layout.navigation.interfaces import INavigationRoot
from plonetheme.blueberry.browser.dynamic_scss_resources import custom_design_variables_resource_factory
from plonetheme.blueberry.browser.forms import VARIABLES_ANNOTATION_KEY
from plonetheme.blueberry.tests import FunctionalTestCase
from zope.annotation import IAnnotations
import transaction

PERMISSION = 'plonetheme.blueberry: Customize Design Variables'

class TestCustomSCSSVariables(FunctionalTestCase):

    def setUp(self):
        super(TestCustomSCSSVariables, self).setUp()
        self.grant('Manager')

    @browsing
    def test_values_in_annotations(self, browser):
        browser.login()
        browser.visit(self.portal, view='manage-theme')
        browser.fill({
            '$color-primary': '#FF00FF',
            '$color-secondary': 'red',
        }).save()

        annotations = IAnnotations(self.portal)
        self.assertDictEqual(
            {'color_primary': {'value': u'#FF00FF',
                               'variable_name': '$color-primary'},
             'color_secondary': {'value': u'red',
                                 'variable_name': '$color-secondary'}},
            dict(annotations[VARIABLES_ANNOTATION_KEY]))

    @browsing
    def test_value_inheritance(self, browser):
        browser.login()
        browser.visit(self.portal, view='manage-theme')
        browser.fill({
            '$color-primary': 'blue',
            '$color-secondary': 'red',
            '$color-link': 'fuchsia',
        }).save()

        page = create(Builder('folder').titled(u'My Subsite').providing(INavigationRoot))
        browser.visit(page, view='manage-theme', send_authenticator=True)
        browser.fill({
            '$color-secondary': 'green',
        }).save()

        scss_resource = custom_design_variables_resource_factory(
            page, self.request)
        self.assertEqual(
            '$color-primary: blue;\n$color-secondary: red;\n'
            '$color-link: fuchsia;\n$color-secondary: green;',
            scss_resource.get_source(page, self.request)
        )

        page2 = create(Builder('folder').titled(u'My Subsite').within(page)
                       .providing(INavigationRoot))
        browser.visit(page2, view='manage-theme', send_authenticator=True)
        browser.fill({
            '$color-secondary': 'yellow',
        }).save()

        scss_resource = custom_design_variables_resource_factory(
            page2, self.request)
        self.assertEqual(
            '$color-primary: blue;\n$color-secondary: red;\n'
            '$color-link: fuchsia;\n$color-secondary: green;\n'
            '$color-secondary: yellow;',
            scss_resource.get_source(page2, self.request)
        )

    @browsing
    def test_emptying_values(self, browser):
        """
        This test makes sure that when a custom variable is emptied it
        no longer is present in the storage.
        """
        browser.login()
        browser.visit(self.portal, view='manage-theme')
        browser.fill({
            '$color-primary': 'blue',
            '$color-secondary': 'red',
        }).save()

        scss_resource = custom_design_variables_resource_factory(
            self.portal, self.request)
        self.assertEqual(
            '$color-primary: blue;\n$color-secondary: red;',
            scss_resource.get_source(self.portal, self.request)
        )

        # Now empty a value and make sure its no longer there.
        browser.visit(self.portal, view='manage-theme')
        browser.fill({
            '$color-primary': 'blue',
            '$color-secondary': '',
        }).save()

        scss_resource = custom_design_variables_resource_factory(
            self.portal, self.request)
        self.assertEqual(
            '$color-primary: blue;',
            scss_resource.get_source(self.portal, self.request)
        )

    @browsing
    def test_user_action(self, browser):
        action_link_label = 'Customize design'
        action_link_url = 'http://nohost/plone/@@manage-theme'

        # Make sure the manager
        browser.login().visit(self.portal)
        self.assertEqual(
            action_link_url,
            browser.find(action_link_label).attrib['href']
        )

        # Make sure the action is not available for users
        # without the permission to configure the contact form.
        member = create(Builder('user')
                        .named('Hugo', 'Boss')
                        .with_roles('Member'))
        browser.login(member).visit(self.portal)
        self.assertIsNone(browser.find(action_link_label))

        # Give the user the permission to configure the contact form and
        # make sure the user can see the action.
        self.portal.manage_permission(PERMISSION, roles=['Member'],
                                      acquire=False)
        transaction.commit()
        browser.visit(self.portal)
        self.assertEqual(
            action_link_url,
            browser.find(action_link_label).attrib['href']
        )

    @browsing
    def test_action_is_hidden_when_user_has_no_permission(self, browser):
        subsite = create(Builder('folder')
                         .titled(u'My Subsite')
                         .providing(INavigationRoot))
        browser.login().visit(subsite)
        self.assertTrue(browser.find('Customize design'))

        subsite.manage_permission(PERMISSION,
                                  roles=[],
                                  acquire=False)
        transaction.commit()
        browser.reload()
        self.assertFalse(browser.find('Customize design'))
