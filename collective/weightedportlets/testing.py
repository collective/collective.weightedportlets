from zope.configuration import xmlconfig

from plone.app.testing import PloneSandboxLayer
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import IntegrationTesting
from plone.app.testing import FunctionalTesting


class CollectiveWeightedPortlets(PloneSandboxLayer):

    defaultsBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        import collective.weightedportlets
        xmlconfig.file('configure.zcml',
                       collective.weightedportlets,
                       context=configurationContext)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'collective.weightedportlets:default')
        for (memberid, roles) in (('member', ['Member']),
                                  ('contributor', ['Contributor']),
                                  ('editor', ['Editor']),
                                  ('reviewer', ['Reviewer']),
                                  ('manager', ['Manager']), ):
            portal.portal_membership.addMember(memberid,
                                               'secret',
                                               roles, [])


COLLECTIVEWEIGHTEDPORTLETS_FIXTURE = CollectiveWeightedPortlets()


WPORTLETS_INTEGRATION_TESTING = IntegrationTesting(
    bases=(COLLECTIVEWEIGHTEDPORTLETS_FIXTURE,),
    name="CollectiveWeightPortlets:Integration")

WPORTLETS_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(COLLECTIVEWEIGHTEDPORTLETS_FIXTURE,),
    name="CollectiveWeightPortlets:Functional")
