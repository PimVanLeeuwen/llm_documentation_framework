

EventObject (Java Platform SE 8 )








<!--
try {
if (location.href.indexOf('is-external=true') == -1) {
parent.document.title="EventObject (Java Platform SE 8 )";
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




compact1, compact2, compact3
java.utilClass EventObject
java.lang.Objectjava.util.EventObject
All Implemented Interfaces:
Serializable

Direct Known Subclasses:
AWTEvent, BeanContextEvent, CaretEvent, ChangeEvent, ConnectionEvent, DragGestureEvent, DragSourceEvent, DropTargetEvent, FlavorEvent, HandshakeCompletedEvent, HyperlinkEvent, LineEvent, ListDataEvent, ListSelectionEvent, MenuEvent, NamingEvent, NamingExceptionEvent, NodeChangeEvent, Notification, PopupMenuEvent, PreferenceChangeEvent, PrintEvent, PropertyChangeEvent, RowSetEvent, RowSorterEvent, SSLSessionBindingEvent, StatementEvent, TableColumnModelEvent, TableModelEvent, TreeExpansionEvent, TreeModelEvent, TreeSelectionEvent, UndoableEditEvent, UnsolicitedNotificationEvent


```
public class EventObject
extends Object
implements Serializable
```
The root class from which all event state objects shall be derived.All Events are constructed with a reference to the object, the "source",
that is logically deemed to be the object upon which the Event in question
initially occurred upon.
Since:
JDK1.1
See Also:
Serialized Form

### Field Summary

Fields Modifier and TypeField and Description`protected Object``source`
The object on which the Event initially occurred.

### Constructor Summary

Constructors Constructor and Description`EventObject(Object source)`
Constructs a prototypical Event.

### Method Summary

All Methods Instance Methods Concrete Methods Modifier and TypeMethod and Description`Object``getSource()`
The object on which the Event initially occurred.`String``toString()`
Returns a String representation of this EventObject.

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, wait, wait, wait`

### Field Detail

#### source

```
protected transient Object source
```
The object on which the Event initially occurred.

### Constructor Detail

#### EventObject

```
public EventObject(Object source)
```
Constructs a prototypical Event.
Parameters:
`source` - The object on which the Event initially occurred.
Throws:
`IllegalArgumentException` - if source is null.

### Method Detail

#### getSource

```
public Object getSource()
```
The object on which the Event initially occurred.
Returns:
The object on which the Event initially occurred.

#### toString

```
public String toString()
```
Returns a String representation of this EventObject.
Overrides:
`toString` in class `Object`
Returns:
A a String representation of this EventObject.




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

