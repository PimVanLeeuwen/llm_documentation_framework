#### getThenReset

```
public long getThenReset()
```
Equivalent in effect to `get()` followed by `reset()`. This method may apply for example during quiescent
points between multithreaded computations. If there are
updates concurrent with this method, the returned value is
not guaranteed to be the final value occurring before
the reset.
Returns:
the value before reset

