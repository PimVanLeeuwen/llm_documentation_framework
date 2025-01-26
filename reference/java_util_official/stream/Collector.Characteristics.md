

Collector.Characteristics (Java Platform SE 8 )







<!--
try {
if (location.href.indexOf('is-external=true') == -1) {
parent.document.title="Collector.Characteristics (Java Platform SE 8 )";
}
}
catch(err) {
}
//-->
var methods = {"i0":9,"i1":9};
var tabs = {65535:["t0","All Methods"],1:["t1","Static Methods"],8:["t4","Concrete Methods"]};
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


Summary:Nested |Enum Constants |Field |MethodDetail:Enum Constants |Field |Method




compact1, compact2, compact3
java.util.streamEnum Collector.Characteristics
java.lang.Objectjava.lang.Enum<Collector.Characteristics>java.util.stream.Collector.Characteristics
All Implemented Interfaces:
Serializable, Comparable<Collector.Characteristics>

Enclosing interface:
Collector<T,A,R>


```
public static enum Collector.Characteristics
extends Enum<Collector.Characteristics>
```
Characteristics indicating properties of a `Collector`, which can
be used to optimize reduction implementations.

### Enum Constant Summary

Enum Constants Enum Constant and Description`CONCURRENT`
Indicates that this collector is concurrent, meaning that
the result container can support the accumulator function being
called concurrently with the same result container from multiple
threads.`IDENTITY_FINISH`
Indicates that the finisher function is the identity function and
can be elided.`UNORDERED`
Indicates that the collection operation does not commit to preserving
the encounter order of input elements.

### Method Summary

All Methods Static Methods Concrete Methods Modifier and TypeMethod and Description`static Collector.Characteristics``valueOf(String name)`
Returns the enum constant of this type with the specified name.`static Collector.Characteristics[]``values()`
Returns an array containing the constants of this enum type, in
the order they are declared.

### Methods inherited from class java.lang.Enum

`clone, compareTo, equals, finalize, getDeclaringClass, hashCode, name, ordinal, toString, valueOf`

### Methods inherited from class java.lang.Object

`getClass, notify, notifyAll, wait, wait, wait`

### Enum Constant Detail

#### CONCURRENT

```
public static final Collector.Characteristics CONCURRENT
```
Indicates that this collector is concurrent, meaning that
the result container can support the accumulator function being
called concurrently with the same result container from multiple
threads.If a `CONCURRENT` collector is not also `UNORDERED`,
then it should only be evaluated concurrently if applied to an
unordered data source.

#### UNORDERED

```
public static final Collector.Characteristics UNORDERED
```
Indicates that the collection operation does not commit to preserving
the encounter order of input elements. (This might be true if the
result container has no intrinsic order, such as a `Set`.)

#### IDENTITY\_FINISH

```
public static final Collector.Characteristics IDENTITY_FINISH
```
Indicates that the finisher function is the identity function and
can be elided. If set, it must be the case that an unchecked cast
from A to R will succeed.

### Method Detail

#### values

```
public static Collector.Characteristics[] values()
```
Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:
```

for (Collector.Characteristics c : Collector.Characteristics.values())
    System.out.println(c);

```

Returns:
an array containing the constants of this enum type, in the order they are declared

#### valueOf

```
public static Collector.Characteristics valueOf(String name)
```
Returns the enum constant of this type with the specified name.
The string must match exactly an identifier used to declare an
enum constant in this type. (Extraneous whitespace characters are
not permitted.)
Parameters:
`name` - the name of the enum constant to be returned.
Returns:
the enum constant with the specified name
Throws:
`IllegalArgumentException` - if this enum type has no constant with the specified name
`NullPointerException` - if the argument is null




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


Summary:Nested |Enum Constants |Field |MethodDetail:Enum Constants |Field |Method


 Submit a bug or feature For further API reference and developer documentation, see Java SE Documentation. That documentation contains more detailed, developer-targeted descriptions, with conceptual overviews, definitions of terms, workarounds, and working code examples. Copyright © 1993, 2025, Oracle and/or its affiliates. All rights reserved. Use is subject to license terms. Also see the documentation redistribution policy. 

