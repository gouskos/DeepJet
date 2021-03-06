


def fixLayersContaining(m, fixOnlyContaining):
    isseq=(not hasattr(fixOnlyContaining, "strip") and
            hasattr(fixOnlyContaining, "__getitem__") or
            hasattr(fixOnlyContaining, "__iter__"))
    if not isseq:
        fixOnlyContaining=[fixOnlyContaining]
        
    for layidx in range(len(m.layers)):
        for ident in fixOnlyContaining:
            if len(ident) and ident in m.get_layer(index=layidx).name:
                m.get_layer(index=layidx).trainable=False
    return m


def loadModelAndFixLayers(filename,fixOnlyContaining):
    #import keras
    from keras.models import load_model
    
    m=load_model(filename)
    
    fixLayersContaining(m, fixOnlyContaining)
                
    return m