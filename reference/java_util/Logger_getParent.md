#### getParent

```
public Logger getParent()
```
Return the parent for this Logger.This method returns the nearest extant parent in the namespace.
Thus if a Logger is called "a.b.c.d", and a Logger called "a.b"
has been created but no logger "a.b.c" exists, then a call of
getParent on the Logger "a.b.c.d" will return the Logger "a.b".The result will be null if it is called on the root Logger
in the namespace.
Returns:
nearest existing parent Logger

