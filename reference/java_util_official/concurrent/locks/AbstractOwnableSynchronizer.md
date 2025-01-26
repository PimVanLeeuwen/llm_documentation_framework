

AbstractOwnableSynchronizer (Java Platform SE 8 )







<!--
try {
if (location.href.indexOf('is-external=true') == -1) {
parent.document.title="AbstractOwnableSynchronizer (Java Platform SE 8 )";
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
java.util.concurrent.locksClass AbstractOwnableSynchronizer
java.lang.Objectjava.util.concurrent.locks.AbstractOwnableSynchronizer
All Implemented Interfaces:
Serializable

Direct Known Subclasses:
AbstractQueuedLongSynchronizer, AbstractQueuedSynchronizer


```
public abstract class AbstractOwnableSynchronizer
extends Object
implements Serializable
```
A synchronizer that may be exclusively owned by a thread. This
class provides a basis for creating locks and related synchronizers
that may entail a notion of ownership. The
`AbstractOwnableSynchronizer` class itself does not manage or
use this information. However, subclasses and tools may use
appropriately maintained values to help control and monitor access
and provide diagnostics.
Since:
1.6
See Also:
Serialized Form

### Constructor Summary

Constructors ModifierConstructor and Description`protected` `AbstractOwnableSynchronizer()`
Empty constructor for use by subclasses.

### Method Summary

All Methods Instance Methods Concrete Methods Modifier and TypeMethod and Description`protected Thread``getExclusiveOwnerThread()`
Returns the thread last set by `setExclusiveOwnerThread`,
or `null` if never set.`protected void``setExclusiveOwnerThread(Thread thread)`
Sets the thread that currently owns exclusive access.

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

### Constructor Detail

#### AbstractOwnableSynchronizer

```
protected AbstractOwnableSynchronizer()
```
Empty constructor for use by subclasses.

### Method Detail

#### setExclusiveOwnerThread

```
protected final void setExclusiveOwnerThread(Thread thread)
```
Sets the thread that currently owns exclusive access.
A `null` argument indicates that no thread owns access.
This method does not otherwise impose any synchronization or
`volatile` field accesses.
Parameters:
`thread` - the owner thread

#### getExclusiveOwnerThread

```
protected final Thread getExclusiveOwnerThread()
```
Returns the thread last set by `setExclusiveOwnerThread`,
or `null` if never set. This method does not otherwise
impose any synchronization or `volatile` field accesses.
Returns:
the owner thread




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

