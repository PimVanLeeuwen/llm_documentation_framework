```
public abstract class Handler
extends Object
```
A Handler object takes log messages from a Logger and
exports them. It might for example, write them to a console
or write them to a file, or send them to a network logging service,
or forward them to an OS log, or whatever.A Handler can be disabled by doing a setLevel(Level.OFF)
and can be re-enabled by doing a setLevel with an appropriate level.Handler classes typically use LogManager properties to set
default values for the Handler's Filter, Formatter,
and Level. See the specific documentation for each concrete
Handler class.
Since:
1.4
