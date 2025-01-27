#### parkNanos

```
public static void parkNanos(long nanos)
```
Disables the current thread for thread scheduling purposes, for up to
the specified waiting time, unless the permit is available.If the permit is available then it is consumed and the call
returns immediately; otherwise the current thread becomes disabled
for thread scheduling purposes and lies dormant until one of four
things happens:Some other thread invokes `unpark` with the
current thread as the target; orSome other thread interrupts
the current thread; orThe specified waiting time elapses; orThe call spuriously (that is, for no reason) returns.This method does not report which of these caused the
method to return. Callers should re-check the conditions which caused
the thread to park in the first place. Callers may also determine,
for example, the interrupt status of the thread, or the elapsed time
upon return.
Parameters:
`nanos` - the maximum number of nanoseconds to wait

