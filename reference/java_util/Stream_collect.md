#### collect

```
<R,A> R collect(Collector<? super T,A,R> collector)
```
Performs a mutable
reduction operation on the elements of this stream using a
`Collector`. A `Collector`
encapsulates the functions used as arguments to
`collect(Supplier, BiConsumer, BiConsumer)`, allowing for reuse of
collection strategies and composition of collect operations such as
multiple-level grouping or partitioning.If the stream is parallel, and the `Collector`
is `concurrent`, and
either the stream is unordered or the collector is
`unordered`,
then a concurrent reduction will be performed (see `Collector` for
details on concurrent reduction.)This is a terminal
operation.When executed in parallel, multiple intermediate results may be
instantiated, populated, and merged so as to maintain isolation of
mutable data structures. Therefore, even when executed in parallel
with non-thread-safe data structures (such as `ArrayList`), no
additional synchronization is needed for a parallel reduction.
API Note:
The following will accumulate strings into an ArrayList:
```

     List<String> asList = stringStream.collect(Collectors.toList());
 
```
The following will classify `Person` objects by city:
```

     Map<String, List<Person>> peopleByCity
         = personStream.collect(Collectors.groupingBy(Person::getCity));
 
```
The following will classify `Person` objects by state and city,
cascading two `Collector`s together:
```

     Map<String, Map<String, List<Person>>> peopleByStateAndCity
         = personStream.collect(Collectors.groupingBy(Person::getState,
                                                      Collectors.groupingBy(Person::getCity)));
 
```

Type Parameters:
`R` - the type of the result
`A` - the intermediate accumulation type of the `Collector`
Parameters:
`collector` - the `Collector` describing the reduction
Returns:
the result of the reduction
See Also:
`collect(Supplier, BiConsumer, BiConsumer)`,
`Collectors`

