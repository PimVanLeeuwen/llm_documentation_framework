#### parent

```
public Preferences parent()
```
Implements the parent method as per the specification in
`Preferences.parent()`.This implementation obtains this preference node's lock, checks that
the node has not been removed and returns the parent value that was
passed to this node's constructor.
Specified by:
`parent` in class `Preferences`
Returns:
the parent of this preference node.
Throws:
`IllegalStateException` - if this node (or an ancestor) has been
removed with the `removeNode()` method.

