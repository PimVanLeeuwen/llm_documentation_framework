#### invokeAll

```
public static <T extends ForkJoinTask<?>> Collection<T> invokeAll(Collection<T> tasks)
```
Forks all tasks in the specified collection, returning when
`isDone` holds for each task or an (unchecked) exception
is encountered, in which case the exception is rethrown. If
more than one task encounters an exception, then this method
throws any one of these exceptions. If any task encounters an
exception, others may be cancelled. However, the execution
status of individual tasks is not guaranteed upon exceptional
return. The status of each task may be obtained using `getException()` and related methods to check if they have been
cancelled, completed normally or exceptionally, or left
unprocessed.
Type Parameters:
`T` - the type of the values returned from the tasks
Parameters:
`tasks` - the collection of tasks
Returns:
the tasks argument, to simplify usage
Throws:
`NullPointerException` - if tasks or any element are null

