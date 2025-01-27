#### noteTimbreChanged()


 void MPESynthesiser::noteTimbreChanged ( MPENote changedNote ) overrideprotectedvirtual 
 

Will find any voice that is currently playing changedNote, update its currently playing note, and call its noteTimbreChanged method.This method will be called automatically according to the midi data passed into renderNextBlock(). Do not call it yourself.Reimplemented from MPEInstrument::Listener.