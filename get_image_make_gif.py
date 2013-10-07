#! /usr/bin/python 
# Retrieves images from the forthcoming image generation app that is currently
# located at http://localhost:8000/ 
# 


import urllib2
import urllib
#for retrieving images and all things http

SERVER = "http://localhost:8080"




def main():
    for i in range(100):
        try:
            img_name = "./images/test{0}.png".format(str(i).zfill(3))
            response =  urllib.urlretrieve(SERVER,img_name )
        except:
            print 'error'
    #print response.getcode()
    #print response.read()
        
if __name__ == '__main__':
    main()
