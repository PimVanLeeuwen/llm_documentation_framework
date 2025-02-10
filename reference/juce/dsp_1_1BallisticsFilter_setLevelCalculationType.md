#### setLevelCalculationType()


template<typename SampleType > 

 void dsp::BallisticsFilter< SampleType >::setLevelCalculationType ( LevelCalculationType newCalculationType ) 
 

Sets how the filter levels are calculated.Level calculation in digital envelope followers is usually performed using peak detection with a rectifier function (like std::abs) and filtering, which returns an envelope dependant on the peak or maximum values of the signal amplitude.To perform an estimation of the average value of the signal you can use an RMS (root mean squared) implementation of the ballistics filter instead. This is useful in some compressor and noisegate designs, or in specific types of volume meters.