#### node

```
public abstract Preferences node(String pathName)
```
Returns the named preference node in the same tree as this node,
creating it and any of its ancestors if they do not already exist.
Accepts a relative or absolute path name. Relative path names
(which do not begin with the slash character ('/')) are
interpreted relative to this preference node.If the returned node did not exist prior to this call, this node and
any ancestors that were created by this call are not guaranteed
to become permanent until the flush method is called on
the returned node (or one of its ancestors or descendants).
Parameters:
`pathName` - the path name of the preference node to return.
Returns:
the specified preference node.
Throws:
`IllegalArgumentException` - if the path name is invalid (i.e.,
it contains multiple consecutive slash characters, or ends
with a slash character and is more than one character long).
`NullPointerException` - if path name is null.
`IllegalStateException` - if this node (or an ancestor) has been
removed with the `removeNode()` method.
See Also:
`flush()`

