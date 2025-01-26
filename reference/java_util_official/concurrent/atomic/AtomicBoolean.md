

AtomicBoolean (Java Platform SE 8 )












<!--
try {
if (location.href.indexOf('is-external=true') == -1) {
parent.document.title="AtomicBoolean (Java Platform SE 8 )";
}
}
catch(err) {
}
//-->
var methods = {"i0":10,"i1":10,"i2":10,"i3":10,"i4":10,"i5":10,"i6":10};
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
java.util.concurrent.atomicClass AtomicBoolean
java.lang.Objectjava.util.concurrent.atomic.AtomicBoolean
All Implemented Interfaces:
Serializable


```
public class AtomicBoolean
extends Object
implements Serializable
```
A `boolean` value that may be updated atomically. See the
`java.util.concurrent.atomic` package specification for
description of the properties of atomic variables. An
`AtomicBoolean` is used in applications such as atomically
updated flags, and cannot be used as a replacement for a
`Boolean`.
Since:
1.5
See Also:
Serialized Form

### Constructor Summary

Constructors Constructor and Description`AtomicBoolean()`
Creates a new `AtomicBoolean` with initial value `false`.`AtomicBoolean(boolean initialValue)`
Creates a new `AtomicBoolean` with the given initial value.

### Method Summary

All Methods Instance Methods Concrete Methods Modifier and TypeMethod and Description`boolean``compareAndSet(boolean expect,
boolean update)`
Atomically sets the value to the given updated value
if the current value `==` the expected value.`boolean``get()`
Returns the current value.`boolean``getAndSet(boolean newValue)`
Atomically sets to the given value and returns the previous value.`void``lazySet(boolean newValue)`
Eventually sets to the given value.`void``set(boolean newValue)`
Unconditionally sets to the given value.`String``toString()`
Returns the String representation of the current value.`boolean``weakCompareAndSet(boolean expect,
boolean update)`
Atomically sets the value to the given updated value
if the current value `==` the expected value.

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, wait, wait, wait`

### Constructor Detail

#### AtomicBoolean

```
public AtomicBoolean(boolean initialValue)
```
Creates a new `AtomicBoolean` with the given initial value.
Parameters:
`initialValue` - the initial value

#### AtomicBoolean

```
public AtomicBoolean()
```
Creates a new `AtomicBoolean` with initial value `false`.

### Method Detail

#### get

```
public final boolean get()
```
Returns the current value.
Returns:
the current value

#### compareAndSet

```
public final boolean compareAndSet(boolean expect,
                                   boolean update)
```
Atomically sets the value to the given updated value
if the current value `==` the expected value.
Parameters:
`expect` - the expected value
`update` - the new value
Returns:
`true` if successful. False return indicates that
the actual value was not equal to the expected value.

#### weakCompareAndSet

```
public boolean weakCompareAndSet(boolean expect,
                                 boolean update)
```
Atomically sets the value to the given updated value
if the current value `==` the expected value.May fail
spuriously and does not provide ordering guarantees, so is
only rarely an appropriate alternative to `compareAndSet`.
Parameters:
`expect` - the expected value
`update` - the new value
Returns:
`true` if successful

#### set

```
public final void set(boolean newValue)
```
Unconditionally sets to the given value.
Parameters:
`newValue` - the new value

#### lazySet

```
public final void lazySet(boolean newValue)
```
Eventually sets to the given value.
Parameters:
`newValue` - the new value
Since:
1.6

#### getAndSet

```
public final boolean getAndSet(boolean newValue)
```
Atomically sets to the given value and returns the previous value.
Parameters:
`newValue` - the new value
Returns:
the previous value

#### toString

```
public String toString()
```
Returns the String representation of the current value.
Overrides:
`toString` in class `Object`
Returns:
the String representation of the current value




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

