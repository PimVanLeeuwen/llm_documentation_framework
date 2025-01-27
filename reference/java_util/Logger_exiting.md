#### exiting

```
public void exiting(String sourceClass,
                    String sourceMethod,
                    Object result)
```
Log a method return, with result object.This is a convenience method that can be used to log returning
from a method. A LogRecord with message "RETURN {0}", log level
FINER, and the gives sourceMethod, sourceClass, and result
object is logged.
Parameters:
`sourceClass` - name of class that issued the logging request
`sourceMethod` - name of the method
`result` - Object that is being returned

