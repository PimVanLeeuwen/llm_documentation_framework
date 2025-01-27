#### thenApplyAsync

```
<U> CompletionStage<U> thenApplyAsync(Function<? super T,? extends U> fn,
                                      Executor executor)
```
Returns a new CompletionStage that, when this stage completes
normally, is executed using the supplied Executor, with this
stage's result as the argument to the supplied function.
See the `CompletionStage` documentation for rules
covering exceptional completion.
Type Parameters:
`U` - the function's return type
Parameters:
`fn` - the function to use to compute the value of
the returned CompletionStage
`executor` - the executor to use for asynchronous execution
Returns:
the new CompletionStage

