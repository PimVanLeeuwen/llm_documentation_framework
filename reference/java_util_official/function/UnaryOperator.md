

UnaryOperator (Java Platform SE 8 )






<!--
try {
if (location.href.indexOf('is-external=true') == -1) {
parent.document.title="UnaryOperator (Java Platform SE 8 )";
}
}
catch(err) {
}
//-->
var methods = {"i0":17};
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
java.util.functionInterface UnaryOperator<T>
Type Parameters:
`T` - the type of the operand and result of the operator

All Superinterfaces:
Function<T,T>

Functional Interface:
This is a functional interface and can therefore be used as the assignment target for a lambda expression or method reference.


```
@FunctionalInterface
public interface UnaryOperator<T>
extends Function<T,T>
```
Represents an operation on a single operand that produces a result of the
same type as its operand. This is a specialization of `Function` for
the case where the operand and result are of the same type.This is a functional interface
whose functional method is `Function.apply(Object)`.
Since:
1.8
See Also:
`Function`

### Method Summary

All Methods Static Methods Default Methods Modifier and TypeMethod and Description`static <T> UnaryOperator<T>``identity()`
Returns a unary operator that always returns its input argument.

### Methods inherited from interface java.util.function.Function

`andThen, apply, compose`

### Method Detail

#### identity

```
static <T> UnaryOperator<T> identity()
```
Returns a unary operator that always returns its input argument.
Specified by:
`identity` in interface `Function<T,T>`
Type Parameters:
`T` - the type of the input and output of the operator
Returns:
a unary operator that always returns its input argument




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

