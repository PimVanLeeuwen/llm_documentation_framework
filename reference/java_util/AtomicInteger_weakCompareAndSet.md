#### weakCompareAndSet

```
public final boolean weakCompareAndSet(int expect,
                                       int update)
```
Atomically sets the value to the given updated value
if the current value `==` the expected value.May fail
spuriously and does not provide ordering guarantees, so is
only rarely an appropriate alternative to `compareAndSet`.
Parameters:
`expect` - the expected value
`update` - the new value
Returns:
`true` if successful

