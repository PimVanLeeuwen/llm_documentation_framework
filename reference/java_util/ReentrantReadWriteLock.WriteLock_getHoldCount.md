#### getHoldCount

```
public int getHoldCount()
```
Queries the number of holds on this write lock by the current
thread. A thread has a hold on a lock for each lock action
that is not matched by an unlock action. Identical in effect
to `ReentrantReadWriteLock.getWriteHoldCount()`.
Returns:
the number of holds on this lock by the current thread,
or zero if this lock is not held by the current thread
Since:
1.6




