class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for i in range(len(asteroids)): 
            detruit = False
            while (stack and stack[-1] > 0 and asteroids[i] < 0):
                if abs(asteroids[i]) > stack[-1]:
                    stack.pop()
                elif abs(asteroids[i]) == stack[-1]: #les deux égaux
                    stack.pop()
                    detruit = True
                    break
                else: #l'astéroide perd
                    detruit = True
                    break #sortir de la boucle infine si asteroid perd 
            if not detruit: 
                stack.append(asteroids[i])
        return stack