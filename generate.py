import os
import json

postDir = "posts/"
output = "public/"

def h1(content):
    return "<h1>" + content + "</h1>"

def a(src, content):
    return "<a href=" + src + ">" + content + "</a>"

def blogPost(name, content, postDir):
	with open('./templates/post.html', 'r') as postTemplate, open(postDir +name + ".html", "w") as Post:
    	
		for line in postTemplate:
			if(line.strip('\n') == "[content]"):
				Post.write("<h1>" + name  + "</h1>")
				Post.write("<p>" + content + "<p>")
			else:
				Post.write(line)

def genIndex():
    with open('./templates/index.html', 'r') as indexTemplate, open(output + "index.html", 'w') as index:
        for line in indexTemplate:
            if(line.strip('\n') == "[content]"):
                for filename in os.listdir("markdown"):
                    index.write('\n')
                    temp = open("markdown/" + filename)
                    blogPost(filename[:-4], temp.read(), output + postDir)
                    index.write( a(postDir + filename[:-4]+".html", filename[:-4]) + "\b")
                    temp.close()
            else:
                index.write(line)

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
