#### setMaximumPoolSize

```
public void setMaximumPoolSize(int maximumPoolSize)
```
Sets the maximum allowed number of threads. This overrides any
value set in the constructor. If the new value is smaller than
the current value, excess existing threads will be
terminated when they next become idle.
Parameters:
`maximumPoolSize` - the new maximum
Throws:
`IllegalArgumentException` - if the new maximum is
less than or equal to zero, or
less than the core pool size
See Also:
`getMaximumPoolSize()`

