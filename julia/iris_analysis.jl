Pkg.add("Plots")
Pkg.add("DataFrames")
Pkg.add("ScikitLearn")
Pkg.add("CSV")
Pkg.add("PyCall")
using PyCall
using Plots
using ScikitLearn
using CSV
using DataFrames
np=pyimport("numpy")
data=CSV.read("D:\\Datasets-master\\archive\\iris.csv",DataFrame)
select!(data,Not("Id"))
names(data)
describe(data)
plot(data.SepalLengthCm)
plot(data.SepalWidthCm)
plot(data.PetalLengthCm)
plot(data.PetalWidthCm)
scatter(data.SepalLengthCm,data.SepalWidthCm)
scatter(data.SepalLengthCm,data.PetalLengthCm)
scatter(data.SepalLengthCm,data.PetalWidthCm)
scatter(data.SepalWidthCm,data.Species)
pie(data.SepalLengthCm)
iris_x=convert(Array,data[:,[1,2,3,4]])
iris_y=convert(Array,data[:,5])
@sk_import model_selection: train_test_split
x_train, x_test, y_train, y_test=train_test_split(iris_x,iris_y,random_state=1)
@sk_import linear_model:LogisticRegression
log_reg=LogisticRegression()
fit!(log_reg,x_train,y_train)
prediction=predict(log_reg,x_test)
@sk_import metrics: accuracy_score
accuracy=accuracy_score(prediction,y_test)
print(accuracy)
