#### node

```
public Preferences node(String path)
```
Implements the node method as per the specification in
`Preferences.node(String)`.This implementation obtains this preference node's lock and checks
that the node has not been removed. If path is "",
this node is returned; if path is "/", this node's
root is returned. If the first character in path is
not '/', the implementation breaks path into
tokens and recursively traverses the path from this node to the
named node, "consuming" a name and a slash from path at
each step of the traversal. At each step, the current node is locked
and the node's child-cache is checked for the named node. If it is
not found, the name is checked to make sure its length does not
exceed MAX\_NAME\_LENGTH. Then the `childSpi(String)`
method is invoked, and the result stored in this node's child-cache.
If the newly created Preferences object's `newNode`
field is true and there are any node change listeners,
a notification event is enqueued for processing by the event dispatch
thread.When there are no more tokens, the last value found in the
child-cache or returned by childSpi is returned by this
method. If during the traversal, two "/" tokens occur
consecutively, or the final token is "/" (rather than a name),
an appropriate IllegalArgumentException is thrown.If the first character of path is '/'
(indicating an absolute path name) this preference node's
lock is dropped prior to breaking path into tokens, and
this method recursively traverses the path starting from the root
(rather than starting from this node). The traversal is otherwise
identical to the one described for relative path names. Dropping
the lock on this node prior to commencing the traversal at the root
node is essential to avoid the possibility of deadlock, as per the
`locking invariant`.
Specified by:
`node` in class `Preferences`
Parameters:
`path` - the path name of the preference node to return.
Returns:
the specified preference node.
Throws:
`IllegalArgumentException` - if the path name is invalid (i.e.,
it contains multiple consecutive slash characters, or ends
with a slash character and is more than one character long).
`IllegalStateException` - if this node (or an ancestor) has been
removed with the `removeNode()` method.
See Also:
`Preferences.flush()`

