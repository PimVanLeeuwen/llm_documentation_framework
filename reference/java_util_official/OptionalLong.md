

OptionalLong (Java Platform SE 8 )
















<!--
try {
if (location.href.indexOf('is-external=true') == -1) {
parent.document.title="OptionalLong (Java Platform SE 8 )";
}
}
catch(err) {
}
//-->
var methods = {"i0":9,"i1":10,"i2":10,"i3":10,"i4":10,"i5":10,"i6":9,"i7":10,"i8":10,"i9":10,"i10":10};
var tabs = {65535:["t0","All Methods"],1:["t1","Static Methods"],2:["t2","Instance Methods"],8:["t4","Concrete Methods"]};
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
java.utilClass OptionalLong
java.lang.Objectjava.util.OptionalLong
```
public final class OptionalLong
extends Object
```
A container object which may or may not contain a `long` value.
If a value is present, `isPresent()` will return `true` and
`getAsLong()` will return the value.Additional methods that depend on the presence or absence of a contained
value are provided, such as `orElse()`
(return a default value if value not present) and
`ifPresent()` (execute a block
of code if the value is present).This is a value-based
class; use of identity-sensitive operations (including reference equality
(`==`), identity hash code, or synchronization) on instances of
`OptionalLong` may have unpredictable results and should be avoided.
Since:
1.8

### Method Summary

All Methods Static Methods Instance Methods Concrete Methods Modifier and TypeMethod and Description`static OptionalLong``empty()`
Returns an empty `OptionalLong` instance.`boolean``equals(Object obj)`
Indicates whether some other object is "equal to" this OptionalLong.`long``getAsLong()`
If a value is present in this `OptionalLong`, returns the value,
otherwise throws `NoSuchElementException`.`int``hashCode()`
Returns the hash code value of the present value, if any, or 0 (zero) if
no value is present.`void``ifPresent(LongConsumer consumer)`
Have the specified consumer accept the value if a value is present,
otherwise do nothing.`boolean``isPresent()`
Return `true` if there is a value present, otherwise `false`.`static OptionalLong``of(long value)`
Return an `OptionalLong` with the specified value present.`long``orElse(long other)`
Return the value if present, otherwise return `other`.`long``orElseGet(LongSupplier other)`
Return the value if present, otherwise invoke `other` and return
the result of that invocation.`<X extends Throwable>long``orElseThrow(Supplier<X> exceptionSupplier)`
Return the contained value, if present, otherwise throw an exception
to be created by the provided supplier.`String``toString()`
Returns a string representation of the object.

### Methods inherited from class java.lang.Object

`clone, finalize, getClass, notify, notifyAll, wait, wait, wait`

### Method Detail

#### empty

```
public static OptionalLong empty()
```
Returns an empty `OptionalLong` instance. No value is present for this
OptionalLong.
API Note:
Though it may be tempting to do so, avoid testing if an object
is empty by comparing with `==` against instances returned by
`Option.empty()`. There is no guarantee that it is a singleton.
Instead, use `isPresent()`.
Returns:
an empty `OptionalLong`.

#### of

```
public static OptionalLong of(long value)
```
Return an `OptionalLong` with the specified value present.
Parameters:
`value` - the value to be present
Returns:
an `OptionalLong` with the value present

#### getAsLong

```
public long getAsLong()
```
If a value is present in this `OptionalLong`, returns the value,
otherwise throws `NoSuchElementException`.
Returns:
the value held by this `OptionalLong`
Throws:
`NoSuchElementException` - if there is no value present
See Also:
`isPresent()`

#### isPresent

```
public boolean isPresent()
```
Return `true` if there is a value present, otherwise `false`.
Returns:
`true` if there is a value present, otherwise `false`

#### ifPresent

```
public void ifPresent(LongConsumer consumer)
```
Have the specified consumer accept the value if a value is present,
otherwise do nothing.
Parameters:
`consumer` - block to be executed if a value is present
Throws:
`NullPointerException` - if value is present and `consumer` is
null

#### orElse

```
public long orElse(long other)
```
Return the value if present, otherwise return `other`.
Parameters:
`other` - the value to be returned if there is no value present
Returns:
the value, if present, otherwise `other`

#### orElseGet

```
public long orElseGet(LongSupplier other)
```
Return the value if present, otherwise invoke `other` and return
the result of that invocation.
Parameters:
`other` - a `LongSupplier` whose result is returned if no value
is present
Returns:
the value if present otherwise the result of `other.getAsLong()`
Throws:
`NullPointerException` - if value is not present and `other` is
null

#### orElseThrow

```
public <X extends Throwable> long orElseThrow(Supplier<X> exceptionSupplier)
                                       throws X
```
Return the contained value, if present, otherwise throw an exception
to be created by the provided supplier.
API Note:
A method reference to the exception constructor with an empty
argument list can be used as the supplier. For example,
`IllegalStateException::new`
Type Parameters:
`X` - Type of the exception to be thrown
Parameters:
`exceptionSupplier` - The supplier which will return the exception to
be thrown
Returns:
the present value
Throws:
`X` - if there is no value present
`NullPointerException` - if no value is present and
`exceptionSupplier` is null
`X extends Throwable`

#### equals

```
public boolean equals(Object obj)
```
Indicates whether some other object is "equal to" this OptionalLong. The
other object is considered equal if:it is also an `OptionalLong` and;both instances have no value present or;the present values are "equal to" each other via `==`.
Overrides:
`equals` in class `Object`
Parameters:
`obj` - an object to be tested for equality
Returns:
{code true} if the other object is "equal to" this object
otherwise `false`
See Also:
`Object.hashCode()`,
`HashMap`

#### hashCode

```
public int hashCode()
```
Returns the hash code value of the present value, if any, or 0 (zero) if
no value is present.
Overrides:
`hashCode` in class `Object`
Returns:
hash code value of the present value or 0 if no value is present
See Also:
`Object.equals(java.lang.Object)`,
`System.identityHashCode(java.lang.Object)`

#### toString

```
public String toString()
```
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
Returns a non-empty string representation of this object suitable for
debugging. The exact presentation format is unspecified and may vary
between implementations and versions.
Overrides:
`toString` in class `Object`
Implementation Requirements:
If a value is present the result must include its string
representation in the result. Empty and present instances must be
unambiguously differentiable.
Returns:
the string representation of this instance




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

