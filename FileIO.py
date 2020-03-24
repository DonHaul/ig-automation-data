import json
import numpy as np
import random
import datetime
import os
import pickle
import matplotlib.pyplot as plt
import scipy.io
import sys

saveInc=0

def CreateFolderIncremental(directory):
    
    count=1
    path = directory  + str(count)

    while os.path.exists(path):
        count=count+1
        path = directory + str(count)

    os.makedirs(path)

    return path




def CreateFolder(directory,putDate=True,suffix=''):

    path=directory
    if(putDate==True):
        path=path +  datetime.datetime.now().strftime("%Y-%m-%d_%H:%M:%S")+'_'+suffix

    if not os.path.exists(path):
        os.makedirs(path)

    return path
    

def GetFileName(directory):

    names = directory.split("/")
    myString = names[len(names)-1]
    myString = myString[0:myString.find(".")]

    return myString

 


def savePCs(filename,pcs,pc):
    '''
    saves a merged point cloud and also the separated pointclouds
    Args:
        filename String: what should the name be
        pcs [open3d.pointcloud]: list of all the retrieved pointclouds
    '''
    global saveInc
    saveInc=saveInc+1
    print(saveInc)
    print(filename)
    filename = filename+"_"+str(saveInc)


    #creates a file for the merged pointcloud
    open3d.write_point_cloud("./PC/"+filename+".ply", pc)

    #create a folder for the unmerged pointclouds
    try:
        os.mkdir("./PC/"+filename)
    except:
        print("PA")
    
    
    #save the individual pointclouds
    for i in range(len(pcs)):
        print(pcs[i])
        open3d.write_point_cloud("./PC/"+filename+"/pointcloud"+str(i)+".ply", pcs[i])





def putFileWithJson(data,filename=None,folder=None,animal=False,putDate=False):
    '''
    puts dictionary into a json
    Args:
        data: data to put in the file
        filename: name of the file
        folder: place to save the file to
    '''

    if folder is None:
        folder = "./tmp"
    
    if filename is None:
        filename = ""

    saveName =folder + "/" + filename

    if animal:
        saveName = saveName + "_" + GetAnimalName()

    if putDate:
        saveName = saveName + "_" +  datetime.datetime.now().strftime("%d-%m-%Y_%H:%M:%S")


    f = open(saveName+".json","w")

    #save files
    json.dump(data,f)
    
    f.close()

    print("Saved File: "+str(saveName)+".json")


def getFromPickle(filename):
    '''
    Gets data from pickle file
    Args:
        filename: name of the file to fetch the data from
    '''

    p={}

    try:
        f= open(filename,"rb")
        p  =  pickle.load(f)
        f.close
    except IOError:
        return None
    #raise Exception("No Such File")

        
    return p


def saveAsPickle(name,data,path="pickles/",putDate=True,animal=True):
    '''
        Args:
        name (str):Filename
        key (str):Name of the variable will be saved as
        data (anything): Data to be saved in the dict
        path (str): Where will it be saved
        putData (bool,optional): whether or not the current data is concatenated to the file name
    '''

    saveName = path+name #path and filename



    #add date
    if putDate:
        saveName = saveName+"_" + datetime.datetime.now().strftime("%Y-%m-%d_%H:%M:%S")

    if animal :
        saveName = saveName+"_"+GetAnimalName()
    
    f= open(saveName+".pickle","wb")    #open file and write bytes
    
    pickle.dump(data,f)          #dump stuff into that file
    
    f.close

    print("Data Saved on: " + saveName +".pickle")


    return saveName + ".pickle"


def getJsonFromFile(filename):
    '''
    Get data from the json file
    Args:
        filename: path to the file to retrieve data from
    '''

    try:
        f=open(filename,"r")
    
        data = json.load(f)
        f.close()

        return data

    except IOError:
      print("Error: File does not appear to exist.")
      return None
