#### unpark

```
public static void unpark(Thread thread)
```
Makes available the permit for the given thread, if it
was not already available. If the thread was blocked on
`park` then it will unblock. Otherwise, its next call
to `park` is guaranteed not to block. This operation
is not guaranteed to have any effect at all if the given
thread has not been started.
Parameters:
`thread` - the thread to unpark, or `null`, in which case
this operation has no effect

