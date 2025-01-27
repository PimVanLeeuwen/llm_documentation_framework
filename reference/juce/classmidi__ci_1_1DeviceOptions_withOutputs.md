#### withOutputs()


 DeviceOptions midi\_ci::DeviceOptions::withOutputs ( std::vector< DeviceMessageHandler \* > x ) const nodiscard 
 

One or more DeviceMessageHandlers that should receive callbacks with any messages that the device wishes to send.Referenced DeviceMessageHandlers must outlive any Device constructed from these options.References withMember(), and x.