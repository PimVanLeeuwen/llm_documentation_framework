

PrimitiveIterator.OfDouble (Java Platform SE 8 )








<!--
try {
if (location.href.indexOf('is-external=true') == -1) {
parent.document.title="PrimitiveIterator.OfDouble (Java Platform SE 8 )";
}
}
catch(err) {
}
//-->
var methods = {"i0":18,"i1":18,"i2":18,"i3":6};
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
java.utilInterface PrimitiveIterator.OfDouble
All Superinterfaces:
Iterator<Double>, PrimitiveIterator<Double,DoubleConsumer>

Enclosing interface:
PrimitiveIterator<T,T\_CONS>


```
public static interface PrimitiveIterator.OfDouble
extends PrimitiveIterator<Double,DoubleConsumer>
```
An Iterator specialized for `double` values.
Since:
1.8

### Nested Class Summary

### Nested classes/interfaces inherited from interface java.util.PrimitiveIterator

`PrimitiveIterator.OfDouble, PrimitiveIterator.OfInt, PrimitiveIterator.OfLong`

### Method Summary

All Methods Instance Methods Abstract Methods Default Methods Modifier and TypeMethod and Description`default void``forEachRemaining(Consumer<? super Double> action)`
Performs the given action for each remaining element until all elements
have been processed or the action throws an exception.`default void``forEachRemaining(DoubleConsumer action)`
Performs the given action for each remaining element until all elements
have been processed or the action throws an exception.`default Double``next()`
Returns the next element in the iteration.`double``nextDouble()`
Returns the next `double` element in the iteration.

### Methods inherited from interface java.util.Iterator

`hasNext, remove`

### Method Detail

#### nextDouble

```
double nextDouble()
```
Returns the next `double` element in the iteration.
Returns:
the next `double` element in the iteration
Throws:
`NoSuchElementException` - if the iteration has no more elements

#### forEachRemaining

```
default void forEachRemaining(DoubleConsumer action)
```
Performs the given action for each remaining element until all elements
have been processed or the action throws an exception. Actions are
performed in the order of iteration, if that order is specified.
Exceptions thrown by the action are relayed to the caller.
Specified by:
`forEachRemaining` in interface `PrimitiveIterator<Double,DoubleConsumer>`
Implementation Requirements:
The default implementation behaves as if:
```

     while (hasNext())
         action.accept(nextDouble());
 
```

Parameters:
`action` - The action to be performed for each element
Throws:
`NullPointerException` - if the specified action is null

#### next

```
default Double next()
```
Returns the next element in the iteration.
Specified by:
`next` in interface `Iterator<Double>`
Implementation Requirements:
The default implementation boxes the result of calling
`nextDouble()`, and returns that boxed result.
Returns:
the next element in the iteration

#### forEachRemaining

```
default void forEachRemaining(Consumer<? super Double> action)
```
Performs the given action for each remaining element until all elements
have been processed or the action throws an exception. Actions are
performed in the order of iteration, if that order is specified.
Exceptions thrown by the action are relayed to the caller.
Specified by:
`forEachRemaining` in interface `Iterator<Double>`
Implementation Requirements:
If the action is an instance of `DoubleConsumer` then it is
cast to `DoubleConsumer` and passed to
`forEachRemaining(java.util.function.DoubleConsumer)`; otherwise the action is adapted to
an instance of `DoubleConsumer`, by boxing the argument of
`DoubleConsumer`, and then passed to
`forEachRemaining(java.util.function.DoubleConsumer)`.
Parameters:
`action` - The action to be performed for each element




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

