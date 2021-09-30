import re


def get_objects_parameters(query, pattern="&|;", key_split="="):
    object_search = {}
    for el in re.split(pattern, query):
        key, value = el.split(key_split)
        object_search.update({key: value.replace("+", " ")})
    return object_search

if __name__ == "__main__":
    google_url = "q=Cat+and+dog&rlz=1C1GCEA_enUA926UA926&oq=Cat+and+dog&aqs=chrome..69i57.1332j0j15&sourceid=chrome&ie=UTF-8"
    rozetka_url = "kolichestvo-osnovnih-kamer=3630921;producer=xiaomi;23777=6-6-5;38435=677049"
    print(get_objects_parameters(google_url))
    print(get_objects_parameters(rozetka_url))
