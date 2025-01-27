#### parkUntil

```
public static void parkUntil(long deadline)
```
Disables the current thread for thread scheduling purposes, until
the specified deadline, unless the permit is available.If the permit is available then it is consumed and the call
returns immediately; otherwise the current thread becomes disabled
for thread scheduling purposes and lies dormant until one of four
things happens:Some other thread invokes `unpark` with the
current thread as the target; orSome other thread interrupts
the current thread; orThe specified deadline passes; orThe call spuriously (that is, for no reason) returns.This method does not report which of these caused the
method to return. Callers should re-check the conditions which caused
the thread to park in the first place. Callers may also determine,
for example, the interrupt status of the thread, or the current time
upon return.
Parameters:
`deadline` - the absolute time, in milliseconds from the Epoch,
to wait until




