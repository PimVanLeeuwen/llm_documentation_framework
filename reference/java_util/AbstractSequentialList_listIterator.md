#### listIterator

```
public abstract ListIterator<E> listIterator(int index)
```
Returns a list iterator over the elements in this list (in proper
sequence).
Specified by:
`listIterator` in interface `List<E>`
Overrides:
`listIterator` in class `AbstractList<E>`
Parameters:
`index` - index of first element to be returned from the list
iterator (by a call to the `next` method)
Returns:
a list iterator over the elements in this list (in proper
sequence)
Throws:
`IndexOutOfBoundsException` - if the index is out of range
(`index < 0 || index > size()`)




