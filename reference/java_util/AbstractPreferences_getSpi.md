#### getSpi

```
protected abstract String getSpi(String key)
```
Return the value associated with the specified key at this preference
node, or null if there is no association for this key, or the
association cannot be determined at this time. It is guaranteed that
key is non-null. Also, it is guaranteed that this node has
not been removed. (The implementor needn't check for either of these
things.)Generally speaking, this method should not throw an exception
under any circumstances. If, however, if it does throw an exception,
the exception will be intercepted and treated as a null
return value.This method is invoked with the lock on this node held.
Parameters:
`key` - the key
Returns:
the value associated with the specified key at this preference
node, or null if there is no association for this
key, or the association cannot be determined at this time.

