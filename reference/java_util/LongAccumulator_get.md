#### get

```
public long get()
```
Returns the current value. The returned value is NOT
an atomic snapshot; invocation in the absence of concurrent
updates returns an accurate result, but concurrent updates that
occur while the value is being calculated might not be
incorporated.
Returns:
the current value

