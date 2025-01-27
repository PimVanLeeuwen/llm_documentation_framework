#### removePropertyChangeListener

```
@Deprecated
default void removePropertyChangeListener(PropertyChangeListener listener)
```
Deprecated. The dependency on `PropertyChangeListener` creates
a significant impediment to future modularization of the
Java platform. This method will be removed in a future
release.
Remove a listener for PropertyChange events, added by
the `addPropertyChangeListener(java.beans.PropertyChangeListener)`.The default implementation of this method does nothing and has
no side-effects.WARNING: This method is omitted from the interface
declaration in all subset Profiles of Java SE that do not include
the `java.beans` package.
Parameters:
`listener` - The PropertyChange listener to be removed.
See Also:
`addPropertyChangeListener(java.beans.PropertyChangeListener)`




