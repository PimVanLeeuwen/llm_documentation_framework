#### getObject

```
public final Object getObject(String key)
```
Gets an object for the given key from this resource bundle or one of its parents.
This method first tries to obtain the object from this resource bundle using
`handleGetObject`.
If not successful, and the parent resource bundle is not null,
it calls the parent's `getObject` method.
If still not successful, it throws a MissingResourceException.
Parameters:
`key` - the key for the desired object
Returns:
the object for the given key
Throws:
`NullPointerException` - if `key` is `null`
`MissingResourceException` - if no object for the given key can be found

