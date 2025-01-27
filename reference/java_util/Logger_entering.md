#### entering

```
public void entering(String sourceClass,
                     String sourceMethod,
                     Object[] params)
```
Log a method entry, with an array of parameters.This is a convenience method that can be used to log entry
to a method. A LogRecord with message "ENTRY" (followed by a
format {N} indicator for each entry in the parameter array),
log level FINER, and the given sourceMethod, sourceClass, and
parameters is logged.
Parameters:
`sourceClass` - name of class that issued the logging request
`sourceMethod` - name of method that is being entered
`params` - array of parameters to the method being entered

