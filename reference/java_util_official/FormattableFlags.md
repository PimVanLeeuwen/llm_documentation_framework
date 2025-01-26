

FormattableFlags (Java Platform SE 8 )








<!--
try {
if (location.href.indexOf('is-external=true') == -1) {
parent.document.title="FormattableFlags (Java Platform SE 8 )";
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
java.utilClass FormattableFlags
java.lang.Objectjava.util.FormattableFlags
```
public class FormattableFlags
extends Object
```
FomattableFlags are passed to the `Formattable.formatTo()` method and modify the output format for Formattables. Implementations of `Formattable` are
responsible for interpreting and validating any flags.
Since:
1.5

### Field Summary

Fields Modifier and TypeField and Description`static int``ALTERNATE`
Requires the output to use an alternate form.`static int``LEFT_JUSTIFY`
Left-justifies the output.`static int``UPPERCASE`
Converts the output to upper case according to the rules of the
locale given during creation of the
formatter argument of the `formatTo()` method.

### Method Summary

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

### Field Detail

#### LEFT\_JUSTIFY

```
public static final int LEFT_JUSTIFY
```
Left-justifies the output. Spaces ('\u0020') will be added
at the end of the converted value as required to fill the minimum width
of the field. If this flag is not set then the output will be
right-justified.This flag corresponds to '-' ('\u002d') in
the format specifier.
See Also:
Constant Field Values

#### UPPERCASE

```
public static final int UPPERCASE
```
Converts the output to upper case according to the rules of the
locale given during creation of the
formatter argument of the `formatTo()` method. The output should be equivalent the following
invocation of `String.toUpperCase(java.util.Locale)`
```

     out.toUpperCase() 
```
This flag corresponds to 'S' ('\u0053') in
the format specifier.
See Also:
Constant Field Values

#### ALTERNATE

```
public static final int ALTERNATE
```
Requires the output to use an alternate form. The definition of the
form is specified by the Formattable.This flag corresponds to '#' ('\u0023') in
the format specifier.
See Also:
Constant Field Values




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

