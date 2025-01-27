#### loadInstalled

```
public static <S> ServiceLoader<S> loadInstalled(Class<S> service)
```
Creates a new service loader for the given service type, using the
extension class loader.This convenience method simply locates the extension class loader,
call it extClassLoader, and then returns
```

 ServiceLoader.load(service, extClassLoader)
```
If the extension class loader cannot be found then the system class
loader is used; if there is no system class loader then the bootstrap
class loader is used.This method is intended for use when only installed providers are
desired. The resulting service will only find and load providers that
have been installed into the current Java virtual machine; providers on
the application's class path will be ignored.
Type Parameters:
`S` - the class of the service type
Parameters:
`service` - The interface or abstract class representing the service
Returns:
A new service loader

