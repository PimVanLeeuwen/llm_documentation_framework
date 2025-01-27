```
public class ServiceConfigurationError
extends Error
```
Error thrown when something goes wrong while loading a service provider.This error will be thrown in the following situations:The format of a provider-configuration file violates the specification;An `IOException` occurs while reading a
provider-configuration file;A concrete provider class named in a provider-configuration file
cannot be found;A concrete provider class is not a subclass of the service class;A concrete provider class cannot be instantiated; orSome other kind of error occurs.
Since:
1.6
See Also:
Serialized Form
