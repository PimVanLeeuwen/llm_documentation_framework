

Formatter.BigDecimalLayoutForm (Java Platform SE 8 )







<!--
try {
if (location.href.indexOf('is-external=true') == -1) {
parent.document.title="Formatter.BigDecimalLayoutForm (Java Platform SE 8 )";
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
java.utilEnum Formatter.BigDecimalLayoutForm
java.lang.Objectjava.lang.Enum<Formatter.BigDecimalLayoutForm>java.util.Formatter.BigDecimalLayoutForm
All Implemented Interfaces:
Serializable, Comparable<Formatter.BigDecimalLayoutForm>

Enclosing class:
Formatter


```
public static enum Formatter.BigDecimalLayoutForm
extends Enum<Formatter.BigDecimalLayoutForm>
```
Enum for `BigDecimal` formatting.

### Enum Constant Summary

Enum Constants Enum Constant and Description`DECIMAL_FLOAT`
Format the `BigDecimal` as a decimal number.`SCIENTIFIC`
Format the `BigDecimal` in computerized scientific notation.

### Method Summary

All Methods Static Methods Concrete Methods Modifier and TypeMethod and Description`static Formatter.BigDecimalLayoutForm``valueOf(String name)`
Returns the enum constant of this type with the specified name.`static Formatter.BigDecimalLayoutForm[]``values()`
Returns an array containing the constants of this enum type, in
the order they are declared.

### Methods inherited from class java.lang.Enum

`clone, compareTo, equals, finalize, getDeclaringClass, hashCode, name, ordinal, toString, valueOf`

### Methods inherited from class java.lang.Object

`getClass, notify, notifyAll, wait, wait, wait`

### Enum Constant Detail

#### SCIENTIFIC

```
public static final Formatter.BigDecimalLayoutForm SCIENTIFIC
```
Format the `BigDecimal` in computerized scientific notation.

#### DECIMAL\_FLOAT

```
public static final Formatter.BigDecimalLayoutForm DECIMAL_FLOAT
```
Format the `BigDecimal` as a decimal number.

### Method Detail

#### values

```
public static Formatter.BigDecimalLayoutForm[] values()
```
Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:
```

for (Formatter.BigDecimalLayoutForm c : Formatter.BigDecimalLayoutForm.values())
    System.out.println(c);

```

Returns:
an array containing the constants of this enum type, in the order they are declared

#### valueOf

```
public static Formatter.BigDecimalLayoutForm valueOf(String name)
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

