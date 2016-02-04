# pylint: disable=E0211, E0213
# E0211: Method has no argument
# E0213: Method should have "self" as first argument

from zope.interface import Interface


class IBlueberryLayer(Interface):
    """Browser layer for plonetheme.blueberry.
    """


class ICustomDesignVariablesSchema(Interface):
    """
    This multi-adapter interface is used to get the current variables schema
    used in the customization form for the given context.
    """
    def __init__(context, request):
        """
        Adapts a navigation root and a request.
        """
