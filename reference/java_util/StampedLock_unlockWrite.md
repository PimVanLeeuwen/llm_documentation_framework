#### unlockWrite

```
public void unlockWrite(long stamp)
```
If the lock state matches the given stamp, releases the
exclusive lock.
Parameters:
`stamp` - a stamp returned by a write-lock operation
Throws:
`IllegalMonitorStateException` - if the stamp does
not match the current state of this lock

