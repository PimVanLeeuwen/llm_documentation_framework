#### addPropertyChangeListener

```
@Deprecated
default void addPropertyChangeListener(PropertyChangeListener listener)
```
Deprecated. The dependency on `PropertyChangeListener` creates
a significant impediment to future modularization of the
Java platform. This method will be removed in a future
release.
Applications that need to monitor progress of the
unpacker can poll the value of the `PROGRESS` property instead.
Registers a listener for PropertyChange events on the properties map.
This is typically used by applications to update a progress bar.The default implementation of this method does nothing and has
no side-effects.WARNING: This method is omitted from the interface
declaration in all subset Profiles of Java SE that do not include
the `java.beans` package.
Parameters:
`listener` - An object to be invoked when a property is changed.
See Also:
`properties()`,
`PROGRESS`

