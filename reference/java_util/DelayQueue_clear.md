#### clear

```
public void clear()
```
Atomically removes all of the elements from this delay queue.
The queue will be empty after this call returns.
Elements with an unexpired delay are not waited for; they are
simply discarded from the queue.
Specified by:
`clear` in interface `Collection<E extends Delayed>`
Overrides:
`clear` in class `AbstractQueue<E extends Delayed>`

