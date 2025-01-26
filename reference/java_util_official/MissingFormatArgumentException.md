

MissingFormatArgumentException (Java Platform SE 8 )







<!--
try {
if (location.href.indexOf('is-external=true') == -1) {
parent.document.title="MissingFormatArgumentException (Java Platform SE 8 )";
}
}
catch(err) {
}
//-->
var methods = {"i0":10,"i1":10};
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
java.utilClass MissingFormatArgumentException
java.lang.Objectjava.lang.Throwablejava.lang.Exceptionjava.lang.RuntimeExceptionjava.lang.IllegalArgumentExceptionjava.util.IllegalFormatExceptionjava.util.MissingFormatArgumentException
All Implemented Interfaces:
Serializable


```
public class MissingFormatArgumentException
extends IllegalFormatException
```
Unchecked exception thrown when there is a format specifier which does not
have a corresponding argument or if an argument index refers to an argument
that does not exist.Unless otherwise specified, passing a null argument to any
method or constructor in this class will cause a `NullPointerException` to be thrown.
Since:
1.5
See Also:
Serialized Form

### Constructor Summary

Constructors Constructor and Description`MissingFormatArgumentException(String s)`
Constructs an instance of this class with the unmatched format
specifier.

### Method Summary

All Methods Instance Methods Concrete Methods Modifier and TypeMethod and Description`String``getFormatSpecifier()`
Returns the unmatched format specifier.`String``getMessage()`
Returns the detail message string of this throwable.

### Methods inherited from class java.lang.Throwable

`addSuppressed, fillInStackTrace, getCause, getLocalizedMessage, getStackTrace, getSuppressed, initCause, printStackTrace, printStackTrace, printStackTrace, setStackTrace, toString`

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, wait, wait, wait`

### Constructor Detail

#### MissingFormatArgumentException

```
public MissingFormatArgumentException(String s)
```
Constructs an instance of this class with the unmatched format
specifier.
Parameters:
`s` - Format specifier which does not have a corresponding argument

### Method Detail

#### getFormatSpecifier

```
public String getFormatSpecifier()
```
Returns the unmatched format specifier.
Returns:
The unmatched format specifier

#### getMessage

```
public String getMessage()
```
Description copied from class: `Throwable`
Returns the detail message string of this throwable.
Overrides:
`getMessage` in class `Throwable`
Returns:
the detail message string of this `Throwable` instance
(which may be `null`).




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

