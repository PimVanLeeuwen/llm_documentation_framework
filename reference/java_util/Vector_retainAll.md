#### retainAll

```
public boolean retainAll(Collection<?> c)
```
Retains only the elements in this Vector that are contained in the
specified Collection. In other words, removes from this Vector all
of its elements that are not contained in the specified Collection.
Specified by:
`retainAll` in interface `Collection<E>`
Specified by:
`retainAll` in interface `List<E>`
Overrides:
`retainAll` in class `AbstractCollection<E>`
Parameters:
`c` - a collection of elements to be retained in this Vector
(all other elements are removed)
Returns:
true if this Vector changed as a result of the call
Throws:
`ClassCastException` - if the types of one or more elements
in this vector are incompatible with the specified
collection
(optional)
`NullPointerException` - if this vector contains one or more null
elements and the specified collection does not support null
elements
(optional),
or if the specified collection is null
Since:
1.2
See Also:
`AbstractCollection.remove(Object)`,
`AbstractCollection.contains(Object)`

