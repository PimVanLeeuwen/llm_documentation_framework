#### removeElement

```
public boolean removeElement(Object obj)
```
Removes the first (lowest-indexed) occurrence of the argument
from this vector. If the object is found in this vector, each
component in the vector with an index greater or equal to the
object's index is shifted downward to have an index one smaller
than the value it had previously.This method is identical in functionality to the
`remove(Object)` method (which is part of the
`List` interface).
Parameters:
`obj` - the component to be removed
Returns:
`true` if the argument was a component of this
vector; `false` otherwise.

