#### addAll

```
public boolean addAll(Collection<? extends E> c)
```
Appends all of the elements in the specified collection to the end of
this queue, in the order that they are returned by the specified
collection's iterator. Attempts to `addAll` of a queue to
itself result in `IllegalArgumentException`.
Specified by:
`addAll` in interface `Collection<E>`
Overrides:
`addAll` in class `AbstractQueue<E>`
Parameters:
`c` - the elements to be inserted into this queue
Returns:
`true` if this queue changed as a result of the call
Throws:
`NullPointerException` - if the specified collection or any
of its elements are null
`IllegalArgumentException` - if the collection is this queue
See Also:
`AbstractQueue.add(Object)`

