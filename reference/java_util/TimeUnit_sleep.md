#### sleep

```
public void sleep(long timeout)
           throws InterruptedException
```
Performs a `Thread.sleep` using
this time unit.
This is a convenience method that converts time arguments into the
form required by the `Thread.sleep` method.
Parameters:
`timeout` - the minimum time to sleep. If less than
or equal to zero, do not sleep at all.
Throws:
`InterruptedException` - if interrupted while sleeping




