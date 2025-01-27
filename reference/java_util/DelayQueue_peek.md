#### peek

```
public E peek()
```
Retrieves, but does not remove, the head of this queue, or
returns `null` if this queue is empty. Unlike
`poll`, if no expired elements are available in the queue,
this method returns the element that will expire next,
if one exists.
Specified by:
`peek` in interface `Queue<E extends Delayed>`
Returns:
the head of this queue, or `null` if this
queue is empty

