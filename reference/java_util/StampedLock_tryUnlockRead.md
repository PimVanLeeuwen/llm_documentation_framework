#### tryUnlockRead

```
public boolean tryUnlockRead()
```
Releases one hold of the read lock if it is held, without
requiring a stamp value. This method may be useful for recovery
after errors.
Returns:
`true` if the read lock was held, else false

