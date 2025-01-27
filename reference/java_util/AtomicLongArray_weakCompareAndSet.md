#### weakCompareAndSet

```
public final boolean weakCompareAndSet(int i,
                                       long expect,
                                       long update)
```
Atomically sets the element at position `i` to the given
updated value if the current value `==` the expected value.May fail
spuriously and does not provide ordering guarantees, so is
only rarely an appropriate alternative to `compareAndSet`.
Parameters:
`i` - the index
`expect` - the expected value
`update` - the new value
Returns:
`true` if successful

