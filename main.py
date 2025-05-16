from sklearn.neighbors import KNeighborsClassifier
df = open("iris/bezdekIris.data", "r").read().split("\n")
X_learn = []
y_learn = []
X_test = []
y_test = []
answers = []
for i in range(102):
    string = df[i].split(",")
    mas = []
    for j in range(len(string) - 1):
        mas.append(float(string[j]))
    X_learn.append(mas)
    y_learn.append(string[-1])
for i in range(102, 150):
    string = df[i].split(",")
    mas = []
    for j in range(len(string) - 1):
        mas.append(float(string[j]))
    X_test.append(mas)
    y_test.append(string[-1])
reg = KNeighborsClassifier(n_neighbors=3)
reg.fit(X_learn, y_learn)
incorrect = 0
all = 0
for i in range(len(y_test)):
    result = reg.predict([X_test[i]])
    if result != y_test[i]:
        incorrect += 1
    all += 1
print("Вероятность правильного ответа", incorrect/all)
X_test = []
for i in range(4):
    a = float(input("Введите численную характеристику ириса>> "))
    X_test.append(a)
print("Вероятнее всего это", reg.predict([X_test])[0])