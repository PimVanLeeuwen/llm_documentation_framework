#### tryConvertToWriteLock

```
public long tryConvertToWriteLock(long stamp)
```
If the lock state matches the given stamp, performs one of
the following actions. If the stamp represents holding a write
lock, returns it. Or, if a read lock, if the write lock is
available, releases the read lock and returns a write stamp.
Or, if an optimistic read, returns a write stamp only if
immediately available. This method returns zero in all other
cases.
Parameters:
`stamp` - a stamp
Returns:
a valid write stamp, or zero on failure

