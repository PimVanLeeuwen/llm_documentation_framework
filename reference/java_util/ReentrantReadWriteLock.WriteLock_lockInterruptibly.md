#### lockInterruptibly

```
public void lockInterruptibly()
                       throws InterruptedException
```
Acquires the write lock unless the current thread is
interrupted.Acquires the write lock if neither the read nor write lock
are held by another thread
and returns immediately, setting the write lock hold count to
one.If the current thread already holds this lock then the
hold count is incremented by one and the method returns
immediately.If the lock is held by another thread then the current
thread becomes disabled for thread scheduling purposes and
lies dormant until one of two things happens:The write lock is acquired by the current thread; orSome other thread interrupts
the current thread.If the write lock is acquired by the current thread then the
lock hold count is set to one.If the current thread:has its interrupted status set on entry to this method;
oris interrupted while
acquiring the write lock,then `InterruptedException` is thrown and the current
thread's interrupted status is cleared.In this implementation, as this method is an explicit
interruption point, preference is given to responding to
the interrupt over normal or reentrant acquisition of the
lock.
Specified by:
`lockInterruptibly` in interface `Lock`
Throws:
`InterruptedException` - if the current thread is interrupted

