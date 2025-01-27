#### removePropertyChangeListener

```
@Deprecated
public void removePropertyChangeListener(PropertyChangeListener l)
                                              throws SecurityException
```
Deprecated. The dependency on `PropertyChangeListener` creates a
significant impediment to future modularization of the Java
platform. This method will be removed in a future release.
The global `LogManager` can detect changes to the
logging configuration by overridding the `readConfiguration` method.
Removes an event listener for property change events.
If the same listener instance has been added to the listener table
through multiple invocations of `addPropertyChangeListener`,
then an equivalent number of
`removePropertyChangeListener` invocations are required to remove
all instances of that listener from the listener table.Returns silently if the given listener is not found.WARNING: This method is omitted from this class in all subset
Profiles of Java SE that do not include the `java.beans` package.
Parameters:
`l` - event listener (can be null)
Throws:
`SecurityException` - if a security manager exists and if
the caller does not have LoggingPermission("control").

