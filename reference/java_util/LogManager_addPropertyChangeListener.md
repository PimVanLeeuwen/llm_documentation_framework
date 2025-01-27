#### addPropertyChangeListener

```
@Deprecated
public void addPropertyChangeListener(PropertyChangeListener l)
                                           throws SecurityException
```
Deprecated. The dependency on `PropertyChangeListener` creates a
significant impediment to future modularization of the Java
platform. This method will be removed in a future release.
The global `LogManager` can detect changes to the
logging configuration by overridding the `readConfiguration` method.
Adds an event listener to be invoked when the logging
properties are re-read. Adding multiple instances of
the same event Listener results in multiple entries
in the property event listener table.WARNING: This method is omitted from this class in all subset
Profiles of Java SE that do not include the `java.beans` package.
Parameters:
`l` - event listener
Throws:
`SecurityException` - if a security manager exists and if
the caller does not have LoggingPermission("control").
`NullPointerException` - if the PropertyChangeListener is null.

