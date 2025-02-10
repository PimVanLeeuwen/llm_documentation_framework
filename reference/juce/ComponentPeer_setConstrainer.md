#### setConstrainer()


 void ComponentPeer::setConstrainer ( ComponentBoundsConstrainer \* newConstrainer ) noexcept 
 

Sets a constrainer to use if the peer can resize itself.The constrainer won't be deleted by this object, so the caller must manage its lifetime.