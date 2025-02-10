#### canPlaySound()


 bool SamplerVoice::canPlaySound ( SynthesiserSound \* ) overridevirtual 
 

Must return true if this voice object is capable of playing the given sound.If there are different classes of sound, and different classes of voice, a voice can choose which ones it wants to take on.A typical implementation of this method may just return true if there's only one type of voice and sound, or it might check the type of the sound object passedin and see if it's one that it understands.Implements SynthesiserVoice.