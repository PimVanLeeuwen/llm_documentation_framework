#### processMessage()


 void midi\_ci::Device::processMessage ( ump::BytesOnGroup ) overridevirtual 
 

To be called with any message that should be processed by the device.This should only be passed complete CI messages you might find the Extractor class useful for parsing a stream of Universal MIDI Packets and extracting the CI messages. Note that this function does not synchronise with any other member function of this class. This means that you must not call this directly from the MIDI input thread if there's any chance of other member functions being called on the same instance simultaneously from other threads. It's probably easiest to send all messages onto the main thread and to limit interactions with the Device to that thread.Implements midi\_ci::DeviceMessageHandler.