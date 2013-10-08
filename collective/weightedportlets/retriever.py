from plone.portlets.retriever import PortletRetriever as BasePortletRetriever
from collective.weightedportlets import ATTR


def getPortletWeight(assignment):
    return getattr(assignment['assignment'], ATTR, {}).get('weight', 50)


class WeightedPortletRetriever(BasePortletRetriever):

    def getPortlets(self):
        assignments = BasePortletRetriever.getPortlets(self)
        assignments.sort(key=getPortletWeight)
        return assignments
