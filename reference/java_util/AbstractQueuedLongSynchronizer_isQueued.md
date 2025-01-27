#### isQueued

```
public final boolean isQueued(Thread thread)
```
Returns true if the given thread is currently queued.This implementation traverses the queue to determine
presence of the given thread.
Parameters:
`thread` - the thread
Returns:
`true` if the given thread is on the queue
Throws:
`NullPointerException` - if the thread is null

