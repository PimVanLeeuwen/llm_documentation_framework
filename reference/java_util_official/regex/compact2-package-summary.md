

java.util.regex (Java Platform SE 8 )





<!--
try {
if (location.href.indexOf('is-external=true') == -1) {
parent.document.title="java.util.regex (Java Platform SE 8 )";
}
}
catch(err) {
}
//-->

JavaScript is disabled on your browser.


Skip navigation links

OverviewPackageClassUseTreeDeprecatedIndexHelpJava™ PlatformStandard Ed. 8

Prev PackageNext PackageFramesNo FramesAll Classes
<!--
allClassesLink = document.getElementById("allclasses\_navbar\_top");
if(window==top) {
allClassesLink.style.display = "block";
}
else {
allClassesLink.style.display = "none";
}
//-->




compact2Package java.util.regex
Classes for matching character sequences against patterns specified by regular
expressions.
See: Description

Interface Summary InterfaceDescriptionMatchResultThe result of a match operation.

Class Summary ClassDescriptionMatcherAn engine that performs match operations on a character sequence by interpreting a `Pattern`.PatternA compiled representation of a regular expression.

Exception Summary ExceptionDescriptionPatternSyntaxExceptionUnchecked exception thrown to indicate a syntax error in a
regular-expression pattern.

Package java.util.regex DescriptionClasses for matching character sequences against patterns specified by regular
expressions.An instance of the `Pattern` class represents a
regular expression that is specified in string form in a syntax similar to
that used by Perl.Instances of the `Matcher` class are used to match
character sequences against a given pattern. Input is provided to matchers via
the `CharSequence` interface in order to support matching
against characters from a wide variety of input sources.Unless otherwise noted, passing a null argument to a method
in any class or interface in this package will cause a
`NullPointerException` to be thrown.Related DocumentationAn excellent tutorial and overview of regular expressions is Mastering Regular
Expressions, Jeffrey E. F. Friedl, O'Reilly and Associates, 1997.
Since:
1.4



Skip navigation links

OverviewPackageClassUseTreeDeprecatedIndexHelpJava™ PlatformStandard Ed. 8

Prev PackageNext PackageFramesNo FramesAll Classes
<!--
allClassesLink = document.getElementById("allclasses\_navbar\_bottom");
if(window==top) {
allClassesLink.style.display = "block";
}
else {
allClassesLink.style.display = "none";
}
//-->



 Submit a bug or feature For further API reference and developer documentation, see Java SE Documentation. That documentation contains more detailed, developer-targeted descriptions, with conceptual overviews, definitions of terms, workarounds, and working code examples. Copyright © 1993, 2025, Oracle and/or its affiliates. All rights reserved. Use is subject to license terms. Also see the documentation redistribution policy. 

