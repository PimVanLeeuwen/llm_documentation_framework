#### addAll

```
public boolean addAll(Collection<? extends E> c)
```
Adds all of the elements in the specified collection to this set.
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
`ClassCastException` - if the elements provided cannot be compared
with the elements currently in the set
`NullPointerException` - if the specified collection is null or
if any element is null and this set uses natural ordering, or
its comparator does not permit null elements
See Also:
`AbstractCollection.add(Object)`

