#### completeExceptionally

```
public void completeExceptionally(Throwable ex)
```
Completes this task abnormally, and if not already aborted or
cancelled, causes it to throw the given exception upon
`join` and related operations. This method may be used
to induce exceptions in asynchronous tasks, or to force
completion of tasks that would not otherwise complete. Its use
in other situations is discouraged. This method is
overridable, but overridden versions must invoke `super`
implementation to maintain guarantees.
Parameters:
`ex` - the exception to throw. If this exception is not a
`RuntimeException` or `Error`, the actual exception
thrown will be a `RuntimeException` with cause `ex`.

