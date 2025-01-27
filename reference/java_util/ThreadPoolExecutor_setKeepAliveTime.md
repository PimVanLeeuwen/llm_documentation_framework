#### setKeepAliveTime

```
public void setKeepAliveTime(long time,
                             TimeUnit unit)
```
Sets the time limit for which threads may remain idle before
being terminated. If there are more than the core number of
threads currently in the pool, after waiting this amount of
time without processing a task, excess threads will be
terminated. This overrides any value set in the constructor.
Parameters:
`time` - the time to wait. A time value of zero will cause
excess threads to terminate immediately after executing tasks.
`unit` - the time unit of the `time` argument
Throws:
`IllegalArgumentException` - if `time` less than zero or
if `time` is zero and `allowsCoreThreadTimeOut`
See Also:
`getKeepAliveTime(TimeUnit)`

