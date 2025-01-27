#### childrenNames

```
public String[] childrenNames()
                       throws BackingStoreException
```
Implements the children method as per the specification in
`Preferences.childrenNames()`.This implementation obtains this preference node's lock, checks that
the node has not been removed, constructs a TreeSet initialized
to the names of children already cached (the children in this node's
"child-cache"), invokes `childrenNamesSpi()`, and adds all of the
returned child-names into the set. The elements of the tree set are
dumped into a String array using the toArray method,
and this array is returned.
Specified by:
`childrenNames` in class `Preferences`
Returns:
the names of the children of this preference node.
Throws:
`BackingStoreException` - if this operation cannot be completed
due to a failure in the backing store, or inability to
communicate with it.
`IllegalStateException` - if this node (or an ancestor) has been
removed with the `removeNode()` method.
See Also:
`cachedChildren()`

