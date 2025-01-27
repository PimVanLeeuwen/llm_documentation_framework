```
public final class OptionalDouble
extends Object
```
A container object which may or may not contain a `double` value.
If a value is present, `isPresent()` will return `true` and
`getAsDouble()` will return the value.Additional methods that depend on the presence or absence of a contained
value are provided, such as `orElse()`
(return a default value if value not present) and
`ifPresent()` (execute a block
of code if the value is present).This is a value-based
class; use of identity-sensitive operations (including reference equality
(`==`), identity hash code, or synchronization) on instances of
`OptionalDouble` may have unpredictable results and should be avoided.
Since:
1.8
