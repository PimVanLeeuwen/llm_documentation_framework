```
public abstract class AbstractSet<E>
extends AbstractCollection<E>
implements Set<E>
```
This class provides a skeletal implementation of the Set
interface to minimize the effort required to implement this
interface.The process of implementing a set by extending this class is identical
to that of implementing a Collection by extending AbstractCollection,
except that all of the methods and constructors in subclasses of this
class must obey the additional constraints imposed by the Set
interface (for instance, the add method must not permit addition of
multiple instances of an object to a set).Note that this class does not override any of the implementations from
the AbstractCollection class. It merely adds implementations
for equals and hashCode.This class is a member of the
Java Collections Framework.
Since:
1.2
See Also:
`Collection`,
`AbstractCollection`,
`Set`
