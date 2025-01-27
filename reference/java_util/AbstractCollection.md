```
public abstract class AbstractCollection<E>
extends Object
implements Collection<E>
```
This class provides a skeletal implementation of the Collection
interface, to minimize the effort required to implement this interface.To implement an unmodifiable collection, the programmer needs only to
extend this class and provide implementations for the iterator and
size methods. (The iterator returned by the iterator
method must implement hasNext and next.)To implement a modifiable collection, the programmer must additionally
override this class's add method (which otherwise throws an
UnsupportedOperationException), and the iterator returned by the
iterator method must additionally implement its remove
method.The programmer should generally provide a void (no argument) and
Collection constructor, as per the recommendation in the
Collection interface specification.The documentation for each non-abstract method in this class describes its
implementation in detail. Each of these methods may be overridden if
the collection being implemented admits a more efficient implementation.This class is a member of the
Java Collections Framework.
Since:
1.2
See Also:
`Collection`
