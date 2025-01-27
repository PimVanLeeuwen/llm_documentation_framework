#### handle

```
<U> CompletionStage<U> handle(BiFunction<? super T,Throwable,? extends U> fn)
```
Returns a new CompletionStage that, when this stage completes
either normally or exceptionally, is executed with this stage's
result and exception as arguments to the supplied function.When this stage is complete, the given function is invoked
with the result (or `null` if none) and the exception (or
`null` if none) of this stage as arguments, and the
function's result is used to complete the returned stage.
Type Parameters:
`U` - the function's return type
Parameters:
`fn` - the function to use to compute the value of the
returned CompletionStage
Returns:
the new CompletionStage

