

SimpleFormatter (Java Platform SE 8 )






<!--
try {
if (location.href.indexOf('is-external=true') == -1) {
parent.document.title="SimpleFormatter (Java Platform SE 8 )";
}
}
catch(err) {
}
//-->
var methods = {"i0":10};
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
java.util.loggingClass SimpleFormatter
java.lang.Objectjava.util.logging.Formatterjava.util.logging.SimpleFormatter
```
public class SimpleFormatter
extends Formatter
```
Print a brief summary of the `LogRecord` in a human readable
format. The summary will typically be 1 or 2 lines.
Configuration:
The `SimpleFormatter` is initialized with the
format string
specified in the `java.util.logging.SimpleFormatter.format`
property to format the log messages.
This property can be defined
in the logging properties
configuration file
or as a system property. If this property is set in both
the logging properties and system properties,
the format string specified in the system property will be used.
If this property is not defined or the given format string
is illegal,
the default format is implementation-specific.
Since:
1.4
See Also:
`Formatter`

### Constructor Summary

Constructors Constructor and Description`SimpleFormatter()`

### Method Summary

All Methods Instance Methods Concrete Methods Modifier and TypeMethod and Description`String``format(LogRecord record)`
Format the given LogRecord.

### Methods inherited from class java.util.logging.Formatter

`formatMessage, getHead, getTail`

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

### Constructor Detail

#### SimpleFormatter

```
public SimpleFormatter()
```

### Method Detail

#### format

```
public String format(LogRecord record)
```
Format the given LogRecord.The formatting can be customized by specifying the
format string
in the 
`java.util.logging.SimpleFormatter.format` property.
The given `LogRecord` will be formatted as if by calling:
```

    String.format(format, date, source, logger, level, message, thrown);
 
```
where the arguments are:`format` - the `java.util.Formatter` format string specified in the
`java.util.logging.SimpleFormatter.format` property
or the default format.`date` - a `Date` object representing
event time of the log record.`source` - a string representing the caller, if available;
otherwise, the logger's name.`logger` - the logger's name.`level` - the log level.`message` - the formatted log message
returned from the `Formatter.formatMessage(LogRecord)`
method. It uses `java.text`
formatting and does not use the `java.util.Formatter
format` argument.`thrown` - a string representing
the throwable
associated with the log record and its backtrace
beginning with a newline character, if any;
otherwise, an empty string.Some example formats:`java.util.logging.SimpleFormatter.format="%4$s: %5$s [%1$tc]%n"`This prints 1 line with the log level (`4$`),
the log message (`5$`) and the timestamp (`1$`) in
a square bracket.
```

     WARNING: warning message [Tue Mar 22 13:11:31 PDT 2011]
     
```
`java.util.logging.SimpleFormatter.format="%1$tc %2$s%n%4$s: %5$s%6$s%n"`This prints 2 lines where the first line includes
the timestamp (`1$`) and the source (`2$`);
the second line includes the log level (`4$`) and
the log message (`5$`) followed with the throwable
and its backtrace (`6$`), if any:
```

     Tue Mar 22 13:11:31 PDT 2011 MyClass fatal
     SEVERE: several message with an exception
     java.lang.IllegalArgumentException: invalid argument
             at MyClass.mash(MyClass.java:9)
             at MyClass.crunch(MyClass.java:6)
             at MyClass.main(MyClass.java:3)
     
```
`java.util.logging.SimpleFormatter.format="%1$tb %1$td, %1$tY %1$tl:%1$tM:%1$tS %1$Tp %2$s%n%4$s: %5$s%n"`This prints 2 lines similar to the example above
with a different date/time formatting and does not print
the throwable and its backtrace:
```

     Mar 22, 2011 1:11:31 PM MyClass fatal
     SEVERE: several message with an exception
     
```
This method can also be overridden in a subclass.
It is recommended to use the `Formatter.formatMessage(java.util.logging.LogRecord)`
convenience method to localize and format the message field.
Specified by:
`format` in class `Formatter`
Parameters:
`record` - the log record to be formatted.
Returns:
a formatted log record




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

