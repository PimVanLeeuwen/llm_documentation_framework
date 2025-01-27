#### deleteAllChildren()


 void Component::deleteAllChildren ( ) 
 

Removes and deletes all of this component's children.My advice is to avoid this method! It's an old function that is only kept here for backwardscompatibility with legacy code, and should be viewed with extreme suspicion by anyone attempting to write modern C++. In almost all cases, it's much smarter to manage the lifetimes of your child components via modern RAII techniques such as simply making them member variables, or using std::unique\_ptr, OwnedArray, etc to manage their lifetimes appropriately.See alsoremoveAllChildren