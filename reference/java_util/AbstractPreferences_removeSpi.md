#### removeSpi

```
protected abstract void removeSpi(String key)
```
Remove the association (if any) for the specified key at this
preference node. It is guaranteed that key is non-null.
Also, it is guaranteed that this node has not been removed.
(The implementor needn't check for either of these things.)This method is invoked with the lock on this node held.
Parameters:
`key` - the key

