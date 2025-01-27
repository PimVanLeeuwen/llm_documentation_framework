#### add

```
public void add(int index,
                E element)
```
Inserts the specified element at the specified position in this Vector.
Shifts the element currently at that position (if any) and any
subsequent elements to the right (adds one to their indices).
Specified by:
`add` in interface `List<E>`
Overrides:
`add` in class `AbstractList<E>`
Parameters:
`index` - index at which the specified element is to be inserted
`element` - element to be inserted
Throws:
`ArrayIndexOutOfBoundsException` - if the index is out of range
(`index < 0 || index > size()`)
Since:
1.2

