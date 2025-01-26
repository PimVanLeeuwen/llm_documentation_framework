

ErrorManager (Java Platform SE 8 )












<!--
try {
if (location.href.indexOf('is-external=true') == -1) {
parent.document.title="ErrorManager (Java Platform SE 8 )";
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
java.util.loggingClass ErrorManager
java.lang.Objectjava.util.logging.ErrorManager
```
public class ErrorManager
extends Object
```
ErrorManager objects can be attached to Handlers to process
any error that occurs on a Handler during Logging.When processing logging output, if a Handler encounters problems
then rather than throwing an Exception back to the issuer of
the logging call (who is unlikely to be interested) the Handler
should call its associated ErrorManager.

### Field Summary

Fields Modifier and TypeField and Description`static int``CLOSE_FAILURE`
CLOSE\_FAILURE is used when a close of an output stream fails.`static int``FLUSH_FAILURE`
FLUSH\_FAILURE is used when a flush to an output stream fails.`static int``FORMAT_FAILURE`
FORMAT\_FAILURE is used when formatting fails for any reason.`static int``GENERIC_FAILURE`
GENERIC\_FAILURE is used for failure that don't fit
into one of the other categories.`static int``OPEN_FAILURE`
OPEN\_FAILURE is used when an open of an output stream fails.`static int``WRITE_FAILURE`
WRITE\_FAILURE is used when a write to an output stream fails.

### Constructor Summary

Constructors Constructor and Description`ErrorManager()`

### Method Summary

All Methods Instance Methods Concrete Methods Modifier and TypeMethod and Description`void``error(String msg,
Exception ex,
int code)`
The error method is called when a Handler failure occurs.

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

### Field Detail

#### GENERIC\_FAILURE

```
public static final int GENERIC_FAILURE
```
GENERIC\_FAILURE is used for failure that don't fit
into one of the other categories.
See Also:
Constant Field Values

#### WRITE\_FAILURE

```
public static final int WRITE_FAILURE
```
WRITE\_FAILURE is used when a write to an output stream fails.
See Also:
Constant Field Values

#### FLUSH\_FAILURE

```
public static final int FLUSH_FAILURE
```
FLUSH\_FAILURE is used when a flush to an output stream fails.
See Also:
Constant Field Values

#### CLOSE\_FAILURE

```
public static final int CLOSE_FAILURE
```
CLOSE\_FAILURE is used when a close of an output stream fails.
See Also:
Constant Field Values

#### OPEN\_FAILURE

```
public static final int OPEN_FAILURE
```
OPEN\_FAILURE is used when an open of an output stream fails.
See Also:
Constant Field Values

#### FORMAT\_FAILURE

```
public static final int FORMAT_FAILURE
```
FORMAT\_FAILURE is used when formatting fails for any reason.
See Also:
Constant Field Values

### Constructor Detail

#### ErrorManager

```
public ErrorManager()
```

### Method Detail

#### error

```
public void error(String msg,
                  Exception ex,
                  int code)
```
The error method is called when a Handler failure occurs.This method may be overridden in subclasses. The default
behavior in this base class is that the first call is
reported to System.err, and subsequent calls are ignored.
Parameters:
`msg` - a descriptive string (may be null)
`ex` - an exception (may be null)
`code` - an error code defined in ErrorManager




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

