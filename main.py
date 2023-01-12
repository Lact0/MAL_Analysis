from functions import *
import json

print('Loading Anime...')
toAnime, toId = loadAnime()
print('Anime Loaded!')
print('')

AOT = 'Shingeki no Kyojin'
MHS = 'Mahouka Koukou no Rettousei'
BG = 'Seishun Buta Yarou wa Bunny Girl Senpai no Yume wo Minai'

print('Building Map...')
file = open('graph.txt', 'r')
nodes = json.loads(file.readline())
edges = json.loads(file.readline())
file.close()
graph = (nodes, edges)
print('Map has been created.')
print('')


def rec(animeName, nRecs = 5):
  if animeName not in toId:
    print('Anime Name not recognized.')
    return False
  id = toId[animeName]
  if id not in nodes:
    print('Anime invalid. It has not been favorited.')
    return False
  related = [[x, edges[','.join(sorted([str(id), str(x)]))]] for x in nodes[id]]
  related.sort(key = lambda x: -x[1])
  top = [x[0] for x in related[:nRecs]]
  print('Here are your recommendations for {show}!'.format(show=animeName))
  for i in range(len(top)):
    showId = top[i]
    print('{n}: {show}'.format(n=i+1, show=toAnime[showId]))
  return True

def store():
  with open('graph.txt', 'w') as file:
    file.write(json.dumps(nodes))
    file.write('\n')
    file.write(json.dumps(edges))