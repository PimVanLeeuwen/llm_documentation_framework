#### logrb

```
public void logrb(Level level,
                  String sourceClass,
                  String sourceMethod,
                  ResourceBundle bundle,
                  String msg,
                  Throwable thrown)
```
Log a message, specifying source class, method, and resource bundle,
with associated Throwable information.If the logger is currently enabled for the given message
level then the given arguments are stored in a LogRecord
which is forwarded to all registered output handlers.The `msg` string is localized using the given resource bundle.
If the resource bundle is `null`, then the `msg` string is not
localized.Note that the thrown argument is stored in the LogRecord thrown
property, rather than the LogRecord parameters property. Thus it is
processed specially by output Formatters and is not treated
as a formatting parameter to the LogRecord message property.
Parameters:
`level` - One of the message level identifiers, e.g., SEVERE
`sourceClass` - Name of the class that issued the logging request
`sourceMethod` - Name of the method that issued the logging request
`bundle` - Resource bundle to localize `msg`,
can be `null`
`msg` - The string message (or a key in the message catalog)
`thrown` - Throwable associated with the log message.
Since:
1.8

