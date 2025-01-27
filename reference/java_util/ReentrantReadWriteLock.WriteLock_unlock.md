#### unlock

```
public void unlock()
```
Attempts to release this lock.If the current thread is the holder of this lock then
the hold count is decremented. If the hold count is now
zero then the lock is released. If the current thread is
not the holder of this lock then `IllegalMonitorStateException` is thrown.
Specified by:
`unlock` in interface `Lock`
Throws:
`IllegalMonitorStateException` - if the current thread does not
hold this lock

