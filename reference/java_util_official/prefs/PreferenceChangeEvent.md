

PreferenceChangeEvent (Java Platform SE 8 )








<!--
try {
if (location.href.indexOf('is-external=true') == -1) {
parent.document.title="PreferenceChangeEvent (Java Platform SE 8 )";
}
}
catch(err) {
}
//-->
var methods = {"i0":10,"i1":10,"i2":10};
var tabs = {65535:["t0","All Methods"],2:["t2","Instance Methods"],8:["t4","Concrete Methods"]};
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
java.util.prefsClass PreferenceChangeEvent
java.lang.Objectjava.util.EventObjectjava.util.prefs.PreferenceChangeEvent
All Implemented Interfaces:
Serializable


```
public class PreferenceChangeEvent
extends EventObject
```
An event emitted by a Preferences node to indicate that
a preference has been added, removed or has had its value changed.Note, that although PreferenceChangeEvent inherits Serializable interface
from EventObject, it is not intended to be Serializable. Appropriate
serialization methods are implemented to throw NotSerializableException.
Since:
1.4
See Also:
`Preferences`,
`PreferenceChangeListener`,
`NodeChangeEvent`

### Field Summary

### Fields inherited from class java.util.EventObject

`source`

### Constructor Summary

Constructors Constructor and Description`PreferenceChangeEvent(Preferences node,
String key,
String newValue)`
Constructs a new `PreferenceChangeEvent` instance.

### Method Summary

All Methods Instance Methods Concrete Methods Modifier and TypeMethod and Description`String``getKey()`
Returns the key of the preference that was changed.`String``getNewValue()`
Returns the new value for the preference.`Preferences``getNode()`
Returns the preference node that emitted the event.

### Methods inherited from class java.util.EventObject

`getSource, toString`

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, wait, wait, wait`

### Constructor Detail

#### PreferenceChangeEvent

```
public PreferenceChangeEvent(Preferences node,
                             String key,
                             String newValue)
```
Constructs a new `PreferenceChangeEvent` instance.
Parameters:
`node` - The Preferences node that emitted the event.
`key` - The key of the preference that was changed.
`newValue` - The new value of the preference, or null
if the preference is being removed.

### Method Detail

#### getNode

```
public Preferences getNode()
```
Returns the preference node that emitted the event.
Returns:
The preference node that emitted the event.

#### getKey

```
public String getKey()
```
Returns the key of the preference that was changed.
Returns:
The key of the preference that was changed.

#### getNewValue

```
public String getNewValue()
```
Returns the new value for the preference.
Returns:
The new value for the preference, or null if the
preference was removed.




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

