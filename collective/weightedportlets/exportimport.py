from plone.app.portlets.exportimport.portlets import PropertyPortletAssignmentExportImportHandler
from persistent.dict import PersistentDict
from collective.weightedportlets import ATTR


class WeightWatchingPortletAssignmentImportExportHandler(
        PropertyPortletAssignmentExportImportHandler):

    def import_weight(self, node):
        try:
            weight = int(node.getAttribute('weight'))
        except:
            return

        if not hasattr(self.assignment, ATTR):
            setattr(self.assignment, ATTR, PersistentDict())
        getattr(self.assignment, ATTR)['weight'] = weight

    def export_weight(self, doc, node):
        weight = getattr(self.assignment, ATTR, {}).get('weight')
        if weight is None:
            return
        node.setAttribute('weight', unicode(weight))

    def import_assignment(self, interface, node):
        self.import_weight(node)
        PropertyPortletAssignmentExportImportHandler.import_assignment(
            self, interface, node)

    def export_assignment(self, interface, doc, node):
        self.export_weight(doc, node)
        PropertyPortletAssignmentExportImportHandler.export_assignment(
            self, interface, doc, node)
