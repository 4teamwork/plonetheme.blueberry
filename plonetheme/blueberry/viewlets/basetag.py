from plone.app.layout.viewlets.common import ViewletBase


class BaseTagViewlet(ViewletBase):

    template = '<base href="{}" />'

    def index(self):
        return self.template.format(self.context.absolute_url() + '/')
