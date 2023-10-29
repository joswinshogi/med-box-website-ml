import pickle

model = pickle.load(open('Log_Reg_classification.pkl','rb'))

def pred_model(parameters):
    res = model.predict(parameters)[0]
    if res == 0:
        print('No risk of Heart Attack')
    else:
        print('There is risk of Heart Attack')

param = [[0, 37, 185]]
pred_model(param)