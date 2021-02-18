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
