#### childSpi

```
protected abstract AbstractPreferences childSpi(String name)
```
Returns the named child of this preference node, creating it if it does
not already exist. It is guaranteed that name is non-null,
non-empty, does not contain the slash character ('/'), and is no longer
than `Preferences.MAX_NAME_LENGTH` characters. Also, it is guaranteed that
this node has not been removed. (The implementor needn't check for any
of these things.)Finally, it is guaranteed that the named node has not been returned
by a previous invocation of this method or `getChild(String)`
after the last time that it was removed. In other words, a cached
value will always be used in preference to invoking this method.
Subclasses need not maintain their own cache of previously returned
children.The implementer must ensure that the returned node has not been
removed. If a like-named child of this node was previously removed, the
implementer must return a newly constructed AbstractPreferences
node; once removed, an AbstractPreferences node
cannot be "resuscitated."If this method causes a node to be created, this node is not
guaranteed to be persistent until the flush method is
invoked on this node or one of its ancestors (or descendants).This method is invoked with the lock on this node held.
Parameters:
`name` - The name of the child node to return, relative to
this preference node.
Returns:
The named child node.

