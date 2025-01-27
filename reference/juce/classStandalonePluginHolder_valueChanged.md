#### valueChanged()


 void StandalonePluginHolder::valueChanged ( Value & value ) overridevirtual 
 

Called when a Value object is changed.Note that the Value object passed as a parameter may not be exactly the same object that you registered the listener with it might be a copy that refers to the same underlying ValueSource. To find out, you can call Value::refersToSameSourceAs().Implements Value::Listener.References Value::getValue(), and muteInput.