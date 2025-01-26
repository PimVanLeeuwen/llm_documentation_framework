

java.util.prefs (Java Platform SE 8 )





<!--
try {
if (location.href.indexOf('is-external=true') == -1) {
parent.document.title="java.util.prefs (Java Platform SE 8 )";
}
}
catch(err) {
}
//-->

JavaScript is disabled on your browser.


Skip navigation links

OverviewPackageClassUseTreeDeprecatedIndexHelpJava™ PlatformStandard Ed. 8

Prev PackageNext PackageFramesNo FramesAll Classes
<!--
allClassesLink = document.getElementById("allclasses\_navbar\_top");
if(window==top) {
allClassesLink.style.display = "block";
}
else {
allClassesLink.style.display = "none";
}
//-->




Package java.util.prefs
This package allows applications to store and retrieve user and system
preference and configuration data.
See: Description

Interface Summary InterfaceDescriptionNodeChangeListenerA listener for receiving preference node change events.PreferenceChangeListenerA listener for receiving preference change events.PreferencesFactoryA factory object that generates Preferences objects.

Class Summary ClassDescriptionAbstractPreferencesThis class provides a skeletal implementation of the `Preferences`
class, greatly easing the task of implementing it.NodeChangeEventAn event emitted by a Preferences node to indicate that
a child of that node has been added or removed.PreferenceChangeEventAn event emitted by a Preferences node to indicate that
a preference has been added, removed or has had its value changed.PreferencesA node in a hierarchical collection of preference data.

Exception Summary ExceptionDescriptionBackingStoreExceptionThrown to indicate that a preferences operation could not complete because
of a failure in the backing store, or a failure to contact the backing
store.InvalidPreferencesFormatExceptionThrown to indicate that an operation could not complete because
the input did not conform to the appropriate XML document type
for a collection of preferences, as per the `Preferences`
specification.

Package java.util.prefs DescriptionThis package allows applications to store and retrieve user and system
preference and configuration data. This data is stored persistently in an
implementation-dependent backing store. There are two separate trees of
preference nodes, one for user preferences and one for system preferences.

Since:
JDK1.4



Skip navigation links

OverviewPackageClassUseTreeDeprecatedIndexHelpJava™ PlatformStandard Ed. 8

Prev PackageNext PackageFramesNo FramesAll Classes
<!--
allClassesLink = document.getElementById("allclasses\_navbar\_bottom");
if(window==top) {
allClassesLink.style.display = "block";
}
else {
allClassesLink.style.display = "none";
}
//-->



 Submit a bug or feature For further API reference and developer documentation, see Java SE Documentation. That documentation contains more detailed, developer-targeted descriptions, with conceptual overviews, definitions of terms, workarounds, and working code examples. Copyright © 1993, 2025, Oracle and/or its affiliates. All rights reserved. Use is subject to license terms. Also see the documentation redistribution policy. 

