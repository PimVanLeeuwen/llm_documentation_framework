#### compareAndSet

```
public final boolean compareAndSet(V expect,
                                   V update)
```
Atomically sets the value to the given updated value
if the current value `==` the expected value.
Parameters:
`expect` - the expected value
`update` - the new value
Returns:
`true` if successful. False return indicates that
the actual value was not equal to the expected value.

