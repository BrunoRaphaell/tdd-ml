import os
import pickle


def save_model_pkl(model, model_name):
    path = "model/"
    
    # se não existe, cria
    if not os.path.exists(path):
        os.mkdir(path)
    
    # salva o modelo
    pickle.dump(model, open(path + model_name + ".pkl", "wb"))
    
def load_artefacts(model_name):
    path = "model/"
    
    # carrega o modelo
    model = pickle.load(open(path + model_name + ".pkl", "rb"))
    return model


def make_prediction(model, X):
    return model.predict(X)


