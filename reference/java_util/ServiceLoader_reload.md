#### reload

```
public void reload()
```
Clear this loader's provider cache so that all providers will be
reloaded.After invoking this method, subsequent invocations of the `iterator` method will lazily look up and instantiate
providers from scratch, just as is done by a newly-created loader.This method is intended for use in situations in which new providers
can be installed into a running Java virtual machine.

