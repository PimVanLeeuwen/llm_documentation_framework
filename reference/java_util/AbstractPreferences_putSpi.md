#### putSpi

```
protected abstract void putSpi(String key,
                               String value)
```
Put the given key-value association into this preference node. It is
guaranteed that key and value are non-null and of
legal length. Also, it is guaranteed that this node has not been
removed. (The implementor needn't check for any of these things.)This method is invoked with the lock on this node held.
Parameters:
`key` - the key
`value` - the value

