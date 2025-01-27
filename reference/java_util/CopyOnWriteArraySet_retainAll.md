#### retainAll

```
public boolean retainAll(Collection<?> c)
```
Retains only the elements in this set that are contained in the
specified collection. In other words, removes from this set all of
its elements that are not contained in the specified collection. If
the specified collection is also a set, this operation effectively
modifies this set so that its value is the intersection of the
two sets.
Specified by:
`retainAll` in interface `Collection<E>`
Specified by:
`retainAll` in interface `Set<E>`
Overrides:
`retainAll` in class `AbstractCollection<E>`
Parameters:
`c` - collection containing elements to be retained in this set
Returns:
`true` if this set changed as a result of the call
Throws:
`ClassCastException` - if the class of an element of this set
is incompatible with the specified collection (optional)
`NullPointerException` - if this set contains a null element and the
specified collection does not permit null elements (optional),
or if the specified collection is null
See Also:
`remove(Object)`

