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
