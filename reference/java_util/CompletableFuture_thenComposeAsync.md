#### thenComposeAsync

```
public <U> CompletableFuture<U> thenComposeAsync(Function<? super T,? extends CompletionStage<U>> fn,
                                                 Executor executor)
```
Description copied from interface: `CompletionStage`
Returns a new CompletionStage that, when this stage completes
normally, is executed using the supplied Executor, with this
stage's result as the argument to the supplied function.
See the `CompletionStage` documentation for rules
covering exceptional completion.
Specified by:
`thenComposeAsync` in interface `CompletionStage<T>`
Type Parameters:
`U` - the type of the returned CompletionStage's result
Parameters:
`fn` - the function returning a new CompletionStage
`executor` - the executor to use for asynchronous execution
Returns:
the CompletionStage

