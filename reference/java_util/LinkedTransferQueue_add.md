#### add

```
public boolean add(E e)
```
Inserts the specified element at the tail of this queue.
As the queue is unbounded, this method will never throw
`IllegalStateException` or return `false`.
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
`NullPointerException` - if the specified element is null

