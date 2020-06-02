from plone.app.layout.viewlets.globalstatusmessage import GlobalStatusMessage
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile


class BlueberryGlobalStatusMessage(GlobalStatusMessage):
    index = ViewPageTemplateFile('globalstatusmessage.pt')
