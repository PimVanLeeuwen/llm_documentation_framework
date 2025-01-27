#### noneMatch

```
boolean noneMatch(DoublePredicate predicate)
```
Returns whether no elements of this stream match the provided predicate.
May not evaluate the predicate on all elements if not necessary for
determining the result. If the stream is empty then `true` is
returned and the predicate is not evaluated.This is a short-circuiting
terminal operation.
API Note:
This method evaluates the universal quantification of the
negated predicate over the elements of the stream (for all x ~P(x)). If
the stream is empty, the quantification is said to be vacuously satisfied
and is always `true`, regardless of P(x).
Parameters:
`predicate` - a non-interfering,
stateless
predicate to apply to elements of this stream
Returns:
`true` if either no elements of the stream match the
provided predicate or the stream is empty, otherwise `false`

