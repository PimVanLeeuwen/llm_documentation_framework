#### add

```
public boolean add(E e)
```
Inserts the specified element into this priority queue.
Specified by:
`add` in interface `Collection<E>`
Specified by:
`add` in interface `BlockingQueue<E>`
Specified by:
`add` in interface `Queue<E>`
Overrides:
`add` in class `AbstractQueue<E>`
Parameters:
`e` - the element to add
Returns:
`true` (as specified by `Collection.add(E)`)
Throws:
`ClassCastException` - if the specified element cannot be compared
with elements currently in the priority queue according to the
priority queue's ordering
`NullPointerException` - if the specified element is null

