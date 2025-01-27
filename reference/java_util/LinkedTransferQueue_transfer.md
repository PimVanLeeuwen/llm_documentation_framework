#### transfer

```
public void transfer(E e)
              throws InterruptedException
```
Transfers the element to a consumer, waiting if necessary to do so.More precisely, transfers the specified element immediately
if there exists a consumer already waiting to receive it (in
`take()` or timed `poll`),
else inserts the specified element at the tail of this queue
and waits until the element is received by a consumer.
Specified by:
`transfer` in interface `TransferQueue<E>`
Parameters:
`e` - the element to transfer
Throws:
`NullPointerException` - if the specified element is null
`InterruptedException` - if interrupted while waiting,
in which case the element is not left enqueued

