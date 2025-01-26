

PreferenceChangeListener (Java Platform SE 8 )






<!--
try {
if (location.href.indexOf('is-external=true') == -1) {
parent.document.title="PreferenceChangeListener (Java Platform SE 8 )";
}
}
catch(err) {
}
//-->
var methods = {"i0":6};
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
java.util.prefsInterface PreferenceChangeListener
All Superinterfaces:
EventListener

Functional Interface:
This is a functional interface and can therefore be used as the assignment target for a lambda expression or method reference.


```
@FunctionalInterface
public interface PreferenceChangeListener
extends EventListener
```
A listener for receiving preference change events.
Since:
1.4
See Also:
`Preferences`,
`PreferenceChangeEvent`,
`NodeChangeListener`

### Method Summary

All Methods Instance Methods Abstract Methods Modifier and TypeMethod and Description`void``preferenceChange(PreferenceChangeEvent evt)`
This method gets called when a preference is added, removed or when
its value is changed.

### Method Detail

#### preferenceChange

```
void preferenceChange(PreferenceChangeEvent evt)
```
This method gets called when a preference is added, removed or when
its value is changed.
Parameters:
`evt` - A PreferenceChangeEvent object describing the event source
and the preference that has changed.




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

