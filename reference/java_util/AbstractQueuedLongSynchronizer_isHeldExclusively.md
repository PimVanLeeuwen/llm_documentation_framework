#### isHeldExclusively

```
protected boolean isHeldExclusively()
```
Returns `true` if synchronization is held exclusively with
respect to the current (calling) thread. This method is invoked
upon each call to a non-waiting `AbstractQueuedLongSynchronizer.ConditionObject` method.
(Waiting methods instead invoke `release(long)`.)The default implementation throws `UnsupportedOperationException`. This method is invoked
internally only within `AbstractQueuedLongSynchronizer.ConditionObject` methods, so need
not be defined if conditions are not used.
Returns:
`true` if synchronization is held exclusively;
`false` otherwise
Throws:
`UnsupportedOperationException` - if conditions are not supported

