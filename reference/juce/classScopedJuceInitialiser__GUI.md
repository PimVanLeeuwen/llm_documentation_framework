A utility object that helps you initialise and shutdown JUCE correctly using an RAII pattern.When the first instance of this class is created, it calls initialiseJuce\_GUI(), and when the last instance is deleted, it calls shutdownJuce\_GUI(), so that you can easily be sure that as long as at least one instance of the class exists, the library will be initialised.This class is particularly handy to use at the beginning of a console app's main() function, because it'll take care of shutting down whenever you return from the main() call.Be careful with your threading though to be safe, you should always make sure that these objects are created and deleted on the message thread.

Constructor & Destructor Documentation


◆ ScopedJuceInitialiser\_GUI()


 ScopedJuceInitialiser\_GUI::ScopedJuceInitialiser\_GUI ( ) 
 

The constructor simply calls initialiseJuce\_GUI().

◆ ~ScopedJuceInitialiser\_GUI()


 ScopedJuceInitialiser\_GUI::~ScopedJuceInitialiser\_GUI ( ) 
 

The destructor simply calls shutdownJuce\_GUI().