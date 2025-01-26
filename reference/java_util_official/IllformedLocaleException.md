

IllformedLocaleException (Java Platform SE 8 )






<!--
try {
if (location.href.indexOf('is-external=true') == -1) {
parent.document.title="IllformedLocaleException (Java Platform SE 8 )";
}
}
catch(err) {
}
//-->
var methods = {"i0":10};
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
java.utilClass IllformedLocaleException
java.lang.Objectjava.lang.Throwablejava.lang.Exceptionjava.lang.RuntimeExceptionjava.util.IllformedLocaleException
All Implemented Interfaces:
Serializable


```
public class IllformedLocaleException
extends RuntimeException
```
Thrown by methods in `Locale` and `Locale.Builder` to
indicate that an argument is not a well-formed BCP 47 tag.
Since:
1.7
See Also:
`Locale`,
Serialized Form

### Constructor Summary

Constructors Constructor and Description`IllformedLocaleException()`
Constructs a new `IllformedLocaleException` with no
detail message and -1 as the error index.`IllformedLocaleException(String message)`
Constructs a new `IllformedLocaleException` with the
given message and -1 as the error index.`IllformedLocaleException(String message,
int errorIndex)`
Constructs a new `IllformedLocaleException` with the
given message and the error index.

### Method Summary

All Methods Instance Methods Concrete Methods Modifier and TypeMethod and Description`int``getErrorIndex()`
Returns the index where the error was found.

### Methods inherited from class java.lang.Throwable

`addSuppressed, fillInStackTrace, getCause, getLocalizedMessage, getMessage, getStackTrace, getSuppressed, initCause, printStackTrace, printStackTrace, printStackTrace, setStackTrace, toString`

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, wait, wait, wait`

### Constructor Detail

#### IllformedLocaleException

```
public IllformedLocaleException()
```
Constructs a new `IllformedLocaleException` with no
detail message and -1 as the error index.

#### IllformedLocaleException

```
public IllformedLocaleException(String message)
```
Constructs a new `IllformedLocaleException` with the
given message and -1 as the error index.
Parameters:
`message` - the message

#### IllformedLocaleException

```
public IllformedLocaleException(String message,
                                int errorIndex)
```
Constructs a new `IllformedLocaleException` with the
given message and the error index. The error index is the approximate
offset from the start of the ill-formed value to the point where the
parse first detected an error. A negative error index value indicates
either the error index is not applicable or unknown.
Parameters:
`message` - the message
`errorIndex` - the index

### Method Detail

#### getErrorIndex

```
public int getErrorIndex()
```
Returns the index where the error was found. A negative value indicates
either the error index is not applicable or unknown.
Returns:
the error index




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

