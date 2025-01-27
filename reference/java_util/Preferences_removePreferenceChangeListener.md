#### removePreferenceChangeListener

```
public abstract void removePreferenceChangeListener(PreferenceChangeListener pcl)
```
Removes the specified preference change listener, so it no longer
receives preference change events.
Parameters:
`pcl` - The preference change listener to remove.
Throws:
`IllegalArgumentException` - if pcl was not a registered
preference change listener on this node.
`IllegalStateException` - if this node (or an ancestor) has been
removed with the `removeNode()` method.
See Also:
`addPreferenceChangeListener(PreferenceChangeListener)`

