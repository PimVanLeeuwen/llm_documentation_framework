

PrimitiveIterator (Java Platform SE 8 )






<!--
try {
if (location.href.indexOf('is-external=true') == -1) {
parent.document.title="PrimitiveIterator (Java Platform SE 8 )";
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




compact1, compact2, compact3
java.utilInterface PrimitiveIterator<T,T\_CONS>
Type Parameters:
`T` - the type of elements returned by this PrimitiveIterator. The
type must be a wrapper type for a primitive type, such as
`Integer` for the primitive `int` type.
`T_CONS` - the type of primitive consumer. The type must be a
primitive specialization of `Consumer` for
`T`, such as `IntConsumer` for
`Integer`.

All Superinterfaces:
Iterator<T>

All Known Subinterfaces:
PrimitiveIterator.OfDouble, PrimitiveIterator.OfInt, PrimitiveIterator.OfLong


```
public interface PrimitiveIterator<T,T_CONS>
extends Iterator<T>
```
A base type for primitive specializations of `Iterator`. Specialized
subtypes are provided for `int`, `long`, and
`double` values.The specialized subtype default implementations of `Iterator.next()`
and `Iterator.forEachRemaining(java.util.function.Consumer)` box
primitive values to instances of their corresponding wrapper class. Such
boxing may offset any advantages gained when using the primitive
specializations. To avoid boxing, the corresponding primitive-based methods
should be used. For example, `PrimitiveIterator.OfInt.nextInt()` and
`PrimitiveIterator.OfInt.forEachRemaining(java.util.function.IntConsumer)`
should be used in preference to `PrimitiveIterator.OfInt.next()` and
`PrimitiveIterator.OfInt.forEachRemaining(java.util.function.Consumer)`.Iteration of primitive values using boxing-based methods
`next()` and
`forEachRemaining()`,
does not affect the order in which the values, transformed to boxed values,
are encountered.
Implementation Note:
If the boolean system property `org.openjdk.java.util.stream.tripwire`
is set to `true` then diagnostic warnings are reported if boxing of
primitive values occur when operating on primitive subtype specializations.
Since:
1.8

### Nested Class Summary

Nested Classes Modifier and TypeInterface and Description`static interface``PrimitiveIterator.OfDouble`
An Iterator specialized for `double` values.`static interface``PrimitiveIterator.OfInt`
An Iterator specialized for `int` values.`static interface``PrimitiveIterator.OfLong`
An Iterator specialized for `long` values.

### Method Summary

All Methods Instance Methods Abstract Methods Modifier and TypeMethod and Description`void``forEachRemaining(T_CONS action)`
Performs the given action for each remaining element, in the order
elements occur when iterating, until all elements have been processed
or the action throws an exception.

### Methods inherited from interface java.util.Iterator

`forEachRemaining, hasNext, next, remove`

### Method Detail

#### forEachRemaining

```
void forEachRemaining(T_CONS action)
```
Performs the given action for each remaining element, in the order
elements occur when iterating, until all elements have been processed
or the action throws an exception. Errors or runtime exceptions
thrown by the action are relayed to the caller.
Parameters:
`action` - The action to be performed for each element
Throws:
`NullPointerException` - if the specified action is null




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

