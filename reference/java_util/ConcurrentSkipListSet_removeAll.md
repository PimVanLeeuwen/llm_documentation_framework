#### removeAll

```
public boolean removeAll(Collection<?> c)
```
Removes from this set all of its elements that are contained in
the specified collection. If the specified collection is also
a set, this operation effectively modifies this set so that its
value is the asymmetric set difference of the two sets.
Specified by:
`removeAll` in interface `Collection<E>`
Specified by:
`removeAll` in interface `Set<E>`
Overrides:
`removeAll` in class `AbstractSet<E>`
Parameters:
`c` - collection containing elements to be removed from this set
Returns:
`true` if this set changed as a result of the call
Throws:
`ClassCastException` - if the types of one or more elements in this
set are incompatible with the specified collection
`NullPointerException` - if the specified collection or any
of its elements are null
See Also:
`AbstractCollection.remove(Object)`,
`AbstractCollection.contains(Object)`

