#### putDouble

```
public void putDouble(String key,
                      double value)
```
Implements the putDouble method as per the specification in
`Preferences.putDouble(String,double)`.This implementation translates value to a string with
`Double.toString(double)` and invokes `put(String,String)`
on the result.
Specified by:
`putDouble` in class `Preferences`
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
`Preferences.getDouble(String,double)`

