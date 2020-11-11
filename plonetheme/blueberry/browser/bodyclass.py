from Products.CMFPlone.utils import getFSVersionTuple
from plone.app.layout.globals.interfaces import IBodyClassAdapter
from zope.browserpage.viewpagetemplatefile import ViewPageTemplateFile as ZopeViewPageTemplateFile  # noqa
from zope.component import adapter
from zope.interface import Interface
from zope.interface import implementer


@adapter(Interface, Interface)
@implementer(IBodyClassAdapter)
class PloneVersionBodyClass(object):

    def __init__(self, context, request):
        self.context = context
        self.request = request

    def get_classes(self, template, view):
        return [
            'plone-%d' % getFSVersionTuple()[0],
        ]
