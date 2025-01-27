#### asList

```
@SafeVarargs
public static <T> List<T> asList(T... a)
```
Returns a fixed-size list backed by the specified array. (Changes to
the returned list "write through" to the array.) This method acts
as bridge between array-based and collection-based APIs, in
combination with `Collection.toArray()`. The returned list is
serializable and implements `RandomAccess`.This method also provides a convenient way to create a fixed-size
list initialized to contain several elements:
```

     List<String> stooges = Arrays.asList("Larry", "Moe", "Curly");
 
```

Type Parameters:
`T` - the class of the objects in the array
Parameters:
`a` - the array by which the list will be backed
Returns:
a list view of the specified array

