#### clear

```
public void clear()
```
Removes all of the mappings from this map (optional operation).
The map will be empty after this call returns.
Specified by:
`clear` in interface `Map<K,V>`
Implementation Requirements:
This implementation calls entrySet().clear().Note that this implementation throws an
UnsupportedOperationException if the entrySet
does not support the clear operation.
Throws:
`UnsupportedOperationException` - if the clear operation
is not supported by this map

