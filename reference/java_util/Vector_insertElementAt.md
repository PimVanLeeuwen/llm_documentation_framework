#### insertElementAt

```
public void insertElementAt(E obj,
                            int index)
```
Inserts the specified object as a component in this vector at the
specified `index`. Each component in this vector with
an index greater or equal to the specified `index` is
shifted upward to have an index one greater than the value it had
previously.The index must be a value greater than or equal to `0`
and less than or equal to the current size of the vector. (If the
index is equal to the current size of the vector, the new element
is appended to the Vector.)This method is identical in functionality to the
`add(int, E)`
method (which is part of the `List` interface). Note that the
`add` method reverses the order of the parameters, to more closely
match array usage.
Parameters:
`obj` - the component to insert
`index` - where to insert the new component
Throws:
`ArrayIndexOutOfBoundsException` - if the index is out of range
(`index < 0 || index > size()`)

