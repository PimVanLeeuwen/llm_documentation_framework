#### create() [2/2]


 static std::optional< RequestID > midi\_ci::RequestID::create ( std::byte value ) static 
 

Constructs a RequestID if the provided value is valid, i.e.its most significant bit is not set. Otherwise, returns nullopt.References create().