class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        in_degree = [0] * numCourses
        cours_suivants = [[] for _ in range(numCourses)]
        coursFait = []

        for cours, prerequis in prerequisites:
            in_degree[cours] += 1 
            cours_suivants[prerequis].append(cours)

        for cours in range(numCourses): 
            if in_degree[cours] == 0: 
                coursFait.append(cours)

        cours_valides = 0 
        
        while len(coursFait) > 0:
            current_cours = coursFait.pop(0)
            cours_valides += 1
            
            for suivant in cours_suivants[current_cours]:
                in_degree[suivant] -= 1 
                if in_degree[suivant] == 0: 
                    coursFait.append(suivant)

        if cours_valides == numCourses:
            return True 

        return False 


