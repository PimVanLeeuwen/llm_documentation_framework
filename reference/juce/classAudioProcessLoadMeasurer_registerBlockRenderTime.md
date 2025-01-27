#### registerBlockRenderTime()


 void AudioProcessLoadMeasurer::registerBlockRenderTime ( double millisecondsTaken ) 
 

Can be called manually to add the time of a callback to the stats.Normally you probably would never call this it's simpler and more robust to use a ScopedTimer to measure the time using an RAII pattern.