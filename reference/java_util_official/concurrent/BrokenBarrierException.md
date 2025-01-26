

BrokenBarrierException (Java Platform SE 8 )





<!--
try {
if (location.href.indexOf('is-external=true') == -1) {
parent.document.title="BrokenBarrierException (Java Platform SE 8 )";
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
java.util.concurrentClass BrokenBarrierException
java.lang.Objectjava.lang.Throwablejava.lang.Exceptionjava.util.concurrent.BrokenBarrierException
All Implemented Interfaces:
Serializable


```
public class BrokenBarrierException
extends Exception
```
Exception thrown when a thread tries to wait upon a barrier that is
in a broken state, or which enters the broken state while the thread
is waiting.
Since:
1.5
See Also:
`CyclicBarrier`,
Serialized Form

### Constructor Summary

Constructors Constructor and Description`BrokenBarrierException()`
Constructs a `BrokenBarrierException` with no specified detail
message.`BrokenBarrierException(String message)`
Constructs a `BrokenBarrierException` with the specified
detail message.

### Method Summary

### Methods inherited from class java.lang.Throwable

`addSuppressed, fillInStackTrace, getCause, getLocalizedMessage, getMessage, getStackTrace, getSuppressed, initCause, printStackTrace, printStackTrace, printStackTrace, setStackTrace, toString`

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, wait, wait, wait`

### Constructor Detail

#### BrokenBarrierException

```
public BrokenBarrierException()
```
Constructs a `BrokenBarrierException` with no specified detail
message.

#### BrokenBarrierException

```
public BrokenBarrierException(String message)
```
Constructs a `BrokenBarrierException` with the specified
detail message.
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

