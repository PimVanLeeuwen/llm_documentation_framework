#### properties

```
SortedMap<String,String> properties()
```
Get the set of this engine's properties. This set is
a "live view", so that changing its
contents immediately affects the Packer engine, and
changes from the engine (such as progress indications)
are immediately visible in the map.The property map may contain pre-defined implementation
specific and default properties. Users are encouraged to
read the information and fully understand the implications,
before modifying pre-existing properties.Implementation specific properties are prefixed with a
package name associated with the implementor, beginning
with com. or a similar prefix.
All property names beginning with pack. and
unpack. are reserved for use by this API.Unknown properties may be ignored or rejected with an
unspecified error, and invalid entries may cause an
unspecified error to be thrown.
Returns:
A sorted association of option key strings to option values.

