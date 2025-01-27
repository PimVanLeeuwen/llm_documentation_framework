#### updateAndGet

```
public final V updateAndGet(UnaryOperator<V> updateFunction)
```
Atomically updates the current value with the results of
applying the given function, returning the updated value. The
function should be side-effect-free, since it may be re-applied
when attempted updates fail due to contention among threads.
Parameters:
`updateFunction` - a side-effect-free function
Returns:
the updated value
Since:
1.8

