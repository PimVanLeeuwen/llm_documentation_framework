#### compareAndSetState

```
protected final boolean compareAndSetState(int expect,
                                           int update)
```
Atomically sets synchronization state to the given updated
value if the current state value equals the expected value.
This operation has memory semantics of a `volatile` read
and write.
Parameters:
`expect` - the expected value
`update` - the new value
Returns:
`true` if successful. False return indicates that the actual
value was not equal to the expected value.

