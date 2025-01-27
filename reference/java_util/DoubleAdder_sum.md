#### sum

```
public double sum()
```
Returns the current sum. The returned value is NOT an
atomic snapshot; invocation in the absence of concurrent
updates returns an accurate result, but concurrent updates that
occur while the sum is being calculated might not be
incorporated. Also, because floating-point arithmetic is not
strictly associative, the returned result need not be identical
to the value that would be obtained in a sequential series of
updates to a single variable.
Returns:
the sum

