#### addAll

```
public boolean addAll(Collection<? extends K> c)
```
Adds all of the elements in the specified collection to this set,
as if by calling `add(K)` on each one.
Specified by:
`addAll` in interface `Collection<K>`
Specified by:
`addAll` in interface `Set<K>`
Parameters:
`c` - the elements to be inserted into this set
Returns:
`true` if this set changed as a result of the call
Throws:
`NullPointerException` - if the collection or any of its
elements are `null`
`UnsupportedOperationException` - if no default mapped value
for additions was provided
See Also:
`Set.add(Object)`

