#### remove

```
public abstract V remove(Object key)
```
Removes the `key` (and its corresponding
`value`) from this dictionary. This method does nothing
if the `key` is not in this dictionary.
Parameters:
`key` - the key that needs to be removed.
Returns:
the value to which the `key` had been mapped in this
dictionary, or `null` if the key did not have a
mapping.
Throws:
`NullPointerException` - if key is null.




