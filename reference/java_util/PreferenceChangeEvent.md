```
public class PreferenceChangeEvent
extends EventObject
```
An event emitted by a Preferences node to indicate that
a preference has been added, removed or has had its value changed.Note, that although PreferenceChangeEvent inherits Serializable interface
from EventObject, it is not intended to be Serializable. Appropriate
serialization methods are implemented to throw NotSerializableException.
Since:
1.4
See Also:
`Preferences`,
`PreferenceChangeListener`,
`NodeChangeEvent`
