Introduction
============

The Plone portlets system gives site managers a powerful system for assigning
portlets to different sections, content types, and groups.  However, there is a
predefined order in which portlets coming from these sources are displayed. So
there is no built-in way to, for instance, specify that one contextual portlet
should appear above any inherited portlets and another one should appear below
them.

This product addresses that limitation by adding to each portlet assignment a
"weight" field on the portlet management pages, where an integer can be
specified (it defaults to 50). The full list of portlets will be retrieved in
their standard order; then a final sort based on the weight will be applied
before the portlets are displayed.  Portlets with a lower weight will be sorted
to the top, while portlets with a higher weight will be sorted to the bottom.

So, for example, if I wanted to display one contextual portlet above all
inherited portlets and one contextual portlet below all inherited portlets,
I could set their weights to 40 and 60 respectively.

Note that adjustments to the portlet order are saved via an AJAX request; you
don't have to press a button and reload the page to save the new weights.

Import and export of portlet assignment weights via GenericSetup is also
supported.


Installation
============

Add the collective.weightedportlets egg to your buildout.  If using Plone
3.1 or 3.2, make sure you add its ZCML as well.  The ZCML should be
loaded automatically in Plone >= 3.3.

Start Zope and install "Weighted Portlet Ordering" via the Add/Remove Products
panel in Site Setup.


Compatibility
=============

This product requires Plone 3.1 or greater.

This product operates by overriding the following parts of the portlet
machinery.  You may run into problems if using other products or custom
code that also overrides these components:

* the template macros used to render the portlet management UI
* the IPortletRetriever adapter
* the IPortletAssignmentExportImportHandler adapter


Self-certification
==================

* [X] Internationalized
* [X] Unit tests
* [X] End-user documentation
* [X] Internal documentation (documentation, interfaces, etc.)
* [X] Existed and maintained for at least 6 months
* [X] Installs and uninstalls cleanly
* [X] Code structure follows best practice
* [X] No side effects on Plone sites where not installed


Credits
=======

David Glick [davisagli]

Thanks to Martin Aspeli for the Plone 3 portlet system.
