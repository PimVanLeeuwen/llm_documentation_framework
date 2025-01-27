#### put

```
public void put(E e)
         throws InterruptedException
```
Adds the specified element to this queue, waiting if necessary for
another thread to receive it.
Specified by:
`put` in interface `BlockingQueue<E>`
Parameters:
`e` - the element to add
Throws:
`InterruptedException` - if interrupted while waiting
`NullPointerException` - if the specified element is null

