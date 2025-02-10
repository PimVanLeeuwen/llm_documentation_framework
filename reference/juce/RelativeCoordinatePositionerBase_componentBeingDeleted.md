#### componentBeingDeleted()


 void RelativeCoordinatePositionerBase::componentBeingDeleted ( Component & component ) overridevirtual 
 

Called when the component is in the process of being deleted.This callback is made from inside the destructor, so be very, very cautious about what you do in here.In particular, bear in mind that it's the Component base class's destructor that calls this so if the object that's being deleted is a subclass of Component, then the subclass layers of the object will already have been destructed when it gets to this point!Parameters

 component the component that was deleted 
 


Reimplemented from ComponentListener.