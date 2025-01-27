#### load

```
public static <S> ServiceLoader<S> load(Class<S> service)
```
Creates a new service loader for the given service type, using the
current thread's context class loader.An invocation of this convenience method of the form
```

 ServiceLoader.load(service)
```
is equivalent to
```

 ServiceLoader.load(service,
                    Thread.currentThread().getContextClassLoader())
```

Type Parameters:
`S` - the class of the service type
Parameters:
`service` - The interface or abstract class representing the service
Returns:
A new service loader

