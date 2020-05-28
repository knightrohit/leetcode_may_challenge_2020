from collections import defaultdict

def test(N, dislikes):
        if not N:
            return False
        
        if N <= 2:
            return True
        
        while dislikes:
            g1, g2 = set(), set()
            park = []
            for i, j in dislikes:            
                if (i in g1 and j in g1) or (i in g2 and j in g2):
                    return False
                
                if i in g1 and j in g2:
                    pass
                
                elif i in g2 and j in g1:
                    pass
                
                elif j in g1:
                    g2.add(i)
                
                elif j in g2:
                    g1.add(i)

                elif i in g1:
                    g2.add(j)                
                
                elif i in g2:
                    g1.add(j)
                
                elif not g1 and not g2:
                    g1.add(i)
                    g2.add(j)
                
                else:
                    park.append([i, j])

                dislikes = park

        return True