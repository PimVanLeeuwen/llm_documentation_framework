#### put

```
public void put(E e)
```
Inserts the specified element into this priority queue.
As the queue is unbounded, this method will never block.
Specified by:
`put` in interface `BlockingQueue<E>`
Parameters:
`e` - the element to add
Throws:
`ClassCastException` - if the specified element cannot be compared
with elements currently in the priority queue according to the
priority queue's ordering
`NullPointerException` - if the specified element is null

