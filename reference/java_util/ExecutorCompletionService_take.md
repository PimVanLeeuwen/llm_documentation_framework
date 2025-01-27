#### take

```
public Future<V> take()
               throws InterruptedException
```
Description copied from interface: `CompletionService`
Retrieves and removes the Future representing the next
completed task, waiting if none are yet present.
Specified by:
`take` in interface `CompletionService<V>`
Returns:
the Future representing the next completed task
Throws:
`InterruptedException` - if interrupted while waiting

