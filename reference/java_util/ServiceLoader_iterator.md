#### iterator

```
public Iterator<S> iterator()
```
Lazily loads the available providers of this loader's service.The iterator returned by this method first yields all of the
elements of the provider cache, in instantiation order. It then lazily
loads and instantiates any remaining providers, adding each one to the
cache in turn.To achieve laziness the actual work of parsing the available
provider-configuration files and instantiating providers must be done by
the iterator itself. Its `hasNext` and
`next` methods can therefore throw a
`ServiceConfigurationError` if a provider-configuration file
violates the specified format, or if it names a provider class that
cannot be found and instantiated, or if the result of instantiating the
class is not assignable to the service type, or if any other kind of
exception or error is thrown as the next provider is located and
instantiated. To write robust code it is only necessary to catch `ServiceConfigurationError` when using a service iterator.If such an error is thrown then subsequent invocations of the
iterator will make a best effort to locate and instantiate the next
available provider, but in general such recovery cannot be guaranteed.Design Note
Throwing an error in these cases may seem extreme. The rationale for
this behavior is that a malformed provider-configuration file, like a
malformed class file, indicates a serious problem with the way the Java
virtual machine is configured or is being used. As such it is
preferable to throw an error rather than try to recover or, even worse,
fail silently.The iterator returned by this method does not support removal.
Invoking its `remove` method will
cause an `UnsupportedOperationException` to be thrown.
Specified by:
`iterator` in interface `Iterable<S>`
Implementation Note:
When adding providers to the cache, the `Iterator` processes resources in the order that the `ClassLoader.getResources(String)` method finds the service configuration
files.
Returns:
An iterator that lazily loads providers for this loader's
service

