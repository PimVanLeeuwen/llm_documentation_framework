

IllegalFormatWidthException (Java Platform SE 8 )







<!--
try {
if (location.href.indexOf('is-external=true') == -1) {
parent.document.title="IllegalFormatWidthException (Java Platform SE 8 )";
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
java.utilClass IllegalFormatWidthException
java.lang.Objectjava.lang.Throwablejava.lang.Exceptionjava.lang.RuntimeExceptionjava.lang.IllegalArgumentExceptionjava.util.IllegalFormatExceptionjava.util.IllegalFormatWidthException
All Implemented Interfaces:
Serializable


```
public class IllegalFormatWidthException
extends IllegalFormatException
```
Unchecked exception thrown when the format width is a negative value other
than -1 or is otherwise unsupported.
Since:
1.5
See Also:
Serialized Form

### Constructor Summary

Constructors Constructor and Description`IllegalFormatWidthException(int w)`
Constructs an instance of this class with the specified width.

### Method Summary

All Methods Instance Methods Concrete Methods Modifier and TypeMethod and Description`String``getMessage()`
Returns the detail message string of this throwable.`int``getWidth()`
Returns the width

### Methods inherited from class java.lang.Throwable

`addSuppressed, fillInStackTrace, getCause, getLocalizedMessage, getStackTrace, getSuppressed, initCause, printStackTrace, printStackTrace, printStackTrace, setStackTrace, toString`

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, wait, wait, wait`

### Constructor Detail

#### IllegalFormatWidthException

```
public IllegalFormatWidthException(int w)
```
Constructs an instance of this class with the specified width.
Parameters:
`w` - The width

### Method Detail

#### getWidth

```
public int getWidth()
```
Returns the width
Returns:
The width

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

