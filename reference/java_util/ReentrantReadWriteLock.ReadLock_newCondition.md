#### newCondition

```
public Condition newCondition()
```
Throws `UnsupportedOperationException` because
`ReadLocks` do not support conditions.
Specified by:
`newCondition` in interface `Lock`
Returns:
A new `Condition` instance for this `Lock` instance
Throws:
`UnsupportedOperationException` - always

