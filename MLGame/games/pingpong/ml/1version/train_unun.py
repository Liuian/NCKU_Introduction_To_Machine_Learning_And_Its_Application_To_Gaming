import pickle
import os
import numpy as np
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import  classification_report, confusion_matrix
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import StratifiedShuffleSplit

''' Import os package which used to get all pickle files in folder '''
file_dir = os.path.join(
    os.path.dirname(os.path.realpath('__file__')), "..", "log")
# print(file_dir)
file_dir = file_dir + "\\"
print("file_directory = ", file_dir)
file_path = os.listdir(file_dir)
print('total num of records : {}'.format(len(file_path)))

''' Load first pickle file
    Used to check information is correct '''
first_file = open(file_dir + file_path[0], "rb")
data = pickle.load(first_file)
first_file.close()
scene_info = data['ml_1P']['scene_info']
command = data['ml_1P']['command']

''' Load all the pickle files in log folder '''
for i in file_path[1:]:
#     print(file_dir + i)
    file = open(file_dir + i, "rb")
    data = pickle.load(file)
    scene_info = scene_info + data['ml_1P']['scene_info']
    command = command + data['ml_1P']['command']
    file.close()
    
print(len(scene_info))
print(len(command))

k = range(1, len(scene_info)-1)

ball_x = np.array([scene_info[i]['ball'][0] for i in k])
ball_y = np.array([scene_info[i]['ball'][1] for i in k])
ball_speed_x = np.array([scene_info[i+1]['ball'][0] - scene_info[i]['ball'][0] for i in k])
ball_speed_y = np.array([scene_info[i+1]['ball'][1] - scene_info[i]['ball'][1] for i in k])
direction = np.where(np.vstack((ball_speed_x, ball_speed_y)) > 0, [[1],[0]], [[2],[3]]).sum(axis=0)  # x y: ++1, +-4, -+2, --3
platform_1 = np.array([scene_info[i]['platform_1P'][0] for i in k])
target = np.where(np.array(command) == 'NONE', 0,
                  np.where(np.array(command) == 'MOVE_LEFT', -1, 1))[1:-1]  # [0] SERVE_TO_RIGHT, [1897] None
                  
X = np.hstack((ball_x.reshape(-1, 1),
               ball_y.reshape(-1, 1),
               ball_speed_x.reshape(-1, 1),
               ball_speed_y.reshape(-1, 1),
               direction.reshape(-1, 1),
               platform_1.reshape(-1, 1)))
            #  des_x.reshape(-1,1)))
y = target

# train data

#####/////
#資料劃分
#test_size:3:7(ask:test)
#x ans, y feature
x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=9)
from sklearn.tree import DecisionTreeClassifier
dtree=DecisionTreeClassifier()
dtree.fit(x_train,y_train)
predictions=dtree.predict(x_test)
print(classification_report(y_test,predictions))
print(confusion_matrix(y_test,predictions))

from sklearn.ensemble import RandomForestClassifier
rfc = RandomForestClassifier(n_estimators=50)
rfc.fit(x_train, y_train)
rfc_pred = rfc.predict(x_test)
print(confusion_matrix(y_test,rfc_pred))
print(classification_report(y_test,rfc_pred))
#儲存
file = open('RF1.pickle', 'wb')
pickle.dump(rfc, file)
file.close()
