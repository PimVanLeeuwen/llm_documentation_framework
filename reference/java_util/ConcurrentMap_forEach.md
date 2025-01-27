#### forEach

```
default void forEach(BiConsumer<? super K,? super V> action)
```
Performs the given action for each entry in this map until all entries
have been processed or the action throws an exception. Unless
otherwise specified by the implementing class, actions are performed in
the order of entry set iteration (if an iteration order is specified.)
Exceptions thrown by the action are relayed to the caller.
Specified by:
`forEach` in interface `Map<K,V>`
Implementation Requirements:
The default implementation is equivalent to, for this
`map`:
```
 
 for ((Map.Entry<K, V> entry : map.entrySet())
     action.accept(entry.getKey(), entry.getValue());
 
```

Implementation Note:
The default implementation assumes that
`IllegalStateException` thrown by `getKey()` or
`getValue()` indicates that the entry has been removed and cannot
be processed. Operation continues for subsequent entries.
Parameters:
`action` - The action to be performed for each entry
Throws:
`NullPointerException` - if the specified action is null
Since:
1.8

