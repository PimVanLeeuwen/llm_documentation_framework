#### listIterator

```
public ListIterator<E> listIterator(int index)
```
Returns a list iterator over the elements in this list (in proper
sequence), starting at the specified position in the list.
The specified index indicates the first element that would be
returned by an initial call to `next`.
An initial call to `previous` would
return the element with the specified index minus one.This implementation returns a straightforward implementation of the
`ListIterator` interface that extends the implementation of the
`Iterator` interface returned by the `iterator()` method.
The `ListIterator` implementation relies on the backing list's
`get(int)`, `set(int, E)`, `add(int, E)`
and `remove(int)` methods.Note that the list iterator returned by this implementation will
throw an `UnsupportedOperationException` in response to its
`remove`, `set` and `add` methods unless the
list's `remove(int)`, `set(int, E)`, and
`add(int, E)` methods are overridden.This implementation can be made to throw runtime exceptions in the
face of concurrent modification, as described in the specification for
the (protected) `modCount` field.
Specified by:
`listIterator` in interface `List<E>`
Parameters:
`index` - index of the first element to be returned from the
list iterator (by a call to `next`)
Returns:
a list iterator over the elements in this list (in proper
sequence), starting at the specified position in the list
Throws:
`IndexOutOfBoundsException` - if the index is out of range
(`index < 0 || index > size()`)

