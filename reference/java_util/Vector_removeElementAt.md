#### removeElementAt

```
public void removeElementAt(int index)
```
Deletes the component at the specified index. Each component in
this vector with an index greater or equal to the specified
`index` is shifted downward to have an index one
smaller than the value it had previously. The size of this vector
is decreased by `1`.The index must be a value greater than or equal to `0`
and less than the current size of the vector.This method is identical in functionality to the `remove(int)`
method (which is part of the `List` interface). Note that the
`remove` method returns the old value that was stored at the
specified position.
Parameters:
`index` - the index of the object to remove
Throws:
`ArrayIndexOutOfBoundsException` - if the index is out of range
(`index < 0 || index >= size()`)

