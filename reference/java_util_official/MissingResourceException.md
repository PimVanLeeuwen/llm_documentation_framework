

MissingResourceException (Java Platform SE 8 )







<!--
try {
if (location.href.indexOf('is-external=true') == -1) {
parent.document.title="MissingResourceException (Java Platform SE 8 )";
}
}
catch(err) {
}
//-->
var methods = {"i0":10,"i1":10};
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
java.utilClass MissingResourceException
java.lang.Objectjava.lang.Throwablejava.lang.Exceptionjava.lang.RuntimeExceptionjava.util.MissingResourceException
All Implemented Interfaces:
Serializable


```
public class MissingResourceException
extends RuntimeException
```
Signals that a resource is missing.
Since:
JDK1.1
See Also:
`Exception`,
`ResourceBundle`,
Serialized Form

### Constructor Summary

Constructors Constructor and Description`MissingResourceException(String s,
String className,
String key)`
Constructs a MissingResourceException with the specified information.

### Method Summary

All Methods Instance Methods Concrete Methods Modifier and TypeMethod and Description`String``getClassName()`
Gets parameter passed by constructor.`String``getKey()`
Gets parameter passed by constructor.

### Methods inherited from class java.lang.Throwable

`addSuppressed, fillInStackTrace, getCause, getLocalizedMessage, getMessage, getStackTrace, getSuppressed, initCause, printStackTrace, printStackTrace, printStackTrace, setStackTrace, toString`

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, wait, wait, wait`

### Constructor Detail

#### MissingResourceException

```
public MissingResourceException(String s,
                                String className,
                                String key)
```
Constructs a MissingResourceException with the specified information.
A detail message is a String that describes this particular exception.
Parameters:
`s` - the detail message
`className` - the name of the resource class
`key` - the key for the missing resource.

### Method Detail

#### getClassName

```
public String getClassName()
```
Gets parameter passed by constructor.
Returns:
the name of the resource class

#### getKey

```
public String getKey()
```
Gets parameter passed by constructor.
Returns:
the key for the missing resource




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

