#### getWaitingConsumerCount

```
int getWaitingConsumerCount()
```
Returns an estimate of the number of consumers waiting to
receive elements via `BlockingQueue.take()` or timed
`poll`. The return value is an
approximation of a momentary state of affairs, that may be
inaccurate if consumers have completed or given up waiting.
The value may be useful for monitoring and heuristics, but
not for synchronization control. Implementations of this
method are likely to be noticeably slower than those for
`hasWaitingConsumer()`.
Returns:
the number of consumers waiting to receive elements




