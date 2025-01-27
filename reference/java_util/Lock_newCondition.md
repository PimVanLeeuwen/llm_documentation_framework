#### newCondition

```
Condition newCondition()
```
Returns a new `Condition` instance that is bound to this
`Lock` instance.Before waiting on the condition the lock must be held by the
current thread.
A call to `Condition.await()` will atomically release the lock
before waiting and re-acquire the lock before the wait returns.Implementation ConsiderationsThe exact operation of the `Condition` instance depends on
the `Lock` implementation and must be documented by that
implementation.
Returns:
A new `Condition` instance for this `Lock` instance
Throws:
`UnsupportedOperationException` - if this `Lock`
implementation does not support conditions




