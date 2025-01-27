```
public class SocketHandler
extends StreamHandler
```
Simple network logging Handler.LogRecords are published to a network stream connection. By default
the XMLFormatter class is used for formatting.Configuration:
By default each SocketHandler is initialized using the following
LogManager configuration properties where <handler-name>
refers to the fully-qualified class name of the handler.
If properties are not defined
(or have invalid values) then the specified default values are used.<handler-name>.level
specifies the default level for the Handler
(defaults to Level.ALL).<handler-name>.filter
specifies the name of a Filter class to use
(defaults to no Filter).<handler-name>.formatter
specifies the name of a Formatter class to use
(defaults to java.util.logging.XMLFormatter).<handler-name>.encoding
the name of the character set encoding to use (defaults to
the default platform encoding).<handler-name>.host
specifies the target host name to connect to (no default).<handler-name>.port
specifies the target TCP port to use (no default).For example, the properties for `SocketHandler` would be:java.util.logging.SocketHandler.level=INFOjava.util.logging.SocketHandler.formatter=java.util.logging.SimpleFormatterFor a custom handler, e.g. com.foo.MyHandler, the properties would be:com.foo.MyHandler.level=INFOcom.foo.MyHandler.formatter=java.util.logging.SimpleFormatterThe output IO stream is buffered, but is flushed after each
LogRecord is written.
Since:
1.4
