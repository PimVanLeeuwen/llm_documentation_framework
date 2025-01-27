#### asReadLock

```
public Lock asReadLock()
```
Returns a plain `Lock` view of this StampedLock in which
the `Lock.lock()` method is mapped to `readLock()`,
and similarly for other methods. The returned Lock does not
support a `Condition`; method `Lock.newCondition()` throws `UnsupportedOperationException`.
Returns:
the lock

