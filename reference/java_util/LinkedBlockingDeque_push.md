#### push

```
public void push(E e)
```
Description copied from interface: `BlockingDeque`
Pushes an element onto the stack represented by this deque (in other
words, at the head of this deque) if it is possible to do so
immediately without violating capacity restrictions, throwing an
`IllegalStateException` if no space is currently available.This method is equivalent to `addFirst`.
Specified by:
`push` in interface `BlockingDeque<E>`
Specified by:
`push` in interface `Deque<E>`
Parameters:
`e` - the element to push
Throws:
`IllegalStateException` - if this deque is full
`NullPointerException` - if the specified element is null

