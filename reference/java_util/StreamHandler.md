```
public class StreamHandler
extends Handler
```
Stream based logging Handler.This is primarily intended as a base class or support class to
be used in implementing other logging Handlers.LogRecords are published to a given java.io.OutputStream.Configuration:
By default each StreamHandler is initialized using the following
LogManager configuration properties where <handler-name>
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
the default platform encoding).For example, the properties for `StreamHandler` would be:java.util.logging.StreamHandler.level=INFOjava.util.logging.StreamHandler.formatter=java.util.logging.SimpleFormatterFor a custom handler, e.g. com.foo.MyHandler, the properties would be:com.foo.MyHandler.level=INFOcom.foo.MyHandler.formatter=java.util.logging.SimpleFormatter
Since:
1.4
