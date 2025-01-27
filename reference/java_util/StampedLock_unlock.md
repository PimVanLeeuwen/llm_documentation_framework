#### unlock

```
public void unlock(long stamp)
```
If the lock state matches the given stamp, releases the
corresponding mode of the lock.
Parameters:
`stamp` - a stamp returned by a lock operation
Throws:
`IllegalMonitorStateException` - if the stamp does
not match the current state of this lock

