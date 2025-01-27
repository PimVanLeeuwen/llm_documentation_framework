#### of

```
static <T,A,R> Collector<T,A,R> of(Supplier<A> supplier,
                                   BiConsumer<A,T> accumulator,
                                   BinaryOperator<A> combiner,
                                   Function<A,R> finisher,
                                   Collector.Characteristics... characteristics)
```
Returns a new `Collector` described by the given `supplier`,
`accumulator`, `combiner`, and `finisher` functions.
Type Parameters:
`T` - The type of input elements for the new collector
`A` - The intermediate accumulation type of the new collector
`R` - The final result type of the new collector
Parameters:
`supplier` - The supplier function for the new collector
`accumulator` - The accumulator function for the new collector
`combiner` - The combiner function for the new collector
`finisher` - The finisher function for the new collector
`characteristics` - The collector characteristics for the new
collector
Returns:
the new `Collector`
Throws:
`NullPointerException` - if any argument is null




