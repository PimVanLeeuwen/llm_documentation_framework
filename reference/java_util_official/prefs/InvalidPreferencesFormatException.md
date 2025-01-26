

InvalidPreferencesFormatException (Java Platform SE 8 )





<!--
try {
if (location.href.indexOf('is-external=true') == -1) {
parent.document.title="InvalidPreferencesFormatException (Java Platform SE 8 )";
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
java.util.prefsClass InvalidPreferencesFormatException
java.lang.Objectjava.lang.Throwablejava.lang.Exceptionjava.util.prefs.InvalidPreferencesFormatException
All Implemented Interfaces:
Serializable


```
public class InvalidPreferencesFormatException
extends Exception
```
Thrown to indicate that an operation could not complete because
the input did not conform to the appropriate XML document type
for a collection of preferences, as per the `Preferences`
specification.
Since:
1.4
See Also:
`Preferences`,
Serialized Form

### Constructor Summary

Constructors Constructor and Description`InvalidPreferencesFormatException(String message)`
Constructs an InvalidPreferencesFormatException with the specified
detail message.`InvalidPreferencesFormatException(String message,
Throwable cause)`
Constructs an InvalidPreferencesFormatException with the specified
detail message and cause.`InvalidPreferencesFormatException(Throwable cause)`
Constructs an InvalidPreferencesFormatException with the specified
cause.

### Method Summary

### Methods inherited from class java.lang.Throwable

`addSuppressed, fillInStackTrace, getCause, getLocalizedMessage, getMessage, getStackTrace, getSuppressed, initCause, printStackTrace, printStackTrace, printStackTrace, setStackTrace, toString`

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, wait, wait, wait`

### Constructor Detail

#### InvalidPreferencesFormatException

```
public InvalidPreferencesFormatException(Throwable cause)
```
Constructs an InvalidPreferencesFormatException with the specified
cause.
Parameters:
`cause` - the cause (which is saved for later retrieval by the
`Throwable.getCause()` method).

#### InvalidPreferencesFormatException

```
public InvalidPreferencesFormatException(String message)
```
Constructs an InvalidPreferencesFormatException with the specified
detail message.
Parameters:
`message` - the detail message. The detail message is saved for
later retrieval by the `Throwable.getMessage()` method.

#### InvalidPreferencesFormatException

```
public InvalidPreferencesFormatException(String message,
                                         Throwable cause)
```
Constructs an InvalidPreferencesFormatException with the specified
detail message and cause.
Parameters:
`message` - the detail message. The detail message is saved for
later retrieval by the `Throwable.getMessage()` method.
`cause` - the cause (which is saved for later retrieval by the
`Throwable.getCause()` method).




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

