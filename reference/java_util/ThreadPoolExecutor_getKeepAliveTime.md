#### getKeepAliveTime

```
public long getKeepAliveTime(TimeUnit unit)
```
Returns the thread keep-alive time, which is the amount of time
that threads in excess of the core pool size may remain
idle before being terminated.
Parameters:
`unit` - the desired time unit of the result
Returns:
the time limit
See Also:
`setKeepAliveTime(long, TimeUnit)`

