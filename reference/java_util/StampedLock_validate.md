#### validate

```
public boolean validate(long stamp)
```
Returns true if the lock has not been exclusively acquired
since issuance of the given stamp. Always returns false if the
stamp is zero. Always returns true if the stamp represents a
currently held lock. Invoking this method with a value not
obtained from `tryOptimisticRead()` or a locking method
for this lock has no defined effect or result.
Parameters:
`stamp` - a stamp
Returns:
`true` if the lock has not been exclusively acquired
since issuance of the given stamp; else false

