#### isRemoved

```
protected boolean isRemoved()
```
Returns true iff this node (or an ancestor) has been
removed with the `removeNode()` method. This method
locks this node prior to returning the contents of the private
field used to track this state.
Returns:
true iff this node (or an ancestor) has been
removed with the `removeNode()` method.

