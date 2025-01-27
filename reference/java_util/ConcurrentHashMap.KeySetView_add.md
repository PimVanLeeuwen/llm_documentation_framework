#### add

```
public boolean add(K e)
```
Adds the specified key to this set view by mapping the key to
the default mapped value in the backing map, if defined.
Specified by:
`add` in interface `Collection<K>`
Specified by:
`add` in interface `Set<K>`
Parameters:
`e` - key to be added
Returns:
`true` if this set changed as a result of the call
Throws:
`NullPointerException` - if the specified key is null
`UnsupportedOperationException` - if no default mapped value
for additions was provided

