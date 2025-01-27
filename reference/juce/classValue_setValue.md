#### setValue()


 void Value::setValue ( const var & newValue ) 
 

Sets the current value.You can also use operator= to set the value.If there are any listeners registered, they will be notified of the change asynchronously.Referenced by ValueTreePropertyWithDefault::operator=(), and StandalonePluginHolder::reloadAudioDeviceState().