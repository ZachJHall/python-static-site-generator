import os
import json
import markdown
import frontmatter

postDir = "posts/"
output = "public/"

def h1(content):
    return "<h1>" + content + "</h1>"

def a(src, content):
    return "<a href=" + src + ">" + content + "</a>"

def extractPosts():
    posts = [] 
    for post in os.listdir('markdown'):
        frontPost = frontmatter.load('markdown/' + post)
        
        fileName = post
        title = frontPost['title']
        author = frontPost['author']
        date = frontPost['date']
        content = frontPost.content
        posts.append((fileName, title, author, date, content))

    return posts

def genPosts():
    for post in posts:
        with open('./templates/post.html', 'r') as postTemplate, open(output+postDir + post[0][0] + ".html", "w") as postOutput:
            for line in postTemplate:
                if(line.strip('\n') == "[content]"):
                    postOutput.write("<h1>" + post[1]  + "</h1>")
                    postOutput.write(markdown.markdown(post[4]))
                else:
                    postOutput.write(line)
def genIndex():
    with open('./templates/index.html', 'r') as indexTemplate, open(output + "index.html", 'w') as index:
        for line in indexTemplate:
            if(line.strip('\n') == "[content]"):
                index.write('\n')
                for file in posts[-3:]:
                    index.write( a(postDir + file[0][0] + ".html", file[1]) + "<br>")
            else:
                index.write(line)
    
def main():
    if not os.path.exists("public"):
        os.mkdir("public")
    if not os.path.exists("public/posts"):
        os.mkdir("public/posts")
    genPosts()
    genIndex()

posts = sorted(extractPosts())
main()
print(posts)
