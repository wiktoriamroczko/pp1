class matrix():

    @staticmethod
    def create(x,y):
        matrix = [[0 for a in range(x)]for b in range(y)]
        return matrix

    @staticmethod
    def create_unit(x):
        z = matrix.create(x,x)
        pom = 0
        for i in z:
            i[pom] = 1
            pom+=1
        return z

    @staticmethod
    def fill_random(matrix,m,n):
        import random
        for i in matrix:
            for j in range(len(i)):
                i[j] = random.randint(m,n)
   
    @staticmethod           
    def transponse(matrix):
            return [[matrix[j][i] for j in range (len(matrix))]for i in range(len(matrix[0]))]

    @staticmethod      
    def create_diagonal(x,m,n):
        import random
        z = matrix.create(x,x)
        pom = 0
        for i in z:
            x = random.randint(m,n)
            i[pom] = x
            pom+=1
        return z
            
    @staticmethod
    def print(matrix):
        for row in matrix:
            print(row)
            
m = matrix.create(3,4)
matrix.print(m)
x = matrix.transponse(m)
matrix.print(x)
n = matrix.create_unit(5)
matrix.print(n)
b = matrix.create_diagonal(4,10,20)
matrix.print(b)