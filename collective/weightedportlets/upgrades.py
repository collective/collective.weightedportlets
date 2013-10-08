from Products.CMFCore.utils import getToolByName
from transaction import commit

default_profile = 'profile-collective.weightedportlets:default'


def upgrade_from_kss(portal):
    print "Upgrade collective.weightedportlets to use Ajax"
    portal_setup = getToolByName(portal, 'portal_setup')
    portal_setup.runImportStepFromProfile(default_profile, 'jsregistry')
    commit()
