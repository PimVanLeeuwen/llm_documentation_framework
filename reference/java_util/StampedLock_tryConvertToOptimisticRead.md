#### tryConvertToOptimisticRead

```
public long tryConvertToOptimisticRead(long stamp)
```
If the lock state matches the given stamp then, if the stamp
represents holding a lock, releases it and returns an
observation stamp. Or, if an optimistic read, returns it if
validated. This method returns zero in all other cases, and so
may be useful as a form of "tryUnlock".
Parameters:
`stamp` - a stamp
Returns:
a valid optimistic read stamp, or zero on failure

