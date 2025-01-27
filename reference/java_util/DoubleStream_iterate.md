#### iterate

```
static DoubleStream iterate(double seed,
                            DoubleUnaryOperator f)
```
Returns an infinite sequential ordered `DoubleStream` produced by iterative
application of a function `f` to an initial element `seed`,
producing a `Stream` consisting of `seed`, `f(seed)`,
`f(f(seed))`, etc.The first element (position `0`) in the `DoubleStream`
will be the provided `seed`. For `n > 0`, the element at
position `n`, will be the result of applying the function `f`
to the element at position `n - 1`.
Parameters:
`seed` - the initial element
`f` - a function to be applied to the previous element to produce
a new element
Returns:
a new sequential `DoubleStream`

