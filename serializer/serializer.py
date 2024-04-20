'''
Serializes our data 
'''

def decode_data(blog) -> dict:
    return {
        "_id": str(blog["_id"]),
        "title": blog["title"],
        "sub_title": blog["sub_title"],
        "content": blog["content"],
        "author": blog["author"],
        "date": blog["date"]
    }


# storing the decoded data into a list
def decoded_data_list(blogs) -> list:
    return [ decode_data(blog) for blog in blogs ]