

BiPredicate (Java Platform SE 8 )









<!--
try {
if (location.href.indexOf('is-external=true') == -1) {
parent.document.title="BiPredicate (Java Platform SE 8 )";
}
}
catch(err) {
}
//-->
var methods = {"i0":18,"i1":18,"i2":18,"i3":6};
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
java.util.functionInterface BiPredicate<T,U>
Type Parameters:
`T` - the type of the first argument to the predicate
`U` - the type of the second argument the predicate

Functional Interface:
This is a functional interface and can therefore be used as the assignment target for a lambda expression or method reference.


```
@FunctionalInterface
public interface BiPredicate<T,U>
```
Represents a predicate (boolean-valued function) of two arguments. This is
the two-arity specialization of `Predicate`.This is a functional interface
whose functional method is `test(Object, Object)`.
Since:
1.8
See Also:
`Predicate`

### Method Summary

All Methods Instance Methods Abstract Methods Default Methods Modifier and TypeMethod and Description`default BiPredicate<T,U>``and(BiPredicate<? super T,? super U> other)`
Returns a composed predicate that represents a short-circuiting logical
AND of this predicate and another.`default BiPredicate<T,U>``negate()`
Returns a predicate that represents the logical negation of this
predicate.`default BiPredicate<T,U>``or(BiPredicate<? super T,? super U> other)`
Returns a composed predicate that represents a short-circuiting logical
OR of this predicate and another.`boolean``test(T t,
U u)`
Evaluates this predicate on the given arguments.

### Method Detail

#### test

```
boolean test(T t,
             U u)
```
Evaluates this predicate on the given arguments.
Parameters:
`t` - the first input argument
`u` - the second input argument
Returns:
`true` if the input arguments match the predicate,
otherwise `false`

#### and

```
default BiPredicate<T,U> and(BiPredicate<? super T,? super U> other)
```
Returns a composed predicate that represents a short-circuiting logical
AND of this predicate and another. When evaluating the composed
predicate, if this predicate is `false`, then the `other`
predicate is not evaluated.Any exceptions thrown during evaluation of either predicate are relayed
to the caller; if evaluation of this predicate throws an exception, the
`other` predicate will not be evaluated.
Parameters:
`other` - a predicate that will be logically-ANDed with this
predicate
Returns:
a composed predicate that represents the short-circuiting logical
AND of this predicate and the `other` predicate
Throws:
`NullPointerException` - if other is null

#### negate

```
default BiPredicate<T,U> negate()
```
Returns a predicate that represents the logical negation of this
predicate.
Returns:
a predicate that represents the logical negation of this
predicate

#### or

```
default BiPredicate<T,U> or(BiPredicate<? super T,? super U> other)
```
Returns a composed predicate that represents a short-circuiting logical
OR of this predicate and another. When evaluating the composed
predicate, if this predicate is `true`, then the `other`
predicate is not evaluated.Any exceptions thrown during evaluation of either predicate are relayed
to the caller; if evaluation of this predicate throws an exception, the
`other` predicate will not be evaluated.
Parameters:
`other` - a predicate that will be logically-ORed with this
predicate
Returns:
a composed predicate that represents the short-circuiting logical
OR of this predicate and the `other` predicate
Throws:
`NullPointerException` - if other is null




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

