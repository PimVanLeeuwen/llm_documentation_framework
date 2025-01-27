#### prepare()


 void dsp::Convolution::prepare ( const ProcessSpec & ) 
 

Must be called before first calling process.In general, calls to loadImpulseResponse() load the impulse response (IR) asynchronously. The IR will become active once it has been completely loaded and processed, which may take some time.Calling prepare() will ensure that the IR supplied to the most recent call to loadImpulseResponse() is fully initialised. This IR will then be active during the next call to process(). It is recommended to call loadImpulseResponse() before prepare() if a specific IR must be active during the first process() call.