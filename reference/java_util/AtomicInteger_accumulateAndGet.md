#### accumulateAndGet

```
public final int accumulateAndGet(int x,
                                  IntBinaryOperator accumulatorFunction)
```
Atomically updates the current value with the results of
applying the given function to the current and given values,
returning the updated value. The function should be
side-effect-free, since it may be re-applied when attempted
updates fail due to contention among threads. The function
is applied with the current value as its first argument,
and the given update as the second argument.
Parameters:
`x` - the update value
`accumulatorFunction` - a side-effect-free function of two arguments
Returns:
the updated value
Since:
1.8

