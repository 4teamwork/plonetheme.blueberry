from AccessControl.SecurityInfo import ClassSecurityInformation
from ftw.publisher.core.interfaces import IDataCollector
from plonetheme.blueberry.browser.forms import TIMESTAMP_ANNOTATION_KEY
from plonetheme.blueberry.browser.forms import VARIABLES_ANNOTATION_KEY
from zope.annotation import IAnnotations
from zope.interface import implements


class DesignVariablesDataCollector(object):
    implements(IDataCollector)
    security = ClassSecurityInformation()

    def __init__(self, obj):
        self.obj = obj

    security.declarePrivate('getData')
    def getData(self):
        annotations = IAnnotations(self.obj)
        data = {}

        if VARIABLES_ANNOTATION_KEY in annotations:
            data[VARIABLES_ANNOTATION_KEY] = annotations[VARIABLES_ANNOTATION_KEY]

        if TIMESTAMP_ANNOTATION_KEY in annotations:
            data[TIMESTAMP_ANNOTATION_KEY] = annotations[TIMESTAMP_ANNOTATION_KEY]

        return data

    security.declarePrivate('setData')
    def setData(self, data, metadata):
        IAnnotations(self.obj).update(data)
