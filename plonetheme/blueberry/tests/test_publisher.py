from ftw.publisher.core.interfaces import IDataCollector
from persistent.mapping import PersistentMapping
from plonetheme.blueberry.browser.forms import TIMESTAMP_ANNOTATION_KEY
from plonetheme.blueberry.browser.forms import VARIABLES_ANNOTATION_KEY
from plonetheme.blueberry.tests import FunctionalTestCase
from zope.annotation import IAnnotations
from zope.component import getAdapter



class TestDesignVariablesDataCollector(FunctionalTestCase):

    def test(self):
        self.grant('Manager')
        annotations = IAnnotations(self.portal)
        annotations[VARIABLES_ANNOTATION_KEY] = PersistentMapping()
        annotations[VARIABLES_ANNOTATION_KEY]['color_primary'] = {
            'value': 'red',
            'variable_name': '$color-primary',
        }
        annotations[TIMESTAMP_ANNOTATION_KEY] = 1471953385.345843

        collector = getAdapter(self.portal, IDataCollector,
                               name='plonetheme_blueberry_design_variables')
        dump = collector.getData()

        self.assertEquals(
            {VARIABLES_ANNOTATION_KEY: {
                'color_primary': {'value': 'red',
                                  'variable_name': '$color-primary'}},
             TIMESTAMP_ANNOTATION_KEY: 1471953385.345843},
            dump)

        del annotations[VARIABLES_ANNOTATION_KEY]
        del annotations[TIMESTAMP_ANNOTATION_KEY]
        collector.setData(dump, {})

        self.assertEquals({'color_primary':
                           {'value': 'red',
                            'variable_name': '$color-primary'}},
                          dict(annotations[VARIABLES_ANNOTATION_KEY]))
        self.assertEquals(PersistentMapping,
                          type(annotations[VARIABLES_ANNOTATION_KEY]))
        self.assertEquals(1471953385.345843,
                          annotations[TIMESTAMP_ANNOTATION_KEY])
