#### anyMatch

```
boolean anyMatch(LongPredicate predicate)
```
Returns whether any elements of this stream match the provided
predicate. May not evaluate the predicate on all elements if not
necessary for determining the result. If the stream is empty then
`false` is returned and the predicate is not evaluated.This is a short-circuiting
terminal operation.
API Note:
This method evaluates the existential quantification of the
predicate over the elements of the stream (for some x P(x)).
Parameters:
`predicate` - a non-interfering,
stateless
predicate to apply to elements of this stream
Returns:
`true` if any elements of the stream match the provided
predicate, otherwise `false`

