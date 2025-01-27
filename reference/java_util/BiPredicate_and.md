#### and

```
default BiPredicate<T,U> and(BiPredicate<? super T,? super U> other)
```
Returns a composed predicate that represents a short-circuiting logical
AND of this predicate and another. When evaluating the composed
predicate, if this predicate is `false`, then the `other`
predicate is not evaluated.Any exceptions thrown during evaluation of either predicate are relayed
to the caller; if evaluation of this predicate throws an exception, the
`other` predicate will not be evaluated.
Parameters:
`other` - a predicate that will be logically-ANDed with this
predicate
Returns:
a composed predicate that represents the short-circuiting logical
AND of this predicate and the `other` predicate
Throws:
`NullPointerException` - if other is null

