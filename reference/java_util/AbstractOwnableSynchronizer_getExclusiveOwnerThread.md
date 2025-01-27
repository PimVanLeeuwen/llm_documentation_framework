#### getExclusiveOwnerThread

```
protected final Thread getExclusiveOwnerThread()
```
Returns the thread last set by `setExclusiveOwnerThread`,
or `null` if never set. This method does not otherwise
impose any synchronization or `volatile` field accesses.
Returns:
the owner thread




