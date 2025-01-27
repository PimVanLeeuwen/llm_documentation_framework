#### block

```
boolean block()
       throws InterruptedException
```
Possibly blocks the current thread, for example waiting for
a lock or condition.
Returns:
`true` if no additional blocking is necessary
(i.e., if isReleasable would return true)
Throws:
`InterruptedException` - if interrupted while waiting
(the method is not required to do so, but is allowed to)

