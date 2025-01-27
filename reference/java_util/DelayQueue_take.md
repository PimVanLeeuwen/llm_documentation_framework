#### take

```
public E take()
       throws InterruptedException
```
Retrieves and removes the head of this queue, waiting if necessary
until an element with an expired delay is available on this queue.
Specified by:
`take` in interface `BlockingQueue<E extends Delayed>`
Returns:
the head of this queue
Throws:
`InterruptedException` - if interrupted while waiting

