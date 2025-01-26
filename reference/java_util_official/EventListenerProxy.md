

EventListenerProxy (Java Platform SE 8 )






<!--
try {
if (location.href.indexOf('is-external=true') == -1) {
parent.document.title="EventListenerProxy (Java Platform SE 8 )";
}
}
catch(err) {
}
//-->
var methods = {"i0":10};
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
java.utilClass EventListenerProxy<T extends EventListener>
java.lang.Objectjava.util.EventListenerProxy<T>
All Implemented Interfaces:
EventListener

Direct Known Subclasses:
AWTEventListenerProxy, PropertyChangeListenerProxy, VetoableChangeListenerProxy


```
public abstract class EventListenerProxy<T extends EventListener>
extends Object
implements EventListener
```
An abstract wrapper class for an `EventListener` class
which associates a set of additional parameters with the listener.
Subclasses must provide the storage and accessor methods
for the additional arguments or parameters.For example, a bean which supports named properties
would have a two argument method signature for adding
a `PropertyChangeListener` for a property:
```

 public void addPropertyChangeListener(String propertyName,
                                       PropertyChangeListener listener)
 
```
If the bean also implemented the zero argument get listener method:
```

 public PropertyChangeListener[] getPropertyChangeListeners()
 
```
then the array may contain inner `PropertyChangeListeners`
which are also `PropertyChangeListenerProxy` objects.If the calling method is interested in retrieving the named property
then it would have to test the element to see if it is a proxy class.
Since:
1.4

### Constructor Summary

Constructors Constructor and Description`EventListenerProxy(T listener)`
Creates a proxy for the specified listener.

### Method Summary

All Methods Instance Methods Concrete Methods Modifier and TypeMethod and Description`T``getListener()`
Returns the listener associated with the proxy.

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

### Constructor Detail

#### EventListenerProxy

```
public EventListenerProxy(T listener)
```
Creates a proxy for the specified listener.
Parameters:
`listener` - the listener object

### Method Detail

#### getListener

```
public T getListener()
```
Returns the listener associated with the proxy.
Returns:
the listener associated with the proxy




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

