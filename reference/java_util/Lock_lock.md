#### lock

```
void lock()
```
Acquires the lock.If the lock is not available then the current thread becomes
disabled for thread scheduling purposes and lies dormant until the
lock has been acquired.Implementation ConsiderationsA `Lock` implementation may be able to detect erroneous use
of the lock, such as an invocation that would cause deadlock, and
may throw an (unchecked) exception in such circumstances. The
circumstances and the exception type must be documented by that
`Lock` implementation.

