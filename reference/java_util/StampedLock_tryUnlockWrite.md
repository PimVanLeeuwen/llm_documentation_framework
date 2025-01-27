#### tryUnlockWrite

```
public boolean tryUnlockWrite()
```
Releases the write lock if it is held, without requiring a
stamp value. This method may be useful for recovery after
errors.
Returns:
`true` if the lock was held, else false

