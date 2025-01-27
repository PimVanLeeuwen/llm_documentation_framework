#### getString

```
public final String getString(String key)
```
Gets a string for the given key from this resource bundle or one of its parents.
Calling this method is equivalent to calling`(String) getObject(key)`.
Parameters:
`key` - the key for the desired string
Returns:
the string for the given key
Throws:
`NullPointerException` - if `key` is `null`
`MissingResourceException` - if no object for the given key can be found
`ClassCastException` - if the object found for the given key is not a string

