#### setErrorManager

```
public void setErrorManager(ErrorManager em)
```
Define an ErrorManager for this Handler.The ErrorManager's "error" method will be invoked if any
errors occur while using this Handler.
Parameters:
`em` - the new ErrorManager
Throws:
`SecurityException` - if a security manager exists and if
the caller does not have LoggingPermission("control").

