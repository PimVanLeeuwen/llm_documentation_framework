

TimeoutException (Java Platform SE 8 )





<!--
try {
if (location.href.indexOf('is-external=true') == -1) {
parent.document.title="TimeoutException (Java Platform SE 8 )";
}
}
catch(err) {
}
//-->

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
java.util.concurrentClass TimeoutException
java.lang.Objectjava.lang.Throwablejava.lang.Exceptionjava.util.concurrent.TimeoutException
All Implemented Interfaces:
Serializable


```
public class TimeoutException
extends Exception
```
Exception thrown when a blocking operation times out. Blocking
operations for which a timeout is specified need a means to
indicate that the timeout has occurred. For many such operations it
is possible to return a value that indicates timeout; when that is
not possible or desirable then `TimeoutException` should be
declared and thrown.
Since:
1.5
See Also:
Serialized Form

### Constructor Summary

Constructors Constructor and Description`TimeoutException()`
Constructs a `TimeoutException` with no specified detail
message.`TimeoutException(String message)`
Constructs a `TimeoutException` with the specified detail
message.

### Method Summary

### Methods inherited from class java.lang.Throwable

`addSuppressed, fillInStackTrace, getCause, getLocalizedMessage, getMessage, getStackTrace, getSuppressed, initCause, printStackTrace, printStackTrace, printStackTrace, setStackTrace, toString`

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, wait, wait, wait`

### Constructor Detail

#### TimeoutException

```
public TimeoutException()
```
Constructs a `TimeoutException` with no specified detail
message.

#### TimeoutException

```
public TimeoutException(String message)
```
Constructs a `TimeoutException` with the specified detail
message.
Parameters:
`message` - the detail message




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

