

Formatter (Java Platform SE 8 )









<!--
try {
if (location.href.indexOf('is-external=true') == -1) {
parent.document.title="Formatter (Java Platform SE 8 )";
}
}
catch(err) {
}
//-->
var methods = {"i0":6,"i1":10,"i2":10,"i3":10};
var tabs = {65535:["t0","All Methods"],2:["t2","Instance Methods"],4:["t3","Abstract Methods"],8:["t4","Concrete Methods"]};
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
java.util.loggingClass Formatter
java.lang.Objectjava.util.logging.Formatter
Direct Known Subclasses:
SimpleFormatter, XMLFormatter


```
public abstract class Formatter
extends Object
```
A Formatter provides support for formatting LogRecords.Typically each logging Handler will have a Formatter associated
with it. The Formatter takes a LogRecord and converts it to
a string.Some formatters (such as the XMLFormatter) need to wrap head
and tail strings around a set of formatted records. The getHeader
and getTail methods can be used to obtain these strings.
Since:
1.4

### Constructor Summary

Constructors ModifierConstructor and Description`protected` `Formatter()`
Construct a new formatter.

### Method Summary

All Methods Instance Methods Abstract Methods Concrete Methods Modifier and TypeMethod and Description`abstract String``format(LogRecord record)`
Format the given log record and return the formatted string.`String``formatMessage(LogRecord record)`
Localize and format the message string from a log record.`String``getHead(Handler h)`
Return the header string for a set of formatted records.`String``getTail(Handler h)`
Return the tail string for a set of formatted records.

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

### Constructor Detail

#### Formatter

```
protected Formatter()
```
Construct a new formatter.

### Method Detail

#### format

```
public abstract String format(LogRecord record)
```
Format the given log record and return the formatted string.The resulting formatted String will normally include a
localized and formatted version of the LogRecord's message field.
It is recommended to use the `formatMessage(java.util.logging.LogRecord)`
convenience method to localize and format the message field.
Parameters:
`record` - the log record to be formatted.
Returns:
the formatted log record

#### getHead

```
public String getHead(Handler h)
```
Return the header string for a set of formatted records.This base class returns an empty string, but this may be
overridden by subclasses.
Parameters:
`h` - The target handler (can be null)
Returns:
header string

#### getTail

```
public String getTail(Handler h)
```
Return the tail string for a set of formatted records.This base class returns an empty string, but this may be
overridden by subclasses.
Parameters:
`h` - The target handler (can be null)
Returns:
tail string

#### formatMessage

```
public String formatMessage(LogRecord record)
```
Localize and format the message string from a log record. This
method is provided as a convenience for Formatter subclasses to
use when they are performing formatting.The message string is first localized to a format string using
the record's ResourceBundle. (If there is no ResourceBundle,
or if the message key is not found, then the key is used as the
format string.) The format String uses java.text style
formatting.If there are no parameters, no formatter is used.Otherwise, if the string contains "{0" then
java.text.MessageFormat is used to format the string.Otherwise no formatting is performed.
Parameters:
`record` - the log record containing the raw message
Returns:
a localized and formatted message




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

