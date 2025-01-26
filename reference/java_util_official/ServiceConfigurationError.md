

ServiceConfigurationError (Java Platform SE 8 )





<!--
try {
if (location.href.indexOf('is-external=true') == -1) {
parent.document.title="ServiceConfigurationError (Java Platform SE 8 )";
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
java.utilClass ServiceConfigurationError
java.lang.Objectjava.lang.Throwablejava.lang.Errorjava.util.ServiceConfigurationError
All Implemented Interfaces:
Serializable


```
public class ServiceConfigurationError
extends Error
```
Error thrown when something goes wrong while loading a service provider.This error will be thrown in the following situations:The format of a provider-configuration file violates the specification;An `IOException` occurs while reading a
provider-configuration file;A concrete provider class named in a provider-configuration file
cannot be found;A concrete provider class is not a subclass of the service class;A concrete provider class cannot be instantiated; orSome other kind of error occurs.
Since:
1.6
See Also:
Serialized Form

### Constructor Summary

Constructors Constructor and Description`ServiceConfigurationError(String msg)`
Constructs a new instance with the specified message.`ServiceConfigurationError(String msg,
Throwable cause)`
Constructs a new instance with the specified message and cause.

### Method Summary

### Methods inherited from class java.lang.Throwable

`addSuppressed, fillInStackTrace, getCause, getLocalizedMessage, getMessage, getStackTrace, getSuppressed, initCause, printStackTrace, printStackTrace, printStackTrace, setStackTrace, toString`

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, wait, wait, wait`

### Constructor Detail

#### ServiceConfigurationError

```
public ServiceConfigurationError(String msg)
```
Constructs a new instance with the specified message.
Parameters:
`msg` - The message, or null if there is no message

#### ServiceConfigurationError

```
public ServiceConfigurationError(String msg,
                                 Throwable cause)
```
Constructs a new instance with the specified message and cause.
Parameters:
`msg` - The message, or null if there is no message
`cause` - The cause, or null if the cause is nonexistent
or unknown




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

