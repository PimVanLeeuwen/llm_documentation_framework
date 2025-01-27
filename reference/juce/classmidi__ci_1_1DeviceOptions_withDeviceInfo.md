#### withDeviceInfo()


 DeviceOptions midi\_ci::DeviceOptions::withDeviceInfo ( const ump::DeviceInfo & x ) const nodiscard 
 

Basic information about the device used to determine manufacturer, model, etc.In order to populate this correctly, you'll need to register with the MIDI association otherwise you might accidentally end up using IDs that are already assigned to other companies/individuals.References withMember(), and x.