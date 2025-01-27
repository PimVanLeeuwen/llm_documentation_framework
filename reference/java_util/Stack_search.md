#### search

```
public int search(Object o)
```
Returns the 1-based position where an object is on this stack.
If the object o occurs as an item in this stack, this
method returns the distance from the top of the stack of the
occurrence nearest the top of the stack; the topmost item on the
stack is considered to be at distance 1. The equals
method is used to compare o to the
items in this stack.
Parameters:
`o` - the desired object.
Returns:
the 1-based position from the top of the stack where
the object is located; the return value `-1`
indicates that the object is not on the stack.




