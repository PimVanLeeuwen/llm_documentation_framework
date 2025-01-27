#### isHeldByCurrentThread

```
public boolean isHeldByCurrentThread()
```
Queries if this write lock is held by the current thread.
Identical in effect to `ReentrantReadWriteLock.isWriteLockedByCurrentThread()`.
Returns:
`true` if the current thread holds this lock and
`false` otherwise
Since:
1.6

