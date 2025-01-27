#### listIterator

```
public ListIterator<E> listIterator(int index)
```
Returns a list iterator over the elements in this list (in proper
sequence), starting at the specified position in the list.
The specified index indicates the first element that would be
returned by an initial call to `next`.
An initial call to `previous` would
return the element with the specified index minus one.The returned iterator provides a snapshot of the state of the list
when the iterator was constructed. No synchronization is needed while
traversing the iterator. The iterator does NOT support the
`remove`, `set` or `add` methods.
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

