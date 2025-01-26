

BackingStoreException (Java Platform SE 8 )





<!--
try {
if (location.href.indexOf('is-external=true') == -1) {
parent.document.title="BackingStoreException (Java Platform SE 8 )";
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




compact3
java.util.prefsClass BackingStoreException
java.lang.Objectjava.lang.Throwablejava.lang.Exceptionjava.util.prefs.BackingStoreException
All Implemented Interfaces:
Serializable


```
public class BackingStoreException
extends Exception
```
Thrown to indicate that a preferences operation could not complete because
of a failure in the backing store, or a failure to contact the backing
store.
Since:
1.4
See Also:
Serialized Form

### Constructor Summary

Constructors Constructor and Description`BackingStoreException(String s)`
Constructs a BackingStoreException with the specified detail message.`BackingStoreException(Throwable cause)`
Constructs a BackingStoreException with the specified cause.

### Method Summary

### Methods inherited from class java.lang.Throwable

`addSuppressed, fillInStackTrace, getCause, getLocalizedMessage, getMessage, getStackTrace, getSuppressed, initCause, printStackTrace, printStackTrace, printStackTrace, setStackTrace, toString`

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, wait, wait, wait`

### Constructor Detail

#### BackingStoreException

```
public BackingStoreException(String s)
```
Constructs a BackingStoreException with the specified detail message.
Parameters:
`s` - the detail message.

#### BackingStoreException

```
public BackingStoreException(Throwable cause)
```
Constructs a BackingStoreException with the specified cause.
Parameters:
`cause` - the cause




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

