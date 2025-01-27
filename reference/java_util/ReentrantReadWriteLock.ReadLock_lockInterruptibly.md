#### lockInterruptibly

```
public void lockInterruptibly()
                       throws InterruptedException
```
Acquires the read lock unless the current thread is
interrupted.Acquires the read lock if the write lock is not held
by another thread and returns immediately.If the write lock is held by another thread then the
current thread becomes disabled for thread scheduling
purposes and lies dormant until one of two things happens:The read lock is acquired by the current thread; orSome other thread interrupts
the current thread.If the current thread:has its interrupted status set on entry to this method; oris interrupted while
acquiring the read lock,then `InterruptedException` is thrown and the current
thread's interrupted status is cleared.In this implementation, as this method is an explicit
interruption point, preference is given to responding to
the interrupt over normal or reentrant acquisition of the
lock.
Specified by:
`lockInterruptibly` in interface `Lock`
Throws:
`InterruptedException` - if the current thread is interrupted

