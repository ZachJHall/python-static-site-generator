import os
import json

def h1(content):
    return "<h1>" + content + "</h1>"

def a(src, content):
    return "<a href=" + src + ">" + content + "</a>"

def blogPost(name, content, postDir):

    tPost = open(postDir + name+".html", "w")
    tPost.write("<h1>" + name + "</h1>")
    tPost.write("<p>" + content + "</p>")
    tPost.write("<a href='../index.html'>Index</a>")

def genIndex():
    postDir = "posts/"
    output = "public/"
    if not os.path.exists("public"):
        os.mkdir("public")
    if not os.path.exists("public/posts"):
        os.mkdir("public/posts")


    siteInfo = open('site.json')
    data = json.load(siteInfo)

    print(data)

    

    index = open(output + "index.html", "w")
    index.write(h1(data["site-name"]))
    
    for filename in os.listdir("markdown"):
        index.write("\n")


        temp = open("markdown/" + filename)
        blogPost(filename[:-4], temp.read(), output + postDir)

        index.write( a(postDir + filename[:-4]+".html", filename[:-4]) + "\b")
        temp.close()





genIndex()
