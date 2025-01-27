#### timedWait

```
public void timedWait(Object obj,
                      long timeout)
               throws InterruptedException
```
Performs a timed `Object.wait`
using this time unit.
This is a convenience method that converts timeout arguments
into the form required by the `Object.wait` method.For example, you could implement a blocking `poll`
method (see `BlockingQueue.poll`)
using:
```
 
 public synchronized Object poll(long timeout, TimeUnit unit)
     throws InterruptedException {
   while (empty) {
     unit.timedWait(this, timeout);
     ...
   }
 }
```

Parameters:
`obj` - the object to wait on
`timeout` - the maximum time to wait. If less than
or equal to zero, do not wait at all.
Throws:
`InterruptedException` - if interrupted while waiting

