def check_existence(name, collection):
  entry = collection.find_one({"entryName": name})
  if entry :
    return True
  else :
    return False