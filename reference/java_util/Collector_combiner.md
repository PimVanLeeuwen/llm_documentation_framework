#### combiner

```
BinaryOperator<A> combiner()
```
A function that accepts two partial results and merges them. The
combiner function may fold state from one argument into the other and
return that, or may return a new result container.
Returns:
a function which combines two partial results into a combined
result

