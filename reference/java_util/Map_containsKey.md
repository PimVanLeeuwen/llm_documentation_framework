#### containsKey

```
boolean containsKey(Object key)
```
Returns true if this map contains a mapping for the specified
key. More formally, returns true if and only if
this map contains a mapping for a key k such that
(key==null ? k==null : key.equals(k)). (There can be
at most one such mapping.)
Parameters:
`key` - key whose presence in this map is to be tested
Returns:
true if this map contains a mapping for the specified
key
Throws:
`ClassCastException` - if the key is of an inappropriate type for
this map
(optional)
`NullPointerException` - if the specified key is null and this map
does not permit null keys
(optional)

