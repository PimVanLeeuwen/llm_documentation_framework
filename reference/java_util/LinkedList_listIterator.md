#### listIterator

```
public ListIterator<E> listIterator(int index)
```
Returns a list-iterator of the elements in this list (in proper
sequence), starting at the specified position in the list.
Obeys the general contract of `List.listIterator(int)`.The list-iterator is fail-fast: if the list is structurally
modified at any time after the Iterator is created, in any way except
through the list-iterator's own `remove` or `add`
methods, the list-iterator will throw a
`ConcurrentModificationException`. Thus, in the face of
concurrent modification, the iterator fails quickly and cleanly, rather
than risking arbitrary, non-deterministic behavior at an undetermined
time in the future.
Specified by:
`listIterator` in interface `List<E>`
Specified by:
`listIterator` in class `AbstractSequentialList<E>`
Parameters:
`index` - index of the first element to be returned from the
list-iterator (by a call to `next`)
Returns:
a ListIterator of the elements in this list (in proper
sequence), starting at the specified position in the list
Throws:
`IndexOutOfBoundsException` - if the index is out of range
(`index < 0 || index > size()`)
See Also:
`List.listIterator(int)`

