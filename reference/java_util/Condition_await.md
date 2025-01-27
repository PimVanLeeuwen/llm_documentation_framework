#### await

```
boolean await(long time,
              TimeUnit unit)
       throws InterruptedException
```
Causes the current thread to wait until it is signalled or interrupted,
or the specified waiting time elapses. This method is behaviorally
equivalent to:
```
  awaitNanos(unit.toNanos(time)) > 0
```

Parameters:
`time` - the maximum time to wait
`unit` - the time unit of the `time` argument
Returns:
`false` if the waiting time detectably elapsed
before return from the method, else `true`
Throws:
`InterruptedException` - if the current thread is interrupted
(and interruption of thread suspension is supported)

