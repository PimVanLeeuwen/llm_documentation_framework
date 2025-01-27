#### setAll

```
public static void setAll(double[] array,
                          IntToDoubleFunction generator)
```
Set all elements of the specified array, using the provided
generator function to compute each element.If the generator function throws an exception, it is relayed to
the caller and the array is left in an indeterminate state.
Parameters:
`array` - array to be initialized
`generator` - a function accepting an index and producing the desired
value for that position
Throws:
`NullPointerException` - if the generator is null
Since:
1.8

