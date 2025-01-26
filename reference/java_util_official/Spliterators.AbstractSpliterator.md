

Spliterators.AbstractSpliterator (Java Platform SE 8 )








<!--
try {
if (location.href.indexOf('is-external=true') == -1) {
parent.document.title="Spliterators.AbstractSpliterator (Java Platform SE 8 )";
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




compact1, compact2, compact3
java.utilClass Spliterators.AbstractSpliterator<T>
java.lang.Objectjava.util.Spliterators.AbstractSpliterator<T>
All Implemented Interfaces:
Spliterator<T>

Enclosing class:
Spliterators


```
public abstract static class Spliterators.AbstractSpliterator<T>
extends Object
implements Spliterator<T>
```
An abstract `Spliterator` that implements `trySplit` to
permit limited parallelism.An extending class need only
implement `tryAdvance`.
The extending class should override
`forEach` if it can
provide a more performant implementation.
API Note:
This class is a useful aid for creating a spliterator when it is not
possible or difficult to efficiently partition elements in a manner
allowing balanced parallel computation.An alternative to using this class, that also permits limited
parallelism, is to create a spliterator from an iterator
(see `Spliterators.spliterator(Iterator, long, int)`. Depending on the
circumstances using an iterator may be easier or more convenient than
extending this class, such as when there is already an iterator
available to use.
Since:
1.8
See Also:
`Spliterators.spliterator(Iterator, long, int)`

### Nested Class Summary

### Nested classes/interfaces inherited from interface java.util.Spliterator

`Spliterator.OfDouble, Spliterator.OfInt, Spliterator.OfLong, Spliterator.OfPrimitive<T,T_CONS,T_SPLITR extends Spliterator.OfPrimitive<T,T_CONS,T_SPLITR>>`

### Field Summary

### Fields inherited from interface java.util.Spliterator

`CONCURRENT, DISTINCT, IMMUTABLE, NONNULL, ORDERED, SIZED, SORTED, SUBSIZED`

### Constructor Summary

Constructors ModifierConstructor and Description`protected` `AbstractSpliterator(long est,
int additionalCharacteristics)`
Creates a spliterator reporting the given estimated size and
additionalCharacteristics.

### Method Summary

All Methods Instance Methods Concrete Methods Modifier and TypeMethod and Description`int``characteristics()`
Returns a set of characteristics of this Spliterator and its
elements.`long``estimateSize()`
Returns an estimate of the number of elements that would be
encountered by a `Spliterator.forEachRemaining(java.util.function.Consumer<? super T>)` traversal, or returns `Long.MAX_VALUE` if infinite, unknown, or too expensive to compute.`Spliterator<T>``trySplit()`
If this spliterator can be partitioned, returns a Spliterator
covering elements, that will, upon return from this method, not
be covered by this Spliterator.

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

### Methods inherited from interface java.util.Spliterator

`forEachRemaining, getComparator, getExactSizeIfKnown, hasCharacteristics, tryAdvance`

### Constructor Detail

#### AbstractSpliterator

```
protected AbstractSpliterator(long est,
                              int additionalCharacteristics)
```
Creates a spliterator reporting the given estimated size and
additionalCharacteristics.
Parameters:
`est` - the estimated size of this spliterator if known, otherwise
`Long.MAX_VALUE`.
`additionalCharacteristics` - properties of this spliterator's
source or elements. If `SIZED` is reported then this
spliterator will additionally report `SUBSIZED`.

### Method Detail

#### trySplit

```
public Spliterator<T> trySplit()
```
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
This implementation permits limited parallelism.
Specified by:
`trySplit` in interface `Spliterator<T>`
Returns:
a `Spliterator` covering some portion of the
elements, or `null` if this spliterator cannot be split

#### estimateSize

```
public long estimateSize()
```
Returns an estimate of the number of elements that would be
encountered by a `Spliterator.forEachRemaining(java.util.function.Consumer<? super T>)` traversal, or returns `Long.MAX_VALUE` if infinite, unknown, or too expensive to compute.If this Spliterator is `Spliterator.SIZED` and has not yet been partially
traversed or split, or this Spliterator is `Spliterator.SUBSIZED` and has
not yet been partially traversed, this estimate must be an accurate
count of elements that would be encountered by a complete traversal.
Otherwise, this estimate may be arbitrarily inaccurate, but must decrease
as specified across invocations of `Spliterator.trySplit()`.
Specified by:
`estimateSize` in interface `Spliterator<T>`
Implementation Requirements:
This implementation returns the estimated size as reported when
created and, if the estimate size is known, decreases in size when
split.
Returns:
the estimated size, or `Long.MAX_VALUE` if infinite,
unknown, or too expensive to compute.

#### characteristics

```
public int characteristics()
```
Returns a set of characteristics of this Spliterator and its
elements. The result is represented as ORed values from `Spliterator.ORDERED`, `Spliterator.DISTINCT`, `Spliterator.SORTED`, `Spliterator.SIZED`,
`Spliterator.NONNULL`, `Spliterator.IMMUTABLE`, `Spliterator.CONCURRENT`,
`Spliterator.SUBSIZED`. Repeated calls to `characteristics()` on
a given spliterator, prior to or in-between calls to `trySplit`,
should always return the same result.If a Spliterator reports an inconsistent set of
characteristics (either those returned from a single invocation
or across multiple invocations), no guarantees can be made
about any computation using this Spliterator.
Specified by:
`characteristics` in interface `Spliterator<T>`
Implementation Requirements:
This implementation returns the characteristics as reported when
created.
Returns:
a representation of characteristics




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

