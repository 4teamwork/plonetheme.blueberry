from plone.i18n.normalizer.interfaces import IIDNormalizer
from Products.TinyMCE.adapters.interfaces.JSONSearch import IJSONSearch
from Products.TinyMCE.adapters.JSONSearch import JSONSearch
from zope.component import getUtility
from zope.interface import implements
import json


class BlueberryJSONSearch(JSONSearch):
    """Returns a list of search results in JSON"""
    implements(IJSONSearch)

    listing_base_query = {}

    def getSearchResults(self, filter_portal_types, searchtext):
        """Returns the actual search result"""

        if '*' not in searchtext:
            searchtext += '*'

        catalog_results = []
        results = {
            'parent_url': '',
            'path': [],
        }

        normalizer = getUtility(IIDNormalizer)

        query = self.listing_base_query.copy()
        query.update({
            'portal_type': filter_portal_types,
            'path': '/'.join(self.context.getPhysicalPath()),
            'Title': searchtext,
        })
        if searchtext:
            plone_layout = self.context.restrictedTraverse('@@plone_layout',
                                                           None)

            getIcon = lambda brain: plone_layout.getIcon(brain)()
            brains = self.context.portal_catalog.searchResults(**query)

            catalog_results = [
                   {'id': brain.getId,
                    'uid': brain.UID,
                    'url': brain.getURL(),
                    'portal_type': brain.portal_type,
                    'review_state': brain.review_state or None,
                    'normalized_type': normalizer.normalize(brain.portal_type),
                    'title': brain.Title == "" and brain.id or brain.Title,
                    'icon': getIcon(brain),
                    'description': brain.Description,
                    'is_folderish': brain.is_folderish,

                    } for brain in brains if brain]

        # add catalog_results
        results['items'] = catalog_results

        # never allow upload from search results page
        results['upload_allowed'] = False

        # return results in JSON format
        self.context.REQUEST.response.setHeader("Content-type",
                                                "application/json")
        return json.dumps(results)
