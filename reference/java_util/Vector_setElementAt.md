#### setElementAt

```
public void setElementAt(E obj,
                         int index)
```
Sets the component at the specified `index` of this
vector to be the specified object. The previous component at that
position is discarded.The index must be a value greater than or equal to `0`
and less than the current size of the vector.This method is identical in functionality to the
`set(int, E)`
method (which is part of the `List` interface). Note that the
`set` method reverses the order of the parameters, to more closely
match array usage. Note also that the `set` method returns the
old value that was stored at the specified position.
Parameters:
`obj` - what the component is to be set to
`index` - the specified index
Throws:
`ArrayIndexOutOfBoundsException` - if the index is out of range
(`index < 0 || index >= size()`)

