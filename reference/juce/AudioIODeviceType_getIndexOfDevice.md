#### getIndexOfDevice()


 virtual int AudioIODeviceType::getIndexOfDevice ( AudioIODevice \* device, bool asInput ) const pure virtual 
 

Returns the index of a given device in the list of device names.If asInput is true, it shows the index in the inputs list, otherwise it looks for it in the outputs list.