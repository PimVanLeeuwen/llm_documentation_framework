#### add

```
public boolean add(E e)
```
Inserts the specified element at the tail of this queue if it is
possible to do so immediately without exceeding the queue's capacity,
returning `true` upon success and throwing an
`IllegalStateException` if this queue is full.
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
`IllegalStateException` - if this queue is full
`NullPointerException` - if the specified element is null

