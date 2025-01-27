```
public class NodeChangeEvent
extends EventObject
```
An event emitted by a Preferences node to indicate that
a child of that node has been added or removed.Note, that although NodeChangeEvent inherits Serializable interface from
java.util.EventObject, it is not intended to be Serializable. Appropriate
serialization methods are implemented to throw NotSerializableException.
Since:
1.4
See Also:
`Preferences`,
`NodeChangeListener`,
`PreferenceChangeEvent`
