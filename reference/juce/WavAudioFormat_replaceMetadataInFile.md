#### replaceMetadataInFile()


 bool WavAudioFormat::replaceMetadataInFile ( const File & wavFile, 
 
 const StringPairArray & newMetadata ) 

Utility function to replace the metadata in a wav file with a new set of values.If possible, this cheats by overwriting just the metadata region of the file, rather than by copying the whole file again.

Member Data Documentation