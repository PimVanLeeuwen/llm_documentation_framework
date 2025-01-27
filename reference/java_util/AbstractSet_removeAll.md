#### removeAll

```
public boolean removeAll(Collection<?> c)
```
Removes from this set all of its elements that are contained in the
specified collection (optional operation). If the specified
collection is also a set, this operation effectively modifies this
set so that its value is the asymmetric set difference of
the two sets.This implementation determines which is the smaller of this set
and the specified collection, by invoking the size
method on each. If this set has fewer elements, then the
implementation iterates over this set, checking each element
returned by the iterator in turn to see if it is contained in
the specified collection. If it is so contained, it is removed
from this set with the iterator's remove method. If
the specified collection has fewer elements, then the
implementation iterates over the specified collection, removing
from this set each element returned by the iterator, using this
set's remove method.Note that this implementation will throw an
UnsupportedOperationException if the iterator returned by the
iterator method does not implement the remove method.
Specified by:
`removeAll` in interface `Collection<E>`
Specified by:
`removeAll` in interface `Set<E>`
Overrides:
`removeAll` in class `AbstractCollection<E>`
Parameters:
`c` - collection containing elements to be removed from this set
Returns:
true if this set changed as a result of the call
Throws:
`UnsupportedOperationException` - if the removeAll operation
is not supported by this set
`ClassCastException` - if the class of an element of this set
is incompatible with the specified collection
(optional)
`NullPointerException` - if this set contains a null element and the
specified collection does not permit null elements
(optional),
or if the specified collection is null
See Also:
`AbstractCollection.remove(Object)`,
`AbstractCollection.contains(Object)`




