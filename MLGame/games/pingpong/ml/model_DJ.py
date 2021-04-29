#####
import pickle
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn import metrics

from sklearn.ensemble import RandomForestClassifier#
from sklearn.metrics import classification_report, confusion_matrix

col_names = ["ball_x", "ball_y", "ball_speed_x", "ball_speed_y", "platform_x", "blocker_x"]

file = open("/home/auyu/E94086107/MLGame/games/pingpong/log_1/data(1).pickle","rb")
data = pickle.load(file)
file.close()

#####
game_info = data["ml_1P"]["scene_info"]
game_command = data["ml_1P"]["command"]

#####
for i in range (2,51):
	path = "/home/auyu/E94086107/MLGame/games/pingpong/log_1/data("+str(i)+").pickle"
	file = open(path,"rb")
	data = pickle.load(file)
	game_info = game_info + data["ml_1P"]["scene_info"]
	game_command = game_command + data["ml_1P"]["command"]
	file.close

#####
g = game_info[1]

feature = np.array([g["ball"][0], g["ball"][1], g["ball_speed"][0], g["ball_speed"][1], g["platform_1P"][0], g["blocker"][0]])
print(feature)
print(game_command[1])
if game_command[1] == "NONE":
	game_command[1] = 0
elif game_command[1] == "MOVE_LEFT":
	game_command[1] = 1
else:
	game_command[1] = 2

#####
for i in range (2, len(game_info)-1):
	g = game_info[i]
	feature = np.vstack((feature, [g["ball"][0], g["ball"][1], g["ball_speed"][0], g["ball_speed"][1], g["platform_1P"][0], g["blocker"][0]]))
	if game_command[i] == "NONE":
		game_command[i] = 0
	elif game_command[i] == "MOVE_LEFT":
		game_command[i] = 1
	else:
		game_command[i] = 2

#feature_cols = ["ball_x", "ball_y", "ball_speed_x", "ball_speed_y", "platform_x", "blocker_x"]

answer = np.array(game_command[1:-1])

print(feature.shape)
print(answer.shape)

#####
x_train, x_test, y_train, y_test = train_test_split(feature, answer, test_size=0.3, random_state = 1)

forest = RandomForestClassifier(n_estimators=120, max_depth=100)
forest = forest.fit(x_train, y_train)

predicted = forest.predict(x_test)

file = open("model_randomforest_429_1426.pickle", "wb")
pickle.dump(forest, file)
file.close()

###
print("Accuracy score (validation): {0:.3f}".format(forest.score(x_test, y_test)))
print("Confusion Matrix for Raandom Forests:")
print(confusion_matrix(y_test, predicted))
print()
print("Classification Report for Random Forests")
print(classification_report(y_test, predicted))
