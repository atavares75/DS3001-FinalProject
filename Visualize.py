import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from DataLoad import data, raw_data
from sklearn.metrics import max_error, mean_absolute_error, mean_squared_error
import matplotlib.pyplot as plt
import pandas as pd

def correlation_heatmap():
    data.corr()
    f,ax=plt.subplots(figsize=(15,15))
    sns.heatmap(data.corr(),annot=True,linewidth=0.5,fmt='.3f',ax=ax)
    plt.show()

def gender_bar_graph():
    sns.catplot(x="sex", kind="count",palette="magma", data=data, height = 6)
    plt.title("Gender of students : F - female,M - male")
    plt.show()

def age_histogram():
    data.age.unique()
    plt.figure(figsize=(10,5))
    plt.hist(data.age,bins=7,color="purple",width=0.8,density=True)
    plt.xlabel("Age")
    plt.ylabel("Percentage")
    plt.show()

def print_results(y_pred, y_test, model):
    mse = mean_squared_error(y_test, y_pred)
    # df = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred.flatten()})
    # df1 = df.head(25)
    # df1.plot(kind='bar', figsize=(16, 10))
    # plt.grid(which='major', linestyle='-', linewidth='0.5', color='green')
    # plt.grid(which='minor', linestyle=':', linewidth='0.5', color='black')
    # plt.show()
    # print(model, ': \n', 'mean squared error: ', mse)
    return mse

def show_dalc_consumption():
    pass

def absences_box_plot():    
    raw_data['num_abs'] = np.nan
    df = [raw_data]
    for col in df:
        col.loc[col['absences'] == 0 , 'num_abs'] = '0 absences'
        col.loc[col['absences'].between(1, 10) , 'num_abs'] = '1 to 10 absences'
        col.loc[col['absences'].between(11, 20), 'num_abs'] = '16 to 20 absences'
        col.loc[col['absences'] > 20 , 'num_abs'] = '> 20 absences'
    plt.figure(figsize=(18,7))
    plt.title("Box plot for final grades depending on the number of absences")
    sns.boxplot(y="num_abs", x="G3", data = raw_data , orient="h", palette = 'rainbow')
