#### unlockRead

```
public void unlockRead(long stamp)
```
If the lock state matches the given stamp, releases the
non-exclusive lock.
Parameters:
`stamp` - a stamp returned by a read-lock operation
Throws:
`IllegalMonitorStateException` - if the stamp does
not match the current state of this lock

