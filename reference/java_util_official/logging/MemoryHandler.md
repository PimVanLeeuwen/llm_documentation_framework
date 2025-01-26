

MemoryHandler (Java Platform SE 8 )












<!--
try {
if (location.href.indexOf('is-external=true') == -1) {
parent.document.title="MemoryHandler (Java Platform SE 8 )";
}
}
catch(err) {
}
//-->
var methods = {"i0":10,"i1":10,"i2":10,"i3":10,"i4":10,"i5":10,"i6":10};
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
java.util.loggingClass MemoryHandler
java.lang.Objectjava.util.logging.Handlerjava.util.logging.MemoryHandler
```
public class MemoryHandler
extends Handler
```
Handler that buffers requests in a circular buffer in memory.Normally this Handler simply stores incoming LogRecords
into its memory buffer and discards earlier records. This buffering
is very cheap and avoids formatting costs. On certain trigger
conditions, the MemoryHandler will push out its current buffer
contents to a target Handler, which will typically publish
them to the outside world.There are three main models for triggering a push of the buffer:An incoming LogRecord has a type that is greater than
a pre-defined level, the pushLevel.An external class calls the push method explicitly.A subclass overrides the log method and scans each incoming
LogRecord and calls push if a record matches some
desired criteria.Configuration:
By default each MemoryHandler is initialized using the following
LogManager configuration properties where <handler-name>
refers to the fully-qualified class name of the handler.
If properties are not defined
(or have invalid values) then the specified default values are used.
If no default value is defined then a RuntimeException is thrown.<handler-name>.level
specifies the level for the Handler
(defaults to Level.ALL).<handler-name>.filter
specifies the name of a Filter class to use
(defaults to no Filter).<handler-name>.size
defines the buffer size (defaults to 1000).<handler-name>.push
defines the pushLevel (defaults to level.SEVERE).<handler-name>.target
specifies the name of the target Handler  class.
(no default).For example, the properties for `MemoryHandler` would be:java.util.logging.MemoryHandler.level=INFOjava.util.logging.MemoryHandler.formatter=java.util.logging.SimpleFormatterFor a custom handler, e.g. com.foo.MyHandler, the properties would be:com.foo.MyHandler.level=INFOcom.foo.MyHandler.formatter=java.util.logging.SimpleFormatter
Since:
1.4

### Constructor Summary

Constructors Constructor and Description`MemoryHandler()`
Create a MemoryHandler and configure it based on
LogManager configuration properties.`MemoryHandler(Handler target,
int size,
Level pushLevel)`
Create a MemoryHandler.

### Method Summary

All Methods Instance Methods Concrete Methods Modifier and TypeMethod and Description`void``close()`
Close the Handler and free all associated resources.`void``flush()`
Causes a flush on the target Handler.`Level``getPushLevel()`
Get the pushLevel.`boolean``isLoggable(LogRecord record)`
Check if this Handler would actually log a given
LogRecord into its internal buffer.`void``publish(LogRecord record)`
Store a LogRecord in an internal buffer.`void``push()`
Push any buffered output to the target Handler.`void``setPushLevel(Level newLevel)`
Set the pushLevel.

### Methods inherited from class java.util.logging.Handler

`getEncoding, getErrorManager, getFilter, getFormatter, getLevel, reportError, setEncoding, setErrorManager, setFilter, setFormatter, setLevel`

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

### Constructor Detail

#### MemoryHandler

```
public MemoryHandler()
```
Create a MemoryHandler and configure it based on
LogManager configuration properties.

#### MemoryHandler

```
public MemoryHandler(Handler target,
                     int size,
                     Level pushLevel)
```
Create a MemoryHandler.The MemoryHandler is configured based on LogManager
properties (or their default values) except that the given pushLevel
argument and buffer size argument are used.
Parameters:
`target` - the Handler to which to publish output.
`size` - the number of log records to buffer (must be greater than zero)
`pushLevel` - message level to push on
Throws:
`IllegalArgumentException` - if `size is <= 0`

### Method Detail

#### publish

```
public void publish(LogRecord record)
```
Store a LogRecord in an internal buffer.If there is a Filter, its isLoggable
method is called to check if the given log record is loggable.
If not we return. Otherwise the given record is copied into
an internal circular buffer. Then the record's level property is
compared with the pushLevel. If the given level is
greater than or equal to the pushLevel then push
is called to write all buffered records to the target output
Handler.
Specified by:
`publish` in class `Handler`
Parameters:
`record` - description of the log event. A null record is
silently ignored and is not published

#### push

```
public void push()
```
Push any buffered output to the target Handler.The buffer is then cleared.

#### flush

```
public void flush()
```
Causes a flush on the target Handler.Note that the current contents of the MemoryHandler
buffer are not written out. That requires a "push".
Specified by:
`flush` in class `Handler`

#### close

```
public void close()
           throws SecurityException
```
Close the Handler and free all associated resources.
This will also close the target Handler.
Specified by:
`close` in class `Handler`
Throws:
`SecurityException` - if a security manager exists and if
the caller does not have LoggingPermission("control").

#### setPushLevel

```
public void setPushLevel(Level newLevel)
                  throws SecurityException
```
Set the pushLevel. After a LogRecord is copied
into our internal buffer, if its level is greater than or equal to
the pushLevel, then push will be called.
Parameters:
`newLevel` - the new value of the pushLevel
Throws:
`SecurityException` - if a security manager exists and if
the caller does not have LoggingPermission("control").

#### getPushLevel

```
public Level getPushLevel()
```
Get the pushLevel.
Returns:
the value of the pushLevel

#### isLoggable

```
public boolean isLoggable(LogRecord record)
```
Check if this Handler would actually log a given
LogRecord into its internal buffer.This method checks if the LogRecord has an appropriate level and
whether it satisfies any Filter. However it does not
check whether the LogRecord would result in a "push" of the
buffer contents. It will return false if the LogRecord is null.
Overrides:
`isLoggable` in class `Handler`
Parameters:
`record` - a LogRecord
Returns:
true if the LogRecord would be logged.




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

