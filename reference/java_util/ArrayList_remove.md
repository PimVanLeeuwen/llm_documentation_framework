#### remove

```
public boolean remove(Object o)
```
Removes the first occurrence of the specified element from this list,
if it is present. If the list does not contain the element, it is
unchanged. More formally, removes the element with the lowest index
i such that
(o==null ? get(i)==null : o.equals(get(i)))
(if such an element exists). Returns true if this list
contained the specified element (or equivalently, if this list
changed as a result of the call).
Specified by:
`remove` in interface `Collection<E>`
Specified by:
`remove` in interface `List<E>`
Overrides:
`remove` in class `AbstractCollection<E>`
Parameters:
`o` - element to be removed from this list, if present
Returns:
true if this list contained the specified element

