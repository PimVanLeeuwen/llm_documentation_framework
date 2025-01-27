#### hasWaitingConsumer

```
boolean hasWaitingConsumer()
```
Returns `true` if there is at least one consumer waiting
to receive an element via `BlockingQueue.take()` or
timed `poll`.
The return value represents a momentary state of affairs.
Returns:
`true` if there is at least one waiting consumer

