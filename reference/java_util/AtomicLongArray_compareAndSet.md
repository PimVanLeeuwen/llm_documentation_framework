#### compareAndSet

```
public final boolean compareAndSet(int i,
                                   long expect,
                                   long update)
```
Atomically sets the element at position `i` to the given
updated value if the current value `==` the expected value.
Parameters:
`i` - the index
`expect` - the expected value
`update` - the new value
Returns:
`true` if successful. False return indicates that
the actual value was not equal to the expected value.

