

TooManyListenersException (Java Platform SE 8 )





<!--
try {
if (location.href.indexOf('is-external=true') == -1) {
parent.document.title="TooManyListenersException (Java Platform SE 8 )";
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
java.utilClass TooManyListenersException
java.lang.Objectjava.lang.Throwablejava.lang.Exceptionjava.util.TooManyListenersException
All Implemented Interfaces:
Serializable


```
public class TooManyListenersException
extends Exception
```
The  `TooManyListenersException`  Exception is used as part of
the Java Event model to annotate and implement a unicast special case of
a multicast Event Source.The presence of a "throws TooManyListenersException" clause on any given
concrete implementation of the normally multicast "void addXyzEventListener"
event listener registration pattern is used to annotate that interface as
implementing a unicast Listener special case, that is, that one and only
one Listener may be registered on the particular event listener source
concurrently.
Since:
JDK1.1
See Also:
`EventObject`,
`EventListener`,
Serialized Form

### Constructor Summary

Constructors Constructor and Description`TooManyListenersException()`
Constructs a TooManyListenersException with no detail message.`TooManyListenersException(String s)`
Constructs a TooManyListenersException with the specified detail message.

### Method Summary

### Methods inherited from class java.lang.Throwable

`addSuppressed, fillInStackTrace, getCause, getLocalizedMessage, getMessage, getStackTrace, getSuppressed, initCause, printStackTrace, printStackTrace, printStackTrace, setStackTrace, toString`

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, wait, wait, wait`

### Constructor Detail

#### TooManyListenersException

```
public TooManyListenersException()
```
Constructs a TooManyListenersException with no detail message.
A detail message is a String that describes this particular exception.

#### TooManyListenersException

```
public TooManyListenersException(String s)
```
Constructs a TooManyListenersException with the specified detail message.
A detail message is a String that describes this particular exception.
Parameters:
`s` - the detail message




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

