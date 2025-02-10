#### getInputLatencyInSamples()


 virtual int AudioIODevice::getInputLatencyInSamples ( ) pure virtual 
 

Returns the device's input latency.This is the delay in samples between some audio actually arriving at the soundcard, and the callback getting passed this block of data.