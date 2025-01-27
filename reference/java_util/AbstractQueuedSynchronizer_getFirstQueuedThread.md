#### getFirstQueuedThread

```
public final Thread getFirstQueuedThread()
```
Returns the first (longest-waiting) thread in the queue, or
`null` if no threads are currently queued.In this implementation, this operation normally returns in
constant time, but may iterate upon contention if other threads are
concurrently modifying the queue.
Returns:
the first (longest-waiting) thread in the queue, or
`null` if no threads are currently queued

