

AtomicLongFieldUpdater (Java Platform SE 8 )






















<!--
try {
if (location.href.indexOf('is-external=true') == -1) {
parent.document.title="AtomicLongFieldUpdater (Java Platform SE 8 )";
}
}
catch(err) {
}
//-->
var methods = {"i0":10,"i1":10,"i2":6,"i3":10,"i4":6,"i5":10,"i6":10,"i7":10,"i8":10,"i9":10,"i10":10,"i11":10,"i12":6,"i13":9,"i14":6,"i15":10,"i16":6};
var tabs = {65535:["t0","All Methods"],1:["t1","Static Methods"],2:["t2","Instance Methods"],4:["t3","Abstract Methods"],8:["t4","Concrete Methods"]};
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
java.util.concurrent.atomicClass AtomicLongFieldUpdater<T>
java.lang.Objectjava.util.concurrent.atomic.AtomicLongFieldUpdater<T>
Type Parameters:
`T` - The type of the object holding the updatable field


```
public abstract class AtomicLongFieldUpdater<T>
extends Object
```
A reflection-based utility that enables atomic updates to
designated `volatile long` fields of designated classes.
This class is designed for use in atomic data structures in which
several fields of the same node are independently subject to atomic
updates.Note that the guarantees of the `compareAndSet`
method in this class are weaker than in other atomic classes.
Because this class cannot ensure that all uses of the field
are appropriate for purposes of atomic access, it can
guarantee atomicity only with respect to other invocations of
`compareAndSet` and `set` on the same updater.
Since:
1.5

### Constructor Summary

Constructors ModifierConstructor and Description`protected` `AtomicLongFieldUpdater()`
Protected do-nothing constructor for use by subclasses.

### Method Summary

All Methods Static Methods Instance Methods Abstract Methods Concrete Methods Modifier and TypeMethod and Description`long``accumulateAndGet(T obj,
long x,
LongBinaryOperator accumulatorFunction)`
Atomically updates the field of the given object managed by this
updater with the results of applying the given function to the
current and given values, returning the updated value.`long``addAndGet(T obj,
long delta)`
Atomically adds the given value to the current value of the field of
the given object managed by this updater.`abstract boolean``compareAndSet(T obj,
long expect,
long update)`
Atomically sets the field of the given object managed by this updater
to the given updated value if the current value `==` the
expected value.`long``decrementAndGet(T obj)`
Atomically decrements by one the current value of the field of the
given object managed by this updater.`abstract long``get(T obj)`
Gets the current value held in the field of the given object managed
by this updater.`long``getAndAccumulate(T obj,
long x,
LongBinaryOperator accumulatorFunction)`
Atomically updates the field of the given object managed by this
updater with the results of applying the given function to the
current and given values, returning the previous value.`long``getAndAdd(T obj,
long delta)`
Atomically adds the given value to the current value of the field of
the given object managed by this updater.`long``getAndDecrement(T obj)`
Atomically decrements by one the current value of the field of the
given object managed by this updater.`long``getAndIncrement(T obj)`
Atomically increments by one the current value of the field of the
given object managed by this updater.`long``getAndSet(T obj,
long newValue)`
Atomically sets the field of the given object managed by this updater
to the given value and returns the old value.`long``getAndUpdate(T obj,
LongUnaryOperator updateFunction)`
Atomically updates the field of the given object managed by this updater
with the results of applying the given function, returning the previous
value.`long``incrementAndGet(T obj)`
Atomically increments by one the current value of the field of the
given object managed by this updater.`abstract void``lazySet(T obj,
long newValue)`
Eventually sets the field of the given object managed by this
updater to the given updated value.`static <U> AtomicLongFieldUpdater<U>``newUpdater(Class<U> tclass,
String fieldName)`
Creates and returns an updater for objects with the given field.`abstract void``set(T obj,
long newValue)`
Sets the field of the given object managed by this updater to the
given updated value.`long``updateAndGet(T obj,
LongUnaryOperator updateFunction)`
Atomically updates the field of the given object managed by this updater
with the results of applying the given function, returning the updated
value.`abstract boolean``weakCompareAndSet(T obj,
long expect,
long update)`
Atomically sets the field of the given object managed by this updater
to the given updated value if the current value `==` the
expected value.

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

### Constructor Detail

#### AtomicLongFieldUpdater

```
protected AtomicLongFieldUpdater()
```
Protected do-nothing constructor for use by subclasses.

### Method Detail

#### newUpdater

```
public static <U> AtomicLongFieldUpdater<U> newUpdater(Class<U> tclass,
                                                       String fieldName)
```
Creates and returns an updater for objects with the given field.
The Class argument is needed to check that reflective types and
generic types match.
Type Parameters:
`U` - the type of instances of tclass
Parameters:
`tclass` - the class of the objects holding the field
`fieldName` - the name of the field to be updated
Returns:
the updater
Throws:
`IllegalArgumentException` - if the field is not a
volatile long type
`RuntimeException` - with a nested reflection-based
exception if the class does not hold field or is the wrong type,
or the field is inaccessible to the caller according to Java language
access control

#### compareAndSet

```
public abstract boolean compareAndSet(T obj,
                                      long expect,
                                      long update)
```
Atomically sets the field of the given object managed by this updater
to the given updated value if the current value `==` the
expected value. This method is guaranteed to be atomic with respect to
other calls to `compareAndSet` and `set`, but not
necessarily with respect to other changes in the field.
Parameters:
`obj` - An object whose field to conditionally set
`expect` - the expected value
`update` - the new value
Returns:
`true` if successful
Throws:
`ClassCastException` - if `obj` is not an instance
of the class possessing the field established in the constructor

#### weakCompareAndSet

```
public abstract boolean weakCompareAndSet(T obj,
                                          long expect,
                                          long update)
```
Atomically sets the field of the given object managed by this updater
to the given updated value if the current value `==` the
expected value. This method is guaranteed to be atomic with respect to
other calls to `compareAndSet` and `set`, but not
necessarily with respect to other changes in the field.May fail
spuriously and does not provide ordering guarantees, so is
only rarely an appropriate alternative to `compareAndSet`.
Parameters:
`obj` - An object whose field to conditionally set
`expect` - the expected value
`update` - the new value
Returns:
`true` if successful
Throws:
`ClassCastException` - if `obj` is not an instance
of the class possessing the field established in the constructor

#### set

```
public abstract void set(T obj,
                         long newValue)
```
Sets the field of the given object managed by this updater to the
given updated value. This operation is guaranteed to act as a volatile
store with respect to subsequent invocations of `compareAndSet`.
Parameters:
`obj` - An object whose field to set
`newValue` - the new value

#### lazySet

```
public abstract void lazySet(T obj,
                             long newValue)
```
Eventually sets the field of the given object managed by this
updater to the given updated value.
Parameters:
`obj` - An object whose field to set
`newValue` - the new value
Since:
1.6

#### get

```
public abstract long get(T obj)
```
Gets the current value held in the field of the given object managed
by this updater.
Parameters:
`obj` - An object whose field to get
Returns:
the current value

#### getAndSet

```
public long getAndSet(T obj,
                      long newValue)
```
Atomically sets the field of the given object managed by this updater
to the given value and returns the old value.
Parameters:
`obj` - An object whose field to get and set
`newValue` - the new value
Returns:
the previous value

#### getAndIncrement

```
public long getAndIncrement(T obj)
```
Atomically increments by one the current value of the field of the
given object managed by this updater.
Parameters:
`obj` - An object whose field to get and set
Returns:
the previous value

#### getAndDecrement

```
public long getAndDecrement(T obj)
```
Atomically decrements by one the current value of the field of the
given object managed by this updater.
Parameters:
`obj` - An object whose field to get and set
Returns:
the previous value

#### getAndAdd

```
public long getAndAdd(T obj,
                      long delta)
```
Atomically adds the given value to the current value of the field of
the given object managed by this updater.
Parameters:
`obj` - An object whose field to get and set
`delta` - the value to add
Returns:
the previous value

#### incrementAndGet

```
public long incrementAndGet(T obj)
```
Atomically increments by one the current value of the field of the
given object managed by this updater.
Parameters:
`obj` - An object whose field to get and set
Returns:
the updated value

#### decrementAndGet

```
public long decrementAndGet(T obj)
```
Atomically decrements by one the current value of the field of the
given object managed by this updater.
Parameters:
`obj` - An object whose field to get and set
Returns:
the updated value

#### addAndGet

```
public long addAndGet(T obj,
                      long delta)
```
Atomically adds the given value to the current value of the field of
the given object managed by this updater.
Parameters:
`obj` - An object whose field to get and set
`delta` - the value to add
Returns:
the updated value

#### getAndUpdate

```
public final long getAndUpdate(T obj,
                               LongUnaryOperator updateFunction)
```
Atomically updates the field of the given object managed by this updater
with the results of applying the given function, returning the previous
value. The function should be side-effect-free, since it may be
re-applied when attempted updates fail due to contention among threads.
Parameters:
`obj` - An object whose field to get and set
`updateFunction` - a side-effect-free function
Returns:
the previous value
Since:
1.8

#### updateAndGet

```
public final long updateAndGet(T obj,
                               LongUnaryOperator updateFunction)
```
Atomically updates the field of the given object managed by this updater
with the results of applying the given function, returning the updated
value. The function should be side-effect-free, since it may be
re-applied when attempted updates fail due to contention among threads.
Parameters:
`obj` - An object whose field to get and set
`updateFunction` - a side-effect-free function
Returns:
the updated value
Since:
1.8

#### getAndAccumulate

```
public final long getAndAccumulate(T obj,
                                   long x,
                                   LongBinaryOperator accumulatorFunction)
```
Atomically updates the field of the given object managed by this
updater with the results of applying the given function to the
current and given values, returning the previous value. The
function should be side-effect-free, since it may be re-applied
when attempted updates fail due to contention among threads. The
function is applied with the current value as its first argument,
and the given update as the second argument.
Parameters:
`obj` - An object whose field to get and set
`x` - the update value
`accumulatorFunction` - a side-effect-free function of two arguments
Returns:
the previous value
Since:
1.8

#### accumulateAndGet

```
public final long accumulateAndGet(T obj,
                                   long x,
                                   LongBinaryOperator accumulatorFunction)
```
Atomically updates the field of the given object managed by this
updater with the results of applying the given function to the
current and given values, returning the updated value. The
function should be side-effect-free, since it may be re-applied
when attempted updates fail due to contention among threads. The
function is applied with the current value as its first argument,
and the given update as the second argument.
Parameters:
`obj` - An object whose field to get and set
`x` - the update value
`accumulatorFunction` - a side-effect-free function of two arguments
Returns:
the updated value
Since:
1.8




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

