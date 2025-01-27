#### sumThenReset

```
public double sumThenReset()
```
Equivalent in effect to `sum()` followed by `reset()`. This method may apply for example during quiescent
points between multithreaded computations. If there are
updates concurrent with this method, the returned value is
not guaranteed to be the final value occurring before
the reset.
Returns:
the sum

