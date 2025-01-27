#### defaultThreadFactory

```
public static ThreadFactory defaultThreadFactory()
```
Returns a default thread factory used to create new threads.
This factory creates all new threads used by an Executor in the
same `ThreadGroup`. If there is a `SecurityManager`, it uses the group of `System.getSecurityManager()`, else the group of the thread
invoking this `defaultThreadFactory` method. Each new
thread is created as a non-daemon thread with priority set to
the smaller of `Thread.NORM_PRIORITY` and the maximum
priority permitted in the thread group. New threads have names
accessible via `Thread.getName()` of
pool-N-thread-M, where N is the sequence
number of this factory, and M is the sequence number
of the thread created by this factory.
Returns:
a thread factory

