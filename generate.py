import os
import json

postDir = "posts/"
output = "public/"

def h1(content):
    return "<h1>" + content + "</h1>"

def a(src, content):
    return "<a href=" + src + ">" + content + "</a>"

def blogPost(name, content, postDir):

    Post = open(postDir + name+".html", "w")
    Post.write("<header>")
    Post.write("\b")
    Post.write("<title>" + siteInfo["site-name"] + "</title>" )
    Post.write("\b")
    Post.write("</header>")

    Post.write("<h1>" + name + "</h1>")
    Post.write("<p>" + content + "</p>")
    Post.write("<a href='../index.html'>Index</a>")

def genIndex():

    index = open(output + "index.html", "w")
    index.write(h1(siteInfo["site-name"]))
    
    for filename in os.listdir("markdown"):
        index.write("\n")


        temp = open("markdown/" + filename)
        blogPost(filename[:-4], temp.read(), output + postDir)

        index.write( a(postDir + filename[:-4]+".html", filename[:-4]) + "\b")
        temp.close()

def getSiteInfo():
    siteInfo = open('site.json')
    return json.load(siteInfo)



def main():
 
    if not os.path.exists("public"):
        os.mkdir("public")
    if not os.path.exists("public/posts"):
        os.mkdir("public/posts")

    genIndex()


siteInfo = getSiteInfo()
main()