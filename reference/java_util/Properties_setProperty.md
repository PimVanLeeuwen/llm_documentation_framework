#### setProperty

```
public Object setProperty(String key,
                          String value)
```
Calls the Hashtable method `put`. Provided for
parallelism with the getProperty method. Enforces use of
strings for property keys and values. The value returned is the
result of the Hashtable call to `put`.
Parameters:
`key` - the key to be placed into this property list.
`value` - the value corresponding to key.
Returns:
the previous value of the specified key in this property
list, or `null` if it did not have one.
Since:
1.2
See Also:
`getProperty(java.lang.String)`

