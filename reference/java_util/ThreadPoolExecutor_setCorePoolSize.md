#### setCorePoolSize

```
public void setCorePoolSize(int corePoolSize)
```
Sets the core number of threads. This overrides any value set
in the constructor. If the new value is smaller than the
current value, excess existing threads will be terminated when
they next become idle. If larger, new threads will, if needed,
be started to execute any queued tasks.
Parameters:
`corePoolSize` - the new core size
Throws:
`IllegalArgumentException` - if `corePoolSize < 0`
See Also:
`getCorePoolSize()`

