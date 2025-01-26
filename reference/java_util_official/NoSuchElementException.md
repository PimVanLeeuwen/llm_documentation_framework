

NoSuchElementException (Java Platform SE 8 )





<!--
try {
if (location.href.indexOf('is-external=true') == -1) {
parent.document.title="NoSuchElementException (Java Platform SE 8 )";
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
java.utilClass NoSuchElementException
java.lang.Objectjava.lang.Throwablejava.lang.Exceptionjava.lang.RuntimeExceptionjava.util.NoSuchElementException
All Implemented Interfaces:
Serializable

Direct Known Subclasses:
InputMismatchException


```
public class NoSuchElementException
extends RuntimeException
```
Thrown by various accessor methods to indicate that the element being requested
does not exist.
Since:
JDK1.0
See Also:
`Enumeration.nextElement()`,
`Iterator.next()`,
Serialized Form

### Constructor Summary

Constructors Constructor and Description`NoSuchElementException()`
Constructs a `NoSuchElementException` with null
as its error message string.`NoSuchElementException(String s)`
Constructs a `NoSuchElementException`, saving a reference
to the error message string s for later retrieval by the
getMessage method.

### Method Summary

### Methods inherited from class java.lang.Throwable

`addSuppressed, fillInStackTrace, getCause, getLocalizedMessage, getMessage, getStackTrace, getSuppressed, initCause, printStackTrace, printStackTrace, printStackTrace, setStackTrace, toString`

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, wait, wait, wait`

### Constructor Detail

#### NoSuchElementException

```
public NoSuchElementException()
```
Constructs a `NoSuchElementException` with null
as its error message string.

#### NoSuchElementException

```
public NoSuchElementException(String s)
```
Constructs a `NoSuchElementException`, saving a reference
to the error message string s for later retrieval by the
getMessage method.
Parameters:
`s` - the detail message.




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

