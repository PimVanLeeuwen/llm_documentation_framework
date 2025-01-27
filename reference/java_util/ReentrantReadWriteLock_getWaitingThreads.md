#### getWaitingThreads

```
protected Collection<Thread> getWaitingThreads(Condition condition)
```
Returns a collection containing those threads that may be
waiting on the given condition associated with the write lock.
Because the actual set of threads may change dynamically while
constructing this result, the returned collection is only a
best-effort estimate. The elements of the returned collection
are in no particular order. This method is designed to
facilitate construction of subclasses that provide more
extensive condition monitoring facilities.
Parameters:
`condition` - the condition
Returns:
the collection of threads
Throws:
`IllegalMonitorStateException` - if this lock is not held
`IllegalArgumentException` - if the given condition is
not associated with this lock
`NullPointerException` - if the condition is null

