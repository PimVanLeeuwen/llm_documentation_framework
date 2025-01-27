#### isUserNode

```
public boolean isUserNode()
```
Implements the isUserNode method as per the specification in
`Preferences.isUserNode()`.This implementation compares this node's root node (which is stored
in a private field) with the value returned by
`Preferences.userRoot()`. If the two object references are
identical, this method returns true.
Specified by:
`isUserNode` in class `Preferences`
Returns:
true if this preference node is in the user
preference tree, false if it's in the system
preference tree.

