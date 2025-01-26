

Spliterator.OfDouble (Java Platform SE 8 )








<!--
try {
if (location.href.indexOf('is-external=true') == -1) {
parent.document.title="Spliterator.OfDouble (Java Platform SE 8 )";
}
}
catch(err) {
}
//-->
var methods = {"i0":18,"i1":18,"i2":18,"i3":6,"i4":6};
var tabs = {65535:["t0","All Methods"],2:["t2","Instance Methods"],4:["t3","Abstract Methods"],16:["t5","Default Methods"]};
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
java.utilInterface Spliterator.OfDouble
All Superinterfaces:
Spliterator<Double>, Spliterator.OfPrimitive<Double,DoubleConsumer,Spliterator.OfDouble>

All Known Implementing Classes:
Spliterators.AbstractDoubleSpliterator

Enclosing interface:
Spliterator<T>


```
public static interface Spliterator.OfDouble
extends Spliterator.OfPrimitive<Double,DoubleConsumer,Spliterator.OfDouble>
```
A Spliterator specialized for `double` values.
Since:
1.8

### Nested Class Summary

### Nested classes/interfaces inherited from interface java.util.Spliterator

`Spliterator.OfDouble, Spliterator.OfInt, Spliterator.OfLong, Spliterator.OfPrimitive<T,T_CONS,T_SPLITR extends Spliterator.OfPrimitive<T,T_CONS,T_SPLITR>>`

### Field Summary

### Fields inherited from interface java.util.Spliterator

`CONCURRENT, DISTINCT, IMMUTABLE, NONNULL, ORDERED, SIZED, SORTED, SUBSIZED`

### Method Summary

All Methods Instance Methods Abstract Methods Default Methods Modifier and TypeMethod and Description`default void``forEachRemaining(Consumer<? super Double> action)`
Performs the given action for each remaining element, sequentially in
the current thread, until all elements have been processed or the action
throws an exception.`default void``forEachRemaining(DoubleConsumer action)`
Performs the given action for each remaining element, sequentially in
the current thread, until all elements have been processed or the
action throws an exception.`default boolean``tryAdvance(Consumer<? super Double> action)`
If a remaining element exists, performs the given action on it,
returning `true`; else returns `false`.`boolean``tryAdvance(DoubleConsumer action)`
If a remaining element exists, performs the given action on it,
returning `true`; else returns `false`.`Spliterator.OfDouble``trySplit()`
If this spliterator can be partitioned, returns a Spliterator
covering elements, that will, upon return from this method, not
be covered by this Spliterator.

### Methods inherited from interface java.util.Spliterator

`characteristics, estimateSize, getComparator, getExactSizeIfKnown, hasCharacteristics`

### Method Detail

#### trySplit

```
Spliterator.OfDouble trySplit()
```
Description copied from interface: `Spliterator`
If this spliterator can be partitioned, returns a Spliterator
covering elements, that will, upon return from this method, not
be covered by this Spliterator.If this Spliterator is `Spliterator.ORDERED`, the returned Spliterator
must cover a strict prefix of the elements.Unless this Spliterator covers an infinite number of elements,
repeated calls to `trySplit()` must eventually return `null`.
Upon non-null return:the value reported for `estimateSize()` before splitting,
must, after splitting, be greater than or equal to `estimateSize()`
for this and the returned Spliterator; andif this Spliterator is `SUBSIZED`, then `estimateSize()`
for this spliterator before splitting must be equal to the sum of
`estimateSize()` for this and the returned Spliterator after
splitting.This method may return `null` for any reason,
including emptiness, inability to split after traversal has
commenced, data structure constraints, and efficiency
considerations.
Specified by:
`trySplit` in interface `Spliterator<Double>`
Specified by:
`trySplit` in interface `Spliterator.OfPrimitive<Double,DoubleConsumer,Spliterator.OfDouble>`
Returns:
a `Spliterator` covering some portion of the
elements, or `null` if this spliterator cannot be split

#### tryAdvance

```
boolean tryAdvance(DoubleConsumer action)
```
Description copied from interface: `Spliterator.OfPrimitive`
If a remaining element exists, performs the given action on it,
returning `true`; else returns `false`. If this
Spliterator is `Spliterator.ORDERED` the action is performed on the
next element in encounter order. Exceptions thrown by the
action are relayed to the caller.
Specified by:
`tryAdvance` in interface `Spliterator.OfPrimitive<Double,DoubleConsumer,Spliterator.OfDouble>`
Parameters:
`action` - The action
Returns:
`false` if no remaining elements existed
upon entry to this method, else `true`.

#### forEachRemaining

```
default void forEachRemaining(DoubleConsumer action)
```
Description copied from interface: `Spliterator.OfPrimitive`
Performs the given action for each remaining element, sequentially in
the current thread, until all elements have been processed or the
action throws an exception. If this Spliterator is `Spliterator.ORDERED`,
actions are performed in encounter order. Exceptions thrown by the
action are relayed to the caller.
Specified by:
`forEachRemaining` in interface `Spliterator.OfPrimitive<Double,DoubleConsumer,Spliterator.OfDouble>`
Parameters:
`action` - The action

#### tryAdvance

```
default boolean tryAdvance(Consumer<? super Double> action)
```
If a remaining element exists, performs the given action on it,
returning `true`; else returns `false`. If this
Spliterator is `Spliterator.ORDERED` the action is performed on the
next element in encounter order. Exceptions thrown by the
action are relayed to the caller.
Specified by:
`tryAdvance` in interface `Spliterator<Double>`
Implementation Requirements:
If the action is an instance of `DoubleConsumer` then it is
cast to `DoubleConsumer` and passed to
`tryAdvance(java.util.function.DoubleConsumer)`; otherwise
the action is adapted to an instance of `DoubleConsumer`, by
boxing the argument of `DoubleConsumer`, and then passed to
`tryAdvance(java.util.function.DoubleConsumer)`.
Parameters:
`action` - The action
Returns:
`false` if no remaining elements existed
upon entry to this method, else `true`.

#### forEachRemaining

```
default void forEachRemaining(Consumer<? super Double> action)
```
Performs the given action for each remaining element, sequentially in
the current thread, until all elements have been processed or the action
throws an exception. If this Spliterator is `Spliterator.ORDERED`, actions
are performed in encounter order. Exceptions thrown by the action
are relayed to the caller.
Specified by:
`forEachRemaining` in interface `Spliterator<Double>`
Implementation Requirements:
If the action is an instance of `DoubleConsumer` then it is
cast to `DoubleConsumer` and passed to
`forEachRemaining(java.util.function.DoubleConsumer)`;
otherwise the action is adapted to an instance of
`DoubleConsumer`, by boxing the argument of
`DoubleConsumer`, and then passed to
`forEachRemaining(java.util.function.DoubleConsumer)`.
Parameters:
`action` - The action




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

