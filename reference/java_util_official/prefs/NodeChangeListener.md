

NodeChangeListener (Java Platform SE 8 )







<!--
try {
if (location.href.indexOf('is-external=true') == -1) {
parent.document.title="NodeChangeListener (Java Platform SE 8 )";
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
java.util.prefsInterface NodeChangeListener
All Superinterfaces:
EventListener


```
public interface NodeChangeListener
extends EventListener
```
A listener for receiving preference node change events.
Since:
1.4
See Also:
`Preferences`,
`NodeChangeEvent`,
`PreferenceChangeListener`

### Method Summary

All Methods Instance Methods Abstract Methods Modifier and TypeMethod and Description`void``childAdded(NodeChangeEvent evt)`
This method gets called when a child node is added.`void``childRemoved(NodeChangeEvent evt)`
This method gets called when a child node is removed.

### Method Detail

#### childAdded

```
void childAdded(NodeChangeEvent evt)
```
This method gets called when a child node is added.
Parameters:
`evt` - A node change event object describing the parent
and child node.

#### childRemoved

```
void childRemoved(NodeChangeEvent evt)
```
This method gets called when a child node is removed.
Parameters:
`evt` - A node change event object describing the parent
and child node.




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

