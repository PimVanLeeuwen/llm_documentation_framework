#### offer

```
public boolean offer(E e,
                     long timeout,
                     TimeUnit unit)
```
Inserts the specified element into this delay queue. As the queue is
unbounded this method will never block.
Specified by:
`offer` in interface `BlockingQueue<E extends Delayed>`
Parameters:
`e` - the element to add
`timeout` - This parameter is ignored as the method never blocks
`unit` - This parameter is ignored as the method never blocks
Returns:
`true`
Throws:
`NullPointerException` - if the specified element is null

