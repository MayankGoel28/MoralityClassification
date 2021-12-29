from pmaw import PushshiftAPI
import json

api = PushshiftAPI()
f = open("post_data.json", "r")
x = json.load(f)
post_ids = [item["id"] for item in x]
comment_ids = api.search_submission_comment_ids(ids=post_ids)
print("Length is", len(comment_ids))
with open("comment_ids.txt", "w") as f:
    for item in comment_ids:
        f.write("%s\n" % item)
