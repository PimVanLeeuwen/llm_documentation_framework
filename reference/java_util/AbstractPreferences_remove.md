#### remove

```
public void remove(String key)
```
Implements the remove(String) method as per the specification
in `Preferences.remove(String)`.This implementation obtains this preference node's lock,
checks that the node has not been removed, invokes
`removeSpi(String)` and if there are any preference
change listeners, enqueues a notification event for processing by the
event dispatch thread.
Specified by:
`remove` in class `Preferences`
Parameters:
`key` - key whose mapping is to be removed from the preference node.
Throws:
`IllegalStateException` - if this node (or an ancestor) has been
removed with the `removeNode()` method.
`NullPointerException` - if key is null..

