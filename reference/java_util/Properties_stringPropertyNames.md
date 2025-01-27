#### stringPropertyNames

```
public Set<String> stringPropertyNames()
```
Returns a set of keys in this property list where
the key and its corresponding value are strings,
including distinct keys in the default property list if a key
of the same name has not already been found from the main
properties list. Properties whose key or value is not
of type String are omitted.The returned set is not backed by the Properties object.
Changes to this Properties are not reflected in the set,
or vice versa.
Returns:
a set of keys in this property list where
the key and its corresponding value are strings,
including the keys in the default property list.
Since:
1.6
See Also:
`defaults`

