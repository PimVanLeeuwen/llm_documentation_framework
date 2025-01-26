

ExecutionException (Java Platform SE 8 )





<!--
try {
if (location.href.indexOf('is-external=true') == -1) {
parent.document.title="ExecutionException (Java Platform SE 8 )";
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
java.util.concurrentClass ExecutionException
java.lang.Objectjava.lang.Throwablejava.lang.Exceptionjava.util.concurrent.ExecutionException
All Implemented Interfaces:
Serializable


```
public class ExecutionException
extends Exception
```
Exception thrown when attempting to retrieve the result of a task
that aborted by throwing an exception. This exception can be
inspected using the `Throwable.getCause()` method.
Since:
1.5
See Also:
`Future`,
Serialized Form

### Constructor Summary

Constructors ModifierConstructor and Description`protected` `ExecutionException()`
Constructs an `ExecutionException` with no detail message.`protected` `ExecutionException(String message)`
Constructs an `ExecutionException` with the specified detail
message.`ExecutionException(String message,
Throwable cause)`
Constructs an `ExecutionException` with the specified detail
message and cause.`ExecutionException(Throwable cause)`
Constructs an `ExecutionException` with the specified cause.

### Method Summary

### Methods inherited from class java.lang.Throwable

`addSuppressed, fillInStackTrace, getCause, getLocalizedMessage, getMessage, getStackTrace, getSuppressed, initCause, printStackTrace, printStackTrace, printStackTrace, setStackTrace, toString`

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, wait, wait, wait`

### Constructor Detail

#### ExecutionException

```
protected ExecutionException()
```
Constructs an `ExecutionException` with no detail message.
The cause is not initialized, and may subsequently be
initialized by a call to `initCause`.

#### ExecutionException

```
protected ExecutionException(String message)
```
Constructs an `ExecutionException` with the specified detail
message. The cause is not initialized, and may subsequently be
initialized by a call to `initCause`.
Parameters:
`message` - the detail message

#### ExecutionException

```
public ExecutionException(String message,
                          Throwable cause)
```
Constructs an `ExecutionException` with the specified detail
message and cause.
Parameters:
`message` - the detail message
`cause` - the cause (which is saved for later retrieval by the
`Throwable.getCause()` method)

#### ExecutionException

```
public ExecutionException(Throwable cause)
```
Constructs an `ExecutionException` with the specified cause.
The detail message is set to `(cause == null ? null :
cause.toString())` (which typically contains the class and
detail message of `cause`).
Parameters:
`cause` - the cause (which is saved for later retrieval by the
`Throwable.getCause()` method)




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

