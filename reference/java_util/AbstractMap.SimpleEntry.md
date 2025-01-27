```
public static class AbstractMap.SimpleEntry<K,V>
extends Object
implements Map.Entry<K,V>, Serializable
```
An Entry maintaining a key and a value. The value may be
changed using the setValue method. This class
facilitates the process of building custom map
implementations. For example, it may be convenient to return
arrays of SimpleEntry instances in method
Map.entrySet().toArray.
Since:
1.6
See Also:
Serialized Form
