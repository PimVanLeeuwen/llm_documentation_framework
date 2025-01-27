#### setResourceBundle

```
public void setResourceBundle(ResourceBundle bundle)
```
Sets a resource bundle on this logger.
All messages will be logged using the given resource bundle for its
specific locale.
Parameters:
`bundle` - The resource bundle that this logger shall use.
Throws:
`NullPointerException` - if the given bundle is `null`.
`IllegalArgumentException` - if the given bundle doesn't have a
base name,
or if this logger already has a resource bundle set but
the given bundle has a different base name.
`SecurityException` - if a security manager exists,
this logger is not anonymous, and the caller
does not have LoggingPermission("control").
Since:
1.8

