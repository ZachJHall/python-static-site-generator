import os
import json
import markdown

postDir = "posts/"
output = "public/"
posts = os.listdir("markdown")

def h1(content):
    return "<h1>" + content + "</h1>"

def a(src, content):
    return "<a href=" + src + ">" + content + "</a>"

def blogPost(name, content, postDir):
	with open('./templates/post.html', 'r') as postTemplate, open(postDir +name + ".html", "w") as Post:
    	
		for line in postTemplate:
			if(line.strip('\n') == "[content]"):
				Post.write("<h1>" + name  + "</h1>")
				Post.write(markdown.markdown(content))
			else:
				Post.write(line)

def genPosts():
	for post in posts:
		name = post[0]

		with open('./templates/post.html', 'r') as postTemplate, open(output+postDir +name + ".html", "w") as postOutput:
		
			for line in postTemplate:
				if(line.strip('\n') == "[content]"):
					postOutput.write("<h1>" + name  + "</h1>")
					#Post.write(markdown.markdown(content))
				else:
					postOutput.write(line)
def genIndex():
    with open('./templates/index.html', 'r') as indexTemplate, open(output + "index.html", 'w') as index:
        for line in indexTemplate:
            if(line.strip('\n') == "[content]"):
                index.write('\n')
                for file in posts[-3:]:
                    index.write( a(postDir + file[0] + ".html", file[0]) + "\b")
                    index.write('\n')
            else:
                index.write(line)
    
def main():
    if not os.path.exists("public"):
        os.mkdir("public")
    if not os.path.exists("public/posts"):
        os.mkdir("public/posts")
    genPosts()
    genIndex()

main()
print(posts)
