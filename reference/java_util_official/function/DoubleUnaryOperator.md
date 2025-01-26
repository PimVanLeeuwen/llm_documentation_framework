

DoubleUnaryOperator (Java Platform SE 8 )









<!--
try {
if (location.href.indexOf('is-external=true') == -1) {
parent.document.title="DoubleUnaryOperator (Java Platform SE 8 )";
}
}
catch(err) {
}
//-->
var methods = {"i0":18,"i1":6,"i2":18,"i3":17};
var tabs = {65535:["t0","All Methods"],1:["t1","Static Methods"],2:["t2","Instance Methods"],4:["t3","Abstract Methods"],16:["t5","Default Methods"]};
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
java.util.functionInterface DoubleUnaryOperator
Functional Interface:
This is a functional interface and can therefore be used as the assignment target for a lambda expression or method reference.


```
@FunctionalInterface
public interface DoubleUnaryOperator
```
Represents an operation on a single `double`-valued operand that produces
a `double`-valued result. This is the primitive type specialization of
`UnaryOperator` for `double`.This is a functional interface
whose functional method is `applyAsDouble(double)`.
Since:
1.8
See Also:
`UnaryOperator`

### Method Summary

All Methods Static Methods Instance Methods Abstract Methods Default Methods Modifier and TypeMethod and Description`default DoubleUnaryOperator``andThen(DoubleUnaryOperator after)`
Returns a composed operator that first applies this operator to
its input, and then applies the `after` operator to the result.`double``applyAsDouble(double operand)`
Applies this operator to the given operand.`default DoubleUnaryOperator``compose(DoubleUnaryOperator before)`
Returns a composed operator that first applies the `before`
operator to its input, and then applies this operator to the result.`static DoubleUnaryOperator``identity()`
Returns a unary operator that always returns its input argument.

### Method Detail

#### applyAsDouble

```
double applyAsDouble(double operand)
```
Applies this operator to the given operand.
Parameters:
`operand` - the operand
Returns:
the operator result

#### compose

```
default DoubleUnaryOperator compose(DoubleUnaryOperator before)
```
Returns a composed operator that first applies the `before`
operator to its input, and then applies this operator to the result.
If evaluation of either operator throws an exception, it is relayed to
the caller of the composed operator.
Parameters:
`before` - the operator to apply before this operator is applied
Returns:
a composed operator that first applies the `before`
operator and then applies this operator
Throws:
`NullPointerException` - if before is null
See Also:
`andThen(DoubleUnaryOperator)`

#### andThen

```
default DoubleUnaryOperator andThen(DoubleUnaryOperator after)
```
Returns a composed operator that first applies this operator to
its input, and then applies the `after` operator to the result.
If evaluation of either operator throws an exception, it is relayed to
the caller of the composed operator.
Parameters:
`after` - the operator to apply after this operator is applied
Returns:
a composed operator that first applies this operator and then
applies the `after` operator
Throws:
`NullPointerException` - if after is null
See Also:
`compose(DoubleUnaryOperator)`

#### identity

```
static DoubleUnaryOperator identity()
```
Returns a unary operator that always returns its input argument.
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

