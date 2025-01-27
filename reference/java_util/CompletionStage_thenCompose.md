#### thenCompose

```
<U> CompletionStage<U> thenCompose(Function<? super T,? extends CompletionStage<U>> fn)
```
Returns a new CompletionStage that, when this stage completes
normally, is executed with this stage as the argument
to the supplied function.
See the `CompletionStage` documentation for rules
covering exceptional completion.
Type Parameters:
`U` - the type of the returned CompletionStage's result
Parameters:
`fn` - the function returning a new CompletionStage
Returns:
the CompletionStage

