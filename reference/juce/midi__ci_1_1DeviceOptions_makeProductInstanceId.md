#### makeProductInstanceId()


 static std::array< char, 16 > midi\_ci::DeviceOptions::makeProductInstanceId ( Random & random ) static 
 

Creates a random product instance ID.This isn't really recommended it's probably better to have a unique ID that remains persistent after a restart.References Random::nextInt().