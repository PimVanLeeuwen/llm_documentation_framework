#### lock

```
public void lock()
```
Acquires the lock.Acquires the lock if it is not held by another thread and returns
immediately, setting the lock hold count to one.If the current thread already holds the lock then the hold
count is incremented by one and the method returns immediately.If the lock is held by another thread then the
current thread becomes disabled for thread scheduling
purposes and lies dormant until the lock has been acquired,
at which time the lock hold count is set to one.
Specified by:
`lock` in interface `Lock`

