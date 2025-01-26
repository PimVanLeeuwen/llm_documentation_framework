

IntConsumer (Java Platform SE 8 )







<!--
try {
if (location.href.indexOf('is-external=true') == -1) {
parent.document.title="IntConsumer (Java Platform SE 8 )";
}
}
catch(err) {
}
//-->
var methods = {"i0":6,"i1":18};
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
java.util.functionInterface IntConsumer
All Known Subinterfaces:
IntStream.Builder

All Known Implementing Classes:
IntSummaryStatistics, LongSummaryStatistics

Functional Interface:
This is a functional interface and can therefore be used as the assignment target for a lambda expression or method reference.


```
@FunctionalInterface
public interface IntConsumer
```
Represents an operation that accepts a single `int`-valued argument and
returns no result. This is the primitive type specialization of
`Consumer` for `int`. Unlike most other functional interfaces,
`IntConsumer` is expected to operate via side-effects.This is a functional interface
whose functional method is `accept(int)`.
Since:
1.8
See Also:
`Consumer`

### Method Summary

All Methods Instance Methods Abstract Methods Default Methods Modifier and TypeMethod and Description`void``accept(int value)`
Performs this operation on the given argument.`default IntConsumer``andThen(IntConsumer after)`
Returns a composed `IntConsumer` that performs, in sequence, this
operation followed by the `after` operation.

### Method Detail

#### accept

```
void accept(int value)
```
Performs this operation on the given argument.
Parameters:
`value` - the input argument

#### andThen

```
default IntConsumer andThen(IntConsumer after)
```
Returns a composed `IntConsumer` that performs, in sequence, this
operation followed by the `after` operation. If performing either
operation throws an exception, it is relayed to the caller of the
composed operation. If performing this operation throws an exception,
the `after` operation will not be performed.
Parameters:
`after` - the operation to perform after this operation
Returns:
a composed `IntConsumer` that performs in sequence this
operation followed by the `after` operation
Throws:
`NullPointerException` - if `after` is null




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

