#### push

```
public void push(E e)
```
Description copied from interface: `Deque`
Pushes an element onto the stack represented by this deque (in other
words, at the head of this deque) if it is possible to do so
immediately without violating capacity restrictions, throwing an
`IllegalStateException` if no space is currently available.This method is equivalent to `Deque.addFirst(E)`.
Specified by:
`push` in interface `Deque<E>`
Parameters:
`e` - the element to push
Throws:
`NullPointerException` - if the specified element is null and this
deque does not permit null elements

