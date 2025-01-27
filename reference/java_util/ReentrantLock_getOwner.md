#### getOwner

```
protected Thread getOwner()
```
Returns the thread that currently owns this lock, or
`null` if not owned. When this method is called by a
thread that is not the owner, the return value reflects a
best-effort approximation of current lock status. For example,
the owner may be momentarily `null` even if there are
threads trying to acquire the lock but have not yet done so.
This method is designed to facilitate construction of
subclasses that provide more extensive lock monitoring
facilities.
Returns:
the owner, or `null` if not owned

