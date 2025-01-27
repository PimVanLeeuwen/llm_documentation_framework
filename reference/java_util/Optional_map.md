#### map

```
public <U> Optional<U> map(Function<? super T,? extends U> mapper)
```
If a value is present, apply the provided mapping function to it,
and if the result is non-null, return an `Optional` describing the
result. Otherwise return an empty `Optional`.
API Note:
This method supports post-processing on optional values, without
the need to explicitly check for a return status. For example, the
following code traverses a stream of file names, selects one that has
not yet been processed, and then opens that file, returning an
`Optional<FileInputStream>`:
```

     Optional<FileInputStream> fis =
         names.stream().filter(name -> !isProcessedYet(name))
                       .findFirst()
                       .map(name -> new FileInputStream(name));
 
```
Here, `findFirst` returns an `Optional<String>`, and then
`map` returns an `Optional<FileInputStream>` for the desired
file if one exists.
Type Parameters:
`U` - The type of the result of the mapping function
Parameters:
`mapper` - a mapping function to apply to the value, if present
Returns:
an `Optional` describing the result of applying a mapping
function to the value of this `Optional`, if a value is present,
otherwise an empty `Optional`
Throws:
`NullPointerException` - if the mapping function is null

