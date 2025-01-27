#### hasWaitingConsumer

```
public boolean hasWaitingConsumer()
```
Description copied from interface: `TransferQueue`
Returns `true` if there is at least one consumer waiting
to receive an element via `BlockingQueue.take()` or
timed `poll`.
The return value represents a momentary state of affairs.
Specified by:
`hasWaitingConsumer` in interface `TransferQueue<E>`
Returns:
`true` if there is at least one waiting consumer

