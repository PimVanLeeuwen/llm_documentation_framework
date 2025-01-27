#### thenApply

```
<U> CompletionStage<U> thenApply(Function<? super T,? extends U> fn)
```
Returns a new CompletionStage that, when this stage completes
normally, is executed with this stage's result as the argument
to the supplied function.
See the `CompletionStage` documentation for rules
covering exceptional completion.
Type Parameters:
`U` - the function's return type
Parameters:
`fn` - the function to use to compute the value of
the returned CompletionStage
Returns:
the new CompletionStage

