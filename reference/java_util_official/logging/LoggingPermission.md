

LoggingPermission (Java Platform SE 8 )





<!--
try {
if (location.href.indexOf('is-external=true') == -1) {
parent.document.title="LoggingPermission (Java Platform SE 8 )";
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
java.util.loggingClass LoggingPermission
java.lang.Objectjava.security.Permissionjava.security.BasicPermissionjava.util.logging.LoggingPermission
All Implemented Interfaces:
Serializable, Guard


```
public final class LoggingPermission
extends BasicPermission
```
The permission which the SecurityManager will check when code
that is running with a SecurityManager calls one of the logging
control methods (such as Logger.setLevel).Currently there is only one named LoggingPermission. This is "control"
and it grants the ability to control the logging configuration, for
example by adding or removing Handlers, by adding or removing Filters,
or by changing logging levels.Programmers do not normally create LoggingPermission objects directly.
Instead they are created by the security policy code based on reading
the security policy file.
Since:
1.4
See Also:
`BasicPermission`,
`Permission`,
`Permissions`,
`PermissionCollection`,
`SecurityManager`,
Serialized Form

### Constructor Summary

Constructors Constructor and Description`LoggingPermission(String name,
String actions)`
Creates a new LoggingPermission object.

### Method Summary

### Methods inherited from class java.security.BasicPermission

`equals, getActions, hashCode, implies, newPermissionCollection`

### Methods inherited from class java.security.Permission

`checkGuard, getName, toString`

### Methods inherited from class java.lang.Object

`clone, finalize, getClass, notify, notifyAll, wait, wait, wait`

### Constructor Detail

#### LoggingPermission

```
public LoggingPermission(String name,
                         String actions)
                  throws IllegalArgumentException
```
Creates a new LoggingPermission object.
Parameters:
`name` - Permission name. Must be "control".
`actions` - Must be either null or the empty string.
Throws:
`NullPointerException` - if `name` is `null`.
`IllegalArgumentException` - if `name` is empty or if
arguments are invalid.




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

