#### addAll

```
public boolean addAll(Collection<? extends E> c)
```
Adds all of the elements in the specified collection to this set if
they're not already present. If the specified collection is also a
set, the `addAll` operation effectively modifies this set so
that its value is the union of the two sets. The behavior of
this operation is undefined if the specified collection is modified
while the operation is in progress.
Specified by:
`addAll` in interface `Collection<E>`
Specified by:
`addAll` in interface `Set<E>`
Overrides:
`addAll` in class `AbstractCollection<E>`
Parameters:
`c` - collection containing elements to be added to this set
Returns:
`true` if this set changed as a result of the call
Throws:
`NullPointerException` - if the specified collection is null
See Also:
`add(Object)`

