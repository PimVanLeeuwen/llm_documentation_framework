#### putFloat

```
public void putFloat(String key,
                     float value)
```
Implements the putFloat method as per the specification in
`Preferences.putFloat(String,float)`.This implementation translates value to a string with
`Float.toString(float)` and invokes `put(String,String)`
on the result.
Specified by:
`putFloat` in class `Preferences`
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
`Preferences.getFloat(String,float)`

