#### iterator

```
public Iterator<E> iterator()
```
Returns an iterator over the elements in this list in proper sequence.This implementation returns a straightforward implementation of the
iterator interface, relying on the backing list's `size()`,
`get(int)`, and `remove(int)` methods.Note that the iterator returned by this method will throw an
`UnsupportedOperationException` in response to its
`remove` method unless the list's `remove(int)` method is
overridden.This implementation can be made to throw runtime exceptions in the
face of concurrent modification, as described in the specification
for the (protected) `modCount` field.
Specified by:
`iterator` in interface `Iterable<E>`
Specified by:
`iterator` in interface `Collection<E>`
Specified by:
`iterator` in interface `List<E>`
Specified by:
`iterator` in class `AbstractCollection<E>`
Returns:
an iterator over the elements in this list in proper sequence

