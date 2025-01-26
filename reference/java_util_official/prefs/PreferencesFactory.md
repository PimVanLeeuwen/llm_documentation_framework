

PreferencesFactory (Java Platform SE 8 )







<!--
try {
if (location.href.indexOf('is-external=true') == -1) {
parent.document.title="PreferencesFactory (Java Platform SE 8 )";
}
}
catch(err) {
}
//-->
var methods = {"i0":6,"i1":6};
var tabs = {65535:["t0","All Methods"],2:["t2","Instance Methods"],4:["t3","Abstract Methods"]};
var altColor = "altColor";
var rowColor = "rowColor";
var tableTab = "tableTab";
var activeTableTab = "activeTableTab";

JavaScript is disabled on your browser.


Skip navigation links

OverviewPackageClassUseTreeDeprecatedIndexHelpJava™ PlatformStandard Ed. 8

Prev ClassNext ClassFramesNo FramesAll Classes
<!--
allClassesLink = document.getElementById("allclasses\_navbar\_top");
if(window==top) {
allClassesLink.style.display = "block";
}
else {
allClassesLink.style.display = "none";
}
//-->


Summary:Nested |Field |Constr |MethodDetail:Field |Constr |Method




compact3
java.util.prefsInterface PreferencesFactory
```
public interface PreferencesFactory
```
A factory object that generates Preferences objects. Providers of
new `Preferences` implementations should provide corresponding
PreferencesFactory implementations so that the new
Preferences implementation can be installed in place of the
platform-specific default implementation.This class is for Preferences implementers only.
Normal users of the Preferences facility should have no need to
consult this documentation.
Since:
1.4
See Also:
`Preferences`

### Method Summary

All Methods Instance Methods Abstract Methods Modifier and TypeMethod and Description`Preferences``systemRoot()`
Returns the system root preference node.`Preferences``userRoot()`
Returns the user root preference node corresponding to the calling
user.

### Method Detail

#### systemRoot

```
Preferences systemRoot()
```
Returns the system root preference node. (Multiple calls on this
method will return the same object reference.)
Returns:
the system root preference node

#### userRoot

```
Preferences userRoot()
```
Returns the user root preference node corresponding to the calling
user. In a server, the returned value will typically depend on
some implicit client-context.
Returns:
the user root preference node corresponding to the calling
user




Skip navigation links

OverviewPackageClassUseTreeDeprecatedIndexHelpJava™ PlatformStandard Ed. 8

Prev ClassNext ClassFramesNo FramesAll Classes
<!--
allClassesLink = document.getElementById("allclasses\_navbar\_bottom");
if(window==top) {
allClassesLink.style.display = "block";
}
else {
allClassesLink.style.display = "none";
}
//-->


Summary:Nested |Field |Constr |MethodDetail:Field |Constr |Method


 Submit a bug or feature For further API reference and developer documentation, see Java SE Documentation. That documentation contains more detailed, developer-targeted descriptions, with conceptual overviews, definitions of terms, workarounds, and working code examples. Copyright © 1993, 2025, Oracle and/or its affiliates. All rights reserved. Use is subject to license terms. Also see the documentation redistribution policy. 

