

DoubleAccumulator (Java Platform SE 8 )














<!--
try {
if (location.href.indexOf('is-external=true') == -1) {
parent.document.title="DoubleAccumulator (Java Platform SE 8 )";
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
java.util.concurrent.atomicClass DoubleAccumulator
java.lang.Objectjava.lang.Numberjava.util.concurrent.atomic.DoubleAccumulator
All Implemented Interfaces:
Serializable


```
public class DoubleAccumulator
extends Number
implements Serializable
```
One or more variables that together maintain a running `double`
value updated using a supplied function. When updates (method
`accumulate(double)`) are contended across threads, the set of variables
may grow dynamically to reduce contention. Method `get()`
(or, equivalently, `doubleValue()`) returns the current value
across the variables maintaining updates.This class is usually preferable to alternatives when multiple
threads update a common value that is used for purposes such as
summary statistics that are frequently updated but less frequently
read.The supplied accumulator function should be side-effect-free,
since it may be re-applied when attempted updates fail due to
contention among threads. The function is applied with the current
value as its first argument, and the given update as the second
argument. For example, to maintain a running maximum value, you
could supply `Double::max` along with `Double.NEGATIVE_INFINITY` as the identity. The order of
accumulation within or across threads is not guaranteed. Thus, this
class may not be applicable if numerical stability is required,
especially when combining values of substantially different orders
of magnitude.Class `DoubleAdder` provides analogs of the functionality
of this class for the common special case of maintaining sums. The
call `new DoubleAdder()` is equivalent to `new
DoubleAccumulator((x, y) -> x + y, 0.0)`.This class extends `Number`, but does not define
methods such as `equals`, `hashCode` and `compareTo` because instances are expected to be mutated, and so are
not useful as collection keys.
Since:
1.8
See Also:
Serialized Form

### Constructor Summary

Constructors Constructor and Description`DoubleAccumulator(DoubleBinaryOperator accumulatorFunction,
double identity)`
Creates a new instance using the given accumulator function
and identity element.

### Method Summary

All Methods Instance Methods Concrete Methods Modifier and TypeMethod and Description`void``accumulate(double x)`
Updates with the given value.`double``doubleValue()`
Equivalent to `get()`.`float``floatValue()`
Returns the current value as a `float`
after a narrowing primitive conversion.`double``get()`
Returns the current value.`double``getThenReset()`
Equivalent in effect to `get()` followed by `reset()`.`int``intValue()`
Returns the current value as an `int`
after a narrowing primitive conversion.`long``longValue()`
Returns the current value as a `long`
after a narrowing primitive conversion.`void``reset()`
Resets variables maintaining updates to the identity value.`String``toString()`
Returns the String representation of the current value.

### Methods inherited from class java.lang.Number

`byteValue, shortValue`

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, wait, wait, wait`

### Constructor Detail

#### DoubleAccumulator

```
public DoubleAccumulator(DoubleBinaryOperator accumulatorFunction,
                         double identity)
```
Creates a new instance using the given accumulator function
and identity element.
Parameters:
`accumulatorFunction` - a side-effect-free function of two arguments
`identity` - identity (initial value) for the accumulator function

### Method Detail

#### accumulate

```
public void accumulate(double x)
```
Updates with the given value.
Parameters:
`x` - the value

#### get

```
public double get()
```
Returns the current value. The returned value is NOT
an atomic snapshot; invocation in the absence of concurrent
updates returns an accurate result, but concurrent updates that
occur while the value is being calculated might not be
incorporated.
Returns:
the current value

#### reset

```
public void reset()
```
Resets variables maintaining updates to the identity value.
This method may be a useful alternative to creating a new
updater, but is only effective if there are no concurrent
updates. Because this method is intrinsically racy, it should
only be used when it is known that no threads are concurrently
updating.

#### getThenReset

```
public double getThenReset()
```
Equivalent in effect to `get()` followed by `reset()`. This method may apply for example during quiescent
points between multithreaded computations. If there are
updates concurrent with this method, the returned value is
not guaranteed to be the final value occurring before
the reset.
Returns:
the value before reset

#### toString

```
public String toString()
```
Returns the String representation of the current value.
Overrides:
`toString` in class `Object`
Returns:
the String representation of the current value

#### doubleValue

```
public double doubleValue()
```
Equivalent to `get()`.
Specified by:
`doubleValue` in class `Number`
Returns:
the current value

#### longValue

```
public long longValue()
```
Returns the current value as a `long`
after a narrowing primitive conversion.
Specified by:
`longValue` in class `Number`
Returns:
the numeric value represented by this object after conversion
to type `long`.

#### intValue

```
public int intValue()
```
Returns the current value as an `int`
after a narrowing primitive conversion.
Specified by:
`intValue` in class `Number`
Returns:
the numeric value represented by this object after conversion
to type `int`.

#### floatValue

```
public float floatValue()
```
Returns the current value as a `float`
after a narrowing primitive conversion.
Specified by:
`floatValue` in class `Number`
Returns:
the numeric value represented by this object after conversion
to type `float`.




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

