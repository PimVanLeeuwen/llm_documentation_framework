```
public interface ConcurrentMap<K,V>
extends Map<K,V>
```
A `Map` providing thread safety and atomicity
guarantees.Memory consistency effects: As with other concurrent
collections, actions in a thread prior to placing an object into a
`ConcurrentMap` as a key or value
happen-before
actions subsequent to the access or removal of that object from
the `ConcurrentMap` in another thread.This interface is a member of the
Java Collections Framework.
Since:
1.5
