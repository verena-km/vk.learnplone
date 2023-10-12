from plone.app.portlets.portlets import base
from plone.portlets.interfaces import IPortletDataProvider
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from zope import schema
from zope.interface import implementer


class IExamplePortlet(IPortletDataProvider):
    """A portlet that displays a greeting message."""

    message = schema.TextLine(
        title="Greeting message",
        description="The message to display in the portlet.",
        required=True,
    )


@implementer(IExamplePortlet)
class Assignment(base.Assignment):
    """Portlet assignment."""

    def __init__(self, message="Hello World!"):
        self.message = message

    @property
    def title(self):
        """This property is used to give the title of the portlet in the
        "manage portlets" screen. Here we use the message as a part of the title.
        """
        return f"Greeting: {self.message}"


class Renderer(base.Renderer):
    """Portlet renderer."""

    # Define the page template that will be used to render the portlet
    template = ViewPageTemplateFile("example.pt")

    def message(self):
        """This method is called by the page template to render the portlet."""
        return self.data.message

    def render(self):
        """This method is called whenever the portlet is rendered."""
        return self.template()


class AddForm(base.AddForm):
    """Portlet add form."""

    schema = IExamplePortlet
    label = "Add Greeting Portlet"
    description = "This portlet displays a greeting."

    def create(self, data):
        return Assignment(**data)


class EditForm(base.EditForm):
    """Portlet edit form."""

    schema = IExamplePortlet
    label = "Edit Greeting Portlet"
    description = "This portlet displays a greeting."