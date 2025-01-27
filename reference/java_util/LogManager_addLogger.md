#### addLogger

```
public boolean addLogger(Logger logger)
```
Add a named logger. This does nothing and returns false if a logger
with the same name is already registered.The Logger factory methods call this method to register each
newly created Logger.The application should retain its own reference to the Logger
object to avoid it being garbage collected. The LogManager
may only retain a weak reference.
Parameters:
`logger` - the new logger.
Returns:
true if the argument logger was registered successfully,
false if a logger of that name already exists.
Throws:
`NullPointerException` - if the logger name is null.

