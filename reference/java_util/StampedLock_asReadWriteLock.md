#### asReadWriteLock

```
public ReadWriteLock asReadWriteLock()
```
Returns a `ReadWriteLock` view of this StampedLock in
which the `ReadWriteLock.readLock()` method is mapped to
`asReadLock()`, and `ReadWriteLock.writeLock()` to
`asWriteLock()`.
Returns:
the lock




