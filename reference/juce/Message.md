The base class for objects that can be sent to a MessageListener.If you want to send a message that carries some kind of custom data, just create a subclass of Message with some appropriate member variables to hold your data.Always create a new instance of a Message object on the heap, as it will be deleted automatically after the message has been delivered.See alsoMessageListener, MessageManager, ActionListener, ChangeListener 

Member Typedef Documentation


◆ Ptr


 using Message::Ptr = ReferenceCountedObjectPtr<Message> 
 


Constructor & Destructor Documentation


◆ Message()


 Message::Message ( ) noexcept 
 

Creates an uninitialised message.

◆ ~Message()


 Message::~Message ( ) override 
 