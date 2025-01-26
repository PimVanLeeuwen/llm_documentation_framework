

NodeChangeEvent (Java Platform SE 8 )







<!--
try {
if (location.href.indexOf('is-external=true') == -1) {
parent.document.title="NodeChangeEvent (Java Platform SE 8 )";
}
}
catch(err) {
}
//-->
var methods = {"i0":10,"i1":10};
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
java.util.prefsClass NodeChangeEvent
java.lang.Objectjava.util.EventObjectjava.util.prefs.NodeChangeEvent
All Implemented Interfaces:
Serializable


```
public class NodeChangeEvent
extends EventObject
```
An event emitted by a Preferences node to indicate that
a child of that node has been added or removed.Note, that although NodeChangeEvent inherits Serializable interface from
java.util.EventObject, it is not intended to be Serializable. Appropriate
serialization methods are implemented to throw NotSerializableException.
Since:
1.4
See Also:
`Preferences`,
`NodeChangeListener`,
`PreferenceChangeEvent`

### Field Summary

### Fields inherited from class java.util.EventObject

`source`

### Constructor Summary

Constructors Constructor and Description`NodeChangeEvent(Preferences parent,
Preferences child)`
Constructs a new `NodeChangeEvent` instance.

### Method Summary

All Methods Instance Methods Concrete Methods Modifier and TypeMethod and Description`Preferences``getChild()`
Returns the node that was added or removed.`Preferences``getParent()`
Returns the parent of the node that was added or removed.

### Methods inherited from class java.util.EventObject

`getSource, toString`

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, wait, wait, wait`

### Constructor Detail

#### NodeChangeEvent

```
public NodeChangeEvent(Preferences parent,
                       Preferences child)
```
Constructs a new `NodeChangeEvent` instance.
Parameters:
`parent` - The parent of the node that was added or removed.
`child` - The node that was added or removed.

### Method Detail

#### getParent

```
public Preferences getParent()
```
Returns the parent of the node that was added or removed.
Returns:
The parent Preferences node whose child was added or removed

#### getChild

```
public Preferences getChild()
```
Returns the node that was added or removed.
Returns:
The node that was added or removed.




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

