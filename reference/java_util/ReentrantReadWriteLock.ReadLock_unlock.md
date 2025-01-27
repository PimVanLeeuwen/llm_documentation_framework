#### unlock

```
public void unlock()
```
Attempts to release this lock.If the number of readers is now zero then the lock
is made available for write lock attempts.
Specified by:
`unlock` in interface `Lock`

