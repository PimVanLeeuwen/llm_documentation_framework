#### offer

```
public boolean offer(E e)
```
Inserts the specified element at the tail of this queue if it is
possible to do so immediately without exceeding the queue's capacity,
returning `true` upon success and `false` if this queue
is full.
When using a capacity-restricted queue, this method is generally
preferable to method `add`, which can fail to
insert an element only by throwing an exception.
Specified by:
`offer` in interface `BlockingQueue<E>`
Specified by:
`offer` in interface `Queue<E>`
Parameters:
`e` - the element to add
Returns:
`true` if the element was added to this queue, else
`false`
Throws:
`NullPointerException` - if the specified element is null

