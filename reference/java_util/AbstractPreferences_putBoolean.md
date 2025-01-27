#### putBoolean

```
public void putBoolean(String key,
                       boolean value)
```
Implements the putBoolean method as per the specification in
`Preferences.putBoolean(String,boolean)`.This implementation translates value to a string with
`String.valueOf(boolean)` and invokes `put(String,String)`
on the result.
Specified by:
`putBoolean` in class `Preferences`
Parameters:
`key` - key with which the string form of value is to be associated.
`value` - value whose string form is to be associated with key.
Throws:
`NullPointerException` - if key is null.
`IllegalArgumentException` - if key.length() exceeds
MAX\_KEY\_LENGTH.
`IllegalStateException` - if this node (or an ancestor) has been
removed with the `removeNode()` method.
See Also:
`Preferences.getBoolean(String,boolean)`,
`Preferences.get(String,String)`

