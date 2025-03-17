tiangan_list = ['jia','yi','bing','ding','wu','ji','geng','xin','ren','gui']
dizhi_list = ['zi','chou','yin','mao','chen','si','wu','wei','shen','you','xu','hai']

N = int(input())
#00年是geng you
tiangan = tiangan_list[(N%10+6)%len(tiangan_list)]
dizhi = dizhi_list[(N%12+8)%len(dizhi_list)]

print(f'{tiangan}{dizhi}')