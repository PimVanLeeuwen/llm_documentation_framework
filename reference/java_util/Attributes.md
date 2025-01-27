```
public class Attributes
extends Object
implements Map<Object,Object>, Cloneable
```
The Attributes class maps Manifest attribute names to associated string
values. Valid attribute names are case-insensitive, are restricted to
the ASCII characters in the set [0-9a-zA-Z\_-], and cannot exceed 70
characters in length. Attribute values can contain any characters and
will be UTF8-encoded when written to the output stream. See the
JAR File Specification
for more information about valid attribute names and values.
Since:
1.2
See Also:
`Manifest`
