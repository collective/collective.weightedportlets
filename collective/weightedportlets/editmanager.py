from Products.Five import BrowserView
from collective.weightedportlets import ATTR
import plone.app.portlets.browser
from plone.app.portlets.browser import manage as base
from collective.weightedportlets.utils import ReplacingViewPageTemplateFile

from Acquisition import aq_inner
from persistent.dict import PersistentDict

from plone.portlets.utils import unhashPortletInfo
from plone.app.portlets.utils import assignment_mapping_from_key
from plone.app.portlets.interfaces import IPortletPermissionChecker


class AssignPortletWeight(BrowserView):
    """Opertions on portlets done which used to be done with KSS
       now its applied by a BrowserView and some AJAX
    """
    def weighted_message(self, message):
        """ Outputting some HTML to place the message in """
        return '<div class="weightedmessage">' + message + '</div>'

    def __call__(self):
        """ We look for the weight score and the portlet hash,
            if we have neither than we return an error message """
        request = self.request
        weight = request.get('weight', None)
        portlethash = request.get('portlethash', None)
        try:
            weight = int(weight)
        except ValueError:
            err = 'Error: You must enter an integer for the portlet weight'
            return self.weighted_message(err)
        if not portlethash:
            return self.weighted_message('Error saving data.')

        info = unhashPortletInfo(portlethash)
        assignments = assignment_mapping_from_key(self.context,
                                                  info['manager'],
                                                  info['category'],
                                                  info['key'])
        IPortletPermissionChecker(assignments.__of__(aq_inner(self.context)))()
        name = info['name']
        if not hasattr(assignments[name], ATTR):
            setattr(assignments[name], ATTR, PersistentDict())
        getattr(assignments[name], ATTR)['weight'] = weight
        return ''


class PortletWeightInfo(BrowserView):

    def portlet_weight(self, renderer, portlet_index):
        assignments = renderer._lazyLoadAssignments(renderer.manager)
        assignment = assignments[portlet_index]
        return getattr(assignment, ATTR, {}).get('weight', 50)


class ManageContextualPortlets(base.ManageContextualPortlets):

    index = ReplacingViewPageTemplateFile(
        module=plone.app.portlets.browser,
        filename='templates/edit-manager-macros.pt',
        regexp=r'<span class="managedPortletActions">',
        replacement="""
        <span class="managedPortletActions">
        <input type="text" size="2" class="weight" title="Portlet Weight"
            tal:define="weight_info nocall:context/@@portlet-weight-info"
            tal:attributes="value python:weight_info.portlet_weight(view,
             repeat['portlet'].index); data-portlethash portlet/hash;"
            i18n:domain="collective.weightedportlets"
            i18n:attributes="title"/>
        """
    )
