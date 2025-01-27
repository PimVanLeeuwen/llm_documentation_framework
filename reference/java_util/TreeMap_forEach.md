#### forEach

```
public void forEach(BiConsumer<? super K,? super V> action)
```
Description copied from interface: `Map`
Performs the given action for each entry in this map until all entries
have been processed or the action throws an exception. Unless
otherwise specified by the implementing class, actions are performed in
the order of entry set iteration (if an iteration order is specified.)
Exceptions thrown by the action are relayed to the caller.
Specified by:
`forEach` in interface `Map<K,V>`
Parameters:
`action` - The action to be performed for each entry

