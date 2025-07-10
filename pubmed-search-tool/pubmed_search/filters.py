def is_non_academic(author_affiliation):
    if not author_affiliation:
        return False
    keywords = ["inc", "ltd", "gmbh", "pvt", "llc", "corporation", "solutions"]
    return any(keyword in author_affiliation.lower() for keyword in keywords)
