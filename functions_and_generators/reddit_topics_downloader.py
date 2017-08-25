import json
import requests
import itertools



#
# def reddit(topic):
#     r = requests.get("http://www.reddit.com/r/{0}.json".format(topic), headers={'user-agent': 'Chrome'})
#     def generator():
#
#     return generator
#
#     #"http://www.reddit.com/r/{0}.json".format(topic)
#     #http://www.reddit.com/r/python.json
#     # to limit number of topics for printing
#     #you can use itertools module: itertools.islice(golang(), 5).

# topic = "python"
#
# r = requests.get("http://www.reddit.com/r/{0}.json".format(topic), headers={'user-agent': 'Chrome'})
#
# json_data = json.loads(r.text)
# # print(json_data)
# #
# # for title in json_data:
# #     print(title)
#
# # print(len(json_data))
# Children = json_data["data"]["children"]
# new_list = []
# for post in Children:
#     new_list.append(post["data"]["title"])
#
# print(repr(new_list))



def reddit(topic):
    r = requests.get("http://www.reddit.com/r/{0}.json".format(topic), headers={'user-agent': 'Chrome'})
    json_data = json.loads(r.text)
    children = json_data["data"]["children"]
    for post in children:
        yield post["data"]["title"]

python = reddit("python")
for title in python:
    print(title)
