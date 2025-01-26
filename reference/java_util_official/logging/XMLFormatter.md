

XMLFormatter (Java Platform SE 8 )








<!--
try {
if (location.href.indexOf('is-external=true') == -1) {
parent.document.title="XMLFormatter (Java Platform SE 8 )";
}
}
catch(err) {
}
//-->
var methods = {"i0":10,"i1":10,"i2":10};
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
java.util.loggingClass XMLFormatter
java.lang.Objectjava.util.logging.Formatterjava.util.logging.XMLFormatter
```
public class XMLFormatter
extends Formatter
```
Format a LogRecord into a standard XML format.The DTD specification is provided as Appendix A to the
Java Logging APIs specification.The XMLFormatter can be used with arbitrary character encodings,
but it is recommended that it normally be used with UTF-8. The
character encoding can be set on the output Handler.
Since:
1.4

### Constructor Summary

Constructors Constructor and Description`XMLFormatter()`

### Method Summary

All Methods Instance Methods Concrete Methods Modifier and TypeMethod and Description`String``format(LogRecord record)`
Format the given message to XML.`String``getHead(Handler h)`
Return the header string for a set of XML formatted records.`String``getTail(Handler h)`
Return the tail string for a set of XML formatted records.

### Methods inherited from class java.util.logging.Formatter

`formatMessage`

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

### Constructor Detail

#### XMLFormatter

```
public XMLFormatter()
```

### Method Detail

#### format

```
public String format(LogRecord record)
```
Format the given message to XML.This method can be overridden in a subclass.
It is recommended to use the `Formatter.formatMessage(java.util.logging.LogRecord)`
convenience method to localize and format the message field.
Specified by:
`format` in class `Formatter`
Parameters:
`record` - the log record to be formatted.
Returns:
a formatted log record

#### getHead

```
public String getHead(Handler h)
```
Return the header string for a set of XML formatted records.
Overrides:
`getHead` in class `Formatter`
Parameters:
`h` - The target handler (can be null)
Returns:
a valid XML string

#### getTail

```
public String getTail(Handler h)
```
Return the tail string for a set of XML formatted records.
Overrides:
`getTail` in class `Formatter`
Parameters:
`h` - The target handler (can be null)
Returns:
a valid XML string




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

