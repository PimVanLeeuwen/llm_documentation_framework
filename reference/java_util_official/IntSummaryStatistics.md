

IntSummaryStatistics (Java Platform SE 8 )













<!--
try {
if (location.href.indexOf('is-external=true') == -1) {
parent.document.title="IntSummaryStatistics (Java Platform SE 8 )";
}
}
catch(err) {
}
//-->
var methods = {"i0":10,"i1":10,"i2":10,"i3":10,"i4":10,"i5":10,"i6":10,"i7":10};
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
java.utilClass IntSummaryStatistics
java.lang.Objectjava.util.IntSummaryStatistics
All Implemented Interfaces:
IntConsumer


```
public class IntSummaryStatistics
extends Object
implements IntConsumer
```
A state object for collecting statistics such as count, min, max, sum, and
average.This class is designed to work with (though does not require)
streams. For example, you can compute
summary statistics on a stream of ints with:
```
 
 IntSummaryStatistics stats = intStream.collect(IntSummaryStatistics::new,
                                                IntSummaryStatistics::accept,
                                                IntSummaryStatistics::combine);
 
```
`IntSummaryStatistics` can be used as a
reduction
target for a stream. For example:
```
 
 IntSummaryStatistics stats = people.stream()
                                    .collect(Collectors.summarizingInt(Person::getDependents));

```
This computes, in a single pass, the count of people, as well as the minimum,
maximum, sum, and average of their number of dependents.
Implementation Note:
This implementation is not thread safe. However, it is safe to use
`Collectors.toIntStatistics()` on a parallel stream, because the parallel
implementation of `Stream.collect()`
provides the necessary partitioning, isolation, and merging of results for
safe and efficient parallel execution.This implementation does not check for overflow of the sum.
Since:
1.8

### Constructor Summary

Constructors Constructor and Description`IntSummaryStatistics()`
Construct an empty instance with zero count, zero sum,
`Integer.MAX_VALUE` min, `Integer.MIN_VALUE` max and zero
average.

### Method Summary

All Methods Instance Methods Concrete Methods Modifier and TypeMethod and Description`void``accept(int value)`
Records a new value into the summary information`void``combine(IntSummaryStatistics other)`
Combines the state of another `IntSummaryStatistics` into this one.`double``getAverage()`
Returns the arithmetic mean of values recorded, or zero if no values have been
recorded.`long``getCount()`
Returns the count of values recorded.`int``getMax()`
Returns the maximum value recorded, or `Integer.MIN_VALUE` if no
values have been recorded.`int``getMin()`
Returns the minimum value recorded, or `Integer.MAX_VALUE` if no
values have been recorded.`long``getSum()`
Returns the sum of values recorded, or zero if no values have been
recorded.`String``toString()`
Returns a string representation of the object.

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, wait, wait, wait`

### Methods inherited from interface java.util.function.IntConsumer

`andThen`

### Constructor Detail

#### IntSummaryStatistics

```
public IntSummaryStatistics()
```
Construct an empty instance with zero count, zero sum,
`Integer.MAX_VALUE` min, `Integer.MIN_VALUE` max and zero
average.

### Method Detail

#### accept

```
public void accept(int value)
```
Records a new value into the summary information
Specified by:
`accept` in interface `IntConsumer`
Parameters:
`value` - the input value

#### combine

```
public void combine(IntSummaryStatistics other)
```
Combines the state of another `IntSummaryStatistics` into this one.
Parameters:
`other` - another `IntSummaryStatistics`
Throws:
`NullPointerException` - if `other` is null

#### getCount

```
public final long getCount()
```
Returns the count of values recorded.
Returns:
the count of values

#### getSum

```
public final long getSum()
```
Returns the sum of values recorded, or zero if no values have been
recorded.
Returns:
the sum of values, or zero if none

#### getMin

```
public final int getMin()
```
Returns the minimum value recorded, or `Integer.MAX_VALUE` if no
values have been recorded.
Returns:
the minimum value, or `Integer.MAX_VALUE` if none

#### getMax

```
public final int getMax()
```
Returns the maximum value recorded, or `Integer.MIN_VALUE` if no
values have been recorded.
Returns:
the maximum value, or `Integer.MIN_VALUE` if none

#### getAverage

```
public final double getAverage()
```
Returns the arithmetic mean of values recorded, or zero if no values have been
recorded.
Returns:
the arithmetic mean of values, or zero if none

#### toString

```
public String toString()
```
Description copied from class: `Object`
Returns a string representation of the object. In general, the
`toString` method returns a string that
"textually represents" this object. The result should
be a concise but informative representation that is easy for a
person to read.
It is recommended that all subclasses override this method.The `toString` method for class `Object`
returns a string consisting of the name of the class of which the
object is an instance, the at-sign character ``@`', and
the unsigned hexadecimal representation of the hash code of the
object. In other words, this method returns a string equal to the
value of:
```

 getClass().getName() + '@' + Integer.toHexString(hashCode())
 
```

Overrides:
`toString` in class `Object`
Returns:
a string representation of the object.




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

