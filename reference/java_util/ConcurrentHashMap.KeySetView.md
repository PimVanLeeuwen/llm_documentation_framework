```
public static class ConcurrentHashMap.KeySetView<K,V>
extends Object
implements Set<K>, Serializable
```
A view of a ConcurrentHashMap as a `Set` of keys, in
which additions may optionally be enabled by mapping to a
common value. This class cannot be directly instantiated.
See `keySet()`,
`keySet(V)`,
`newKeySet()`,
`newKeySet(int)`.
Since:
1.8
See Also:
Serialized Form
