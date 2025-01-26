

LongStream.Builder (Java Platform SE 8 )








<!--
try {
if (location.href.indexOf('is-external=true') == -1) {
parent.document.title="LongStream.Builder (Java Platform SE 8 )";
}
}
catch(err) {
}
//-->
var methods = {"i0":6,"i1":18,"i2":6};
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
java.util.streamInterface LongStream.Builder
All Superinterfaces:
LongConsumer

Enclosing interface:
LongStream


```
public static interface LongStream.Builder
extends LongConsumer
```
A mutable builder for a `LongStream`.A stream builder has a lifecycle, which starts in a building
phase, during which elements can be added, and then transitions to a built
phase, after which elements may not be added. The built phase begins
begins when the `build()` method is called, which creates an
ordered stream whose elements are the elements that were added to the
stream builder, in the order they were added.
Since:
1.8
See Also:
`LongStream.builder()`

### Method Summary

All Methods Instance Methods Abstract Methods Default Methods Modifier and TypeMethod and Description`void``accept(long t)`
Adds an element to the stream being built.`default LongStream.Builder``add(long t)`
Adds an element to the stream being built.`LongStream``build()`
Builds the stream, transitioning this builder to the built state.

### Methods inherited from interface java.util.function.LongConsumer

`andThen`

### Method Detail

#### accept

```
void accept(long t)
```
Adds an element to the stream being built.
Specified by:
`accept` in interface `LongConsumer`
Parameters:
`t` - the input argument
Throws:
`IllegalStateException` - if the builder has already transitioned
to the built state

#### add

```
default LongStream.Builder add(long t)
```
Adds an element to the stream being built.
Implementation Requirements:
The default implementation behaves as if:
```

     accept(t)
     return this;
 
```

Parameters:
`t` - the element to add
Returns:
`this` builder
Throws:
`IllegalStateException` - if the builder has already transitioned
to the built state

#### build

```
LongStream build()
```
Builds the stream, transitioning this builder to the built state.
An `IllegalStateException` is thrown if there are further
attempts to operate on the builder after it has entered the built
state.
Returns:
the built stream
Throws:
`IllegalStateException` - if the builder has already transitioned
to the built state




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

