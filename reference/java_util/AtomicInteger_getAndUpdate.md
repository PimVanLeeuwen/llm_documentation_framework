#### getAndUpdate

```
public final int getAndUpdate(IntUnaryOperator updateFunction)
```
Atomically updates the current value with the results of
applying the given function, returning the previous value. The
function should be side-effect-free, since it may be re-applied
when attempted updates fail due to contention among threads.
Parameters:
`updateFunction` - a side-effect-free function
Returns:
the previous value
Since:
1.8

