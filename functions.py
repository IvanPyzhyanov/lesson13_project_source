import json

#making function which get data from json file with posts
def read_json():
    with open("posts.json", "r") as file:
        return json.load(file)

#taking tags (words which starts from #) from loaded json file
def take_tags():
    tags_list = []
    for a in read_json():
        for pic, content in a.items():
            for i in content.split():
                if i[0]=="#":
                    tags_list.append(i[1:])
    return tags_list


#looking for the post which contain selected tag
def looking_tag(tag):
    posts_by_tag = [x for x in read_json() if tag in x["content"]]
    return posts_by_tag

