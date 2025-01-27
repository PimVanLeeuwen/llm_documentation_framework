#### timedJoin

```
public void timedJoin(Thread thread,
                      long timeout)
               throws InterruptedException
```
Performs a timed `Thread.join`
using this time unit.
This is a convenience method that converts time arguments into the
form required by the `Thread.join` method.
Parameters:
`thread` - the thread to wait for
`timeout` - the maximum time to wait. If less than
or equal to zero, do not wait at all.
Throws:
`InterruptedException` - if interrupted while waiting

