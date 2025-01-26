

ConsoleHandler (Java Platform SE 8 )







<!--
try {
if (location.href.indexOf('is-external=true') == -1) {
parent.document.title="ConsoleHandler (Java Platform SE 8 )";
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
java.util.loggingClass ConsoleHandler
java.lang.Objectjava.util.logging.Handlerjava.util.logging.StreamHandlerjava.util.logging.ConsoleHandler
```
public class ConsoleHandler
extends StreamHandler
```
This Handler publishes log records to System.err.
By default the SimpleFormatter is used to generate brief summaries.Configuration:
By default each ConsoleHandler is initialized using the following
LogManager configuration properties where `<handler-name>`
refers to the fully-qualified class name of the handler.
If properties are not defined
(or have invalid values) then the specified default values are used.<handler-name>.level
specifies the default level for the Handler
(defaults to Level.INFO).<handler-name>.filter
specifies the name of a Filter class to use
(defaults to no Filter).<handler-name>.formatter
specifies the name of a Formatter class to use
(defaults to java.util.logging.SimpleFormatter).<handler-name>.encoding
the name of the character set encoding to use (defaults to
the default platform encoding).For example, the properties for `ConsoleHandler` would be:java.util.logging.ConsoleHandler.level=INFOjava.util.logging.ConsoleHandler.formatter=java.util.logging.SimpleFormatterFor a custom handler, e.g. com.foo.MyHandler, the properties would be:com.foo.MyHandler.level=INFOcom.foo.MyHandler.formatter=java.util.logging.SimpleFormatter
Since:
1.4

### Constructor Summary

Constructors Constructor and Description`ConsoleHandler()`
Create a ConsoleHandler for System.err.

### Method Summary

All Methods Instance Methods Concrete Methods Modifier and TypeMethod and Description`void``close()`
Override StreamHandler.close to do a flush but not
to close the output stream.`void``publish(LogRecord record)`
Publish a LogRecord.

### Methods inherited from class java.util.logging.StreamHandler

`flush, isLoggable, setEncoding, setOutputStream`

### Methods inherited from class java.util.logging.Handler

`getEncoding, getErrorManager, getFilter, getFormatter, getLevel, reportError, setErrorManager, setFilter, setFormatter, setLevel`

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

### Constructor Detail

#### ConsoleHandler

```
public ConsoleHandler()
```
Create a ConsoleHandler for System.err.The ConsoleHandler is configured based on
LogManager properties (or their default values).

### Method Detail

#### publish

```
public void publish(LogRecord record)
```
Publish a LogRecord.The logging request was made initially to a Logger object,
which initialized the LogRecord and forwarded it here.
Overrides:
`publish` in class `StreamHandler`
Parameters:
`record` - description of the log event. A null record is
silently ignored and is not published

#### close

```
public void close()
```
Override StreamHandler.close to do a flush but not
to close the output stream. That is, we do not
close System.err.
Overrides:
`close` in class `StreamHandler`




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

