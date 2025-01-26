

PatternSyntaxException (Java Platform SE 8 )









<!--
try {
if (location.href.indexOf('is-external=true') == -1) {
parent.document.title="PatternSyntaxException (Java Platform SE 8 )";
}
}
catch(err) {
}
//-->
var methods = {"i0":10,"i1":10,"i2":10,"i3":10};
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
java.util.regexClass PatternSyntaxException
java.lang.Objectjava.lang.Throwablejava.lang.Exceptionjava.lang.RuntimeExceptionjava.lang.IllegalArgumentExceptionjava.util.regex.PatternSyntaxException
All Implemented Interfaces:
Serializable


```
public class PatternSyntaxException
extends IllegalArgumentException
```
Unchecked exception thrown to indicate a syntax error in a
regular-expression pattern.
Since:
1.4
See Also:
Serialized Form

### Constructor Summary

Constructors Constructor and Description`PatternSyntaxException(String desc,
String regex,
int index)`
Constructs a new instance of this class.

### Method Summary

All Methods Instance Methods Concrete Methods Modifier and TypeMethod and Description`String``getDescription()`
Retrieves the description of the error.`int``getIndex()`
Retrieves the error index.`String``getMessage()`
Returns a multi-line string containing the description of the syntax
error and its index, the erroneous regular-expression pattern, and a
visual indication of the error index within the pattern.`String``getPattern()`
Retrieves the erroneous regular-expression pattern.

### Methods inherited from class java.lang.Throwable

`addSuppressed, fillInStackTrace, getCause, getLocalizedMessage, getStackTrace, getSuppressed, initCause, printStackTrace, printStackTrace, printStackTrace, setStackTrace, toString`

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, wait, wait, wait`

### Constructor Detail

#### PatternSyntaxException

```
public PatternSyntaxException(String desc,
                              String regex,
                              int index)
```
Constructs a new instance of this class.
Parameters:
`desc` - A description of the error
`regex` - The erroneous pattern
`index` - The approximate index in the pattern of the error,
or -1 if the index is not known

### Method Detail

#### getIndex

```
public int getIndex()
```
Retrieves the error index.
Returns:
The approximate index in the pattern of the error,
or -1 if the index is not known

#### getDescription

```
public String getDescription()
```
Retrieves the description of the error.
Returns:
The description of the error

#### getPattern

```
public String getPattern()
```
Retrieves the erroneous regular-expression pattern.
Returns:
The erroneous pattern

#### getMessage

```
public String getMessage()
```
Returns a multi-line string containing the description of the syntax
error and its index, the erroneous regular-expression pattern, and a
visual indication of the error index within the pattern.
Overrides:
`getMessage` in class `Throwable`
Returns:
The full detail message




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

