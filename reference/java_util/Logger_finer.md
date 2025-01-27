#### finer

```
public void finer(Supplier<String> msgSupplier)
```
Log a FINER message, which is only to be constructed if the logging
level is such that the message will actually be logged.If the logger is currently enabled for the FINER message
level then the message is constructed by invoking the provided
supplier function and forwarded to all the registered output
Handler objects.
Parameters:
`msgSupplier` - A function, which when called, produces the
desired log message
Since:
1.8

