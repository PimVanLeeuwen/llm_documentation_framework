#### tryConvertToReadLock

```
public long tryConvertToReadLock(long stamp)
```
If the lock state matches the given stamp, performs one of
the following actions. If the stamp represents holding a write
lock, releases it and obtains a read lock. Or, if a read lock,
returns it. Or, if an optimistic read, acquires a read lock and
returns a read stamp only if immediately available. This method
returns zero in all other cases.
Parameters:
`stamp` - a stamp
Returns:
a valid read stamp, or zero on failure

