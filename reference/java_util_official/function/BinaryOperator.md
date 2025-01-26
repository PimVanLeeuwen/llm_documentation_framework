

BinaryOperator (Java Platform SE 8 )







<!--
try {
if (location.href.indexOf('is-external=true') == -1) {
parent.document.title="BinaryOperator (Java Platform SE 8 )";
}
}
catch(err) {
}
//-->
var methods = {"i0":17,"i1":17};
var tabs = {65535:["t0","All Methods"],1:["t1","Static Methods"],16:["t5","Default Methods"]};
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
java.util.functionInterface BinaryOperator<T>
Type Parameters:
`T` - the type of the operands and result of the operator

All Superinterfaces:
BiFunction<T,T,T>

Functional Interface:
This is a functional interface and can therefore be used as the assignment target for a lambda expression or method reference.


```
@FunctionalInterface
public interface BinaryOperator<T>
extends BiFunction<T,T,T>
```
Represents an operation upon two operands of the same type, producing a result
of the same type as the operands. This is a specialization of
`BiFunction` for the case where the operands and the result are all of
the same type.This is a functional interface
whose functional method is `BiFunction.apply(Object, Object)`.
Since:
1.8
See Also:
`BiFunction`,
`UnaryOperator`

### Method Summary

All Methods Static Methods Default Methods Modifier and TypeMethod and Description`static <T> BinaryOperator<T>``maxBy(Comparator<? super T> comparator)`
Returns a `BinaryOperator` which returns the greater of two elements
according to the specified `Comparator`.`static <T> BinaryOperator<T>``minBy(Comparator<? super T> comparator)`
Returns a `BinaryOperator` which returns the lesser of two elements
according to the specified `Comparator`.

### Methods inherited from interface java.util.function.BiFunction

`andThen, apply`

### Method Detail

#### minBy

```
static <T> BinaryOperator<T> minBy(Comparator<? super T> comparator)
```
Returns a `BinaryOperator` which returns the lesser of two elements
according to the specified `Comparator`.
Type Parameters:
`T` - the type of the input arguments of the comparator
Parameters:
`comparator` - a `Comparator` for comparing the two values
Returns:
a `BinaryOperator` which returns the lesser of its operands,
according to the supplied `Comparator`
Throws:
`NullPointerException` - if the argument is null

#### maxBy

```
static <T> BinaryOperator<T> maxBy(Comparator<? super T> comparator)
```
Returns a `BinaryOperator` which returns the greater of two elements
according to the specified `Comparator`.
Type Parameters:
`T` - the type of the input arguments of the comparator
Parameters:
`comparator` - a `Comparator` for comparing the two values
Returns:
a `BinaryOperator` which returns the greater of its operands,
according to the supplied `Comparator`
Throws:
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


Summary:Nested |Field |Constr |MethodDetail:Field |Constr |Method


 Submit a bug or feature For further API reference and developer documentation, see Java SE Documentation. That documentation contains more detailed, developer-targeted descriptions, with conceptual overviews, definitions of terms, workarounds, and working code examples. Copyright © 1993, 2025, Oracle and/or its affiliates. All rights reserved. Use is subject to license terms. Also see the documentation redistribution policy. 

