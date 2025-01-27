#### forEachRemaining

```
void forEachRemaining(T_CONS action)
```
Performs the given action for each remaining element, in the order
elements occur when iterating, until all elements have been processed
or the action throws an exception. Errors or runtime exceptions
thrown by the action are relayed to the caller.
Parameters:
`action` - The action to be performed for each element
Throws:
`NullPointerException` - if the specified action is null




