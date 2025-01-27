#### owns

```
public final boolean owns(AbstractQueuedSynchronizer.ConditionObject condition)
```
Queries whether the given ConditionObject
uses this synchronizer as its lock.
Parameters:
`condition` - the condition
Returns:
`true` if owned
Throws:
`NullPointerException` - if the condition is null

