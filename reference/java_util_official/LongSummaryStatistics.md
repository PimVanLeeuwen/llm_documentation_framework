

LongSummaryStatistics (Java Platform SE 8 )













<!--
try {
if (location.href.indexOf('is-external=true') == -1) {
parent.document.title="LongSummaryStatistics (Java Platform SE 8 )";
}
}
catch(err) {
}
//-->
var methods = {"i0":10,"i1":10,"i2":10,"i3":10,"i4":10,"i5":10,"i6":10,"i7":10,"i8":10};
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
java.utilClass LongSummaryStatistics
java.lang.Objectjava.util.LongSummaryStatistics
All Implemented Interfaces:
IntConsumer, LongConsumer


```
public class LongSummaryStatistics
extends Object
implements LongConsumer, IntConsumer
```
A state object for collecting statistics such as count, min, max, sum, and
average.This class is designed to work with (though does not require)
streams. For example, you can compute
summary statistics on a stream of longs with:
```
 
 LongSummaryStatistics stats = longStream.collect(LongSummaryStatistics::new,
                                                  LongSummaryStatistics::accept,
                                                  LongSummaryStatistics::combine);
 
```
`LongSummaryStatistics` can be used as a
Stream.collect(Collector) reduction}
target for a stream. For example:
```
 
 LongSummaryStatistics stats = people.stream()
                                     .collect(Collectors.summarizingLong(Person::getAge));

```
This computes, in a single pass, the count of people, as well as the minimum,
maximum, sum, and average of their ages.
Implementation Note:
This implementation is not thread safe. However, it is safe to use
`Collectors.toLongStatistics()` on a parallel stream, because the parallel
implementation of `Stream.collect()`
provides the necessary partitioning, isolation, and merging of results for
safe and efficient parallel execution.This implementation does not check for overflow of the sum.
Since:
1.8

### Constructor Summary

Constructors Constructor and Description`LongSummaryStatistics()`
Construct an empty instance with zero count, zero sum,
`Long.MAX_VALUE` min, `Long.MIN_VALUE` max and zero
average.

### Method Summary

All Methods Instance Methods Concrete Methods Modifier and TypeMethod and Description`void``accept(int value)`
Records a new `int` value into the summary information.`void``accept(long value)`
Records a new `long` value into the summary information.`void``combine(LongSummaryStatistics other)`
Combines the state of another `LongSummaryStatistics` into this
one.`double``getAverage()`
Returns the arithmetic mean of values recorded, or zero if no values have been
recorded.`long``getCount()`
Returns the count of values recorded.`long``getMax()`
Returns the maximum value recorded, or `Long.MIN_VALUE` if no
values have been recorded`long``getMin()`
Returns the minimum value recorded, or `Long.MAX_VALUE` if no
values have been recorded.`long``getSum()`
Returns the sum of values recorded, or zero if no values have been
recorded.`String``toString()`
Returns a string representation of the object.

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, wait, wait, wait`

### Methods inherited from interface java.util.function.LongConsumer

`andThen`

### Methods inherited from interface java.util.function.IntConsumer

`andThen`

### Constructor Detail

#### LongSummaryStatistics

```
public LongSummaryStatistics()
```
Construct an empty instance with zero count, zero sum,
`Long.MAX_VALUE` min, `Long.MIN_VALUE` max and zero
average.

### Method Detail

#### accept

```
public void accept(int value)
```
Records a new `int` value into the summary information.
Specified by:
`accept` in interface `IntConsumer`
Parameters:
`value` - the input value

#### accept

```
public void accept(long value)
```
Records a new `long` value into the summary information.
Specified by:
`accept` in interface `LongConsumer`
Parameters:
`value` - the input value

#### combine

```
public void combine(LongSummaryStatistics other)
```
Combines the state of another `LongSummaryStatistics` into this
one.
Parameters:
`other` - another `LongSummaryStatistics`
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
public final long getMin()
```
Returns the minimum value recorded, or `Long.MAX_VALUE` if no
values have been recorded.
Returns:
the minimum value, or `Long.MAX_VALUE` if none

#### getMax

```
public final long getMax()
```
Returns the maximum value recorded, or `Long.MIN_VALUE` if no
values have been recorded
Returns:
the maximum value, or `Long.MIN_VALUE` if none

#### getAverage

```
public final double getAverage()
```
Returns the arithmetic mean of values recorded, or zero if no values have been
recorded.
Returns:
The arithmetic mean of values, or zero if none

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

