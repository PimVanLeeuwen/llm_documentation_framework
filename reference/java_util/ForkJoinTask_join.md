#### join

```
public final V join()
```
Returns the result of the computation when it `is
done`. This method differs from `get()` in that
abnormal completion results in `RuntimeException` or
`Error`, not `ExecutionException`, and that
interrupts of the calling thread do not cause the
method to abruptly return by throwing `InterruptedException`.
Returns:
the computed result

