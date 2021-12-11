import json

def read_json(filename):
    '''making function which get data from json file with posts'''
    with open(filename, "r", encoding="UTF-8") as file:
        return json.load(file)


def take_tags(json_load):
    '''taking tags (words which starts from #) from loaded json file'''
    tags_list = []
    for a in json_load:
        for pic, content in a.items():
            for i in content.split():
                if i[0]=="#":
                    tags_list.append(i[1:])
    return tags_list



def looking_tag(tag, filename):
    '''looking for the post which contain selected tag'''
    posts_by_tag = [x for x in read_json(filename) if tag in x["content"]]
    return posts_by_tag



def add_post(post):
    '''recording new post (picture link and text) in json data file'''
    with open("posts.json", "r", encoding="UTF-8") as file:
        ex_posts = json.load(file)
        ex_posts.append(post)
    with open("posts.json", "w", encoding="UTF-8") as file:
        json.dump(ex_posts, file, ensure_ascii=False, indent=4)
    return "saving complete"
