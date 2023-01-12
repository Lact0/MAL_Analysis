import csv, ast

def buildMap():
  edges = {}
  nodes = {}
  with open('profiles.csv', 'r') as profileFile:
    profileReader = csv.DictReader(profileFile)
    for user in profileReader:
      fav = ast.literal_eval(user['favorites_anime'])
      for i in range(len(fav) - 1):
        ids = [fav[i]]
        for j in range(i + 1, len(fav)):
          ids.append(fav[j])
          for k in range(2):
            if ids[k] not in nodes:
              nodes[ids[k]] = []
            if ids[(k + 1) % 2] not in nodes[ids[k]]:
              nodes[ids[k]].append(ids[(k + 1) % 2])
          key = ','.join(sorted(ids))
          if key not in edges:
            edges[key] = 0
          edges[key] += 1
  return (nodes, edges)
          
def loadAnime():
  idToAnime = {}
  animeToId = {}
  with open('animes.csv', 'r') as animeFile:
    animeReader = csv.DictReader(animeFile)
    for show in animeReader:
      id = show['uid']
      title = show['title']
      idToAnime[id] = title
      animeToId[title] = id
  return (idToAnime, animeToId)