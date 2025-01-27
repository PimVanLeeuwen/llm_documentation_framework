#### logp

```
public void logp(Level level,
                 String sourceClass,
                 String sourceMethod,
                 Throwable thrown,
                 Supplier<String> msgSupplier)
```
Log a lazily constructed message, specifying source class and method,
with associated Throwable information.If the logger is currently enabled for the given message level then the
message is constructed by invoking the provided supplier function. The
message and the given `Throwable` are then stored in a `LogRecord` which is forwarded to all registered output handlers.Note that the thrown argument is stored in the LogRecord thrown
property, rather than the LogRecord parameters property. Thus it is
processed specially by output Formatters and is not treated
as a formatting parameter to the LogRecord message property.
Parameters:
`level` - One of the message level identifiers, e.g., SEVERE
`sourceClass` - name of class that issued the logging request
`sourceMethod` - name of method that issued the logging request
`thrown` - Throwable associated with log message.
`msgSupplier` - A function, which when called, produces the
desired log message
Since:
1.8

