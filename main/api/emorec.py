import pickle
import warnings
warnings.filterwarnings("ignore")
with open(r'E:\Major-Project\Major-Project SPEECH\main\api\nlp.pkl', 'rb') as f:
    classifier = pickle.load(f)  

with open(r'E:\Major-Project\Major-Project SPEECH\main\api\transform.pkl', 'rb') as f:
    cv = pickle.load(f) 


def senti_api(data):
    data_arr = [data]
    # Vector transfromation
    vect = cv.transform(data_arr).toarray()   ## transform them to array for prediction
    prediction = classifier.predict(vect) ## predict over the model
    string = " "                          ## an empty string , will be used for getting the emotion  
    emotion = string.join(prediction)  

    return emotion

