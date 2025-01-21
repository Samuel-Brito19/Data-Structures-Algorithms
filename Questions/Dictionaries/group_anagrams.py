def groupAnagram(self, array):
    g1,g2 = {},[]
    for a in range(array):
        if(g1[a] == g2[a]):
            g2.append(g1[a])
        else:
            return
        