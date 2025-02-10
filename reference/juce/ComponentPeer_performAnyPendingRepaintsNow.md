#### performAnyPendingRepaintsNow()


 virtual void ComponentPeer::performAnyPendingRepaintsNow ( ) pure virtual 
 

This can be called (from the message thread) to cause the immediate redrawing of any areas of this window that need repainting.You shouldn't ever really need to use this, it's mainly for special purposes like supporting audio plugins where the host's event loop is out of our control.