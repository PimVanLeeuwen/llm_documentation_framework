#### transfer

```
void transfer(E e)
       throws InterruptedException
```
Transfers the element to a consumer, waiting if necessary to do so.More precisely, transfers the specified element immediately
if there exists a consumer already waiting to receive it (in
`BlockingQueue.take()` or timed `poll`),
else waits until the element is received by a consumer.
Parameters:
`e` - the element to transfer
Throws:
`InterruptedException` - if interrupted while waiting,
in which case the element is not left enqueued
`ClassCastException` - if the class of the specified element
prevents it from being added to this queue
`NullPointerException` - if the specified element is null
`IllegalArgumentException` - if some property of the specified
element prevents it from being added to this queue

