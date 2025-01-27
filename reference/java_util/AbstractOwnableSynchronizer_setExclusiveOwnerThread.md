#### setExclusiveOwnerThread

```
protected final void setExclusiveOwnerThread(Thread thread)
```
Sets the thread that currently owns exclusive access.
A `null` argument indicates that no thread owns access.
This method does not otherwise impose any synchronization or
`volatile` field accesses.
Parameters:
`thread` - the owner thread

