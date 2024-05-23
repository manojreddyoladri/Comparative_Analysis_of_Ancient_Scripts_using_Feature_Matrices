import numpy as np
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

class SimilarityMatrix:
    matrix1 = []
    matrix2 = []
    letters1 = []
    letters2 = []
    similarity_matrix = []

    def __init__(self, matrix1 , matrix2, letters1, letters2):
        self.matrix1 = matrix1
        self.matrix2 = matrix2
        self.letters1 = letters1
        self.letters2 = letters2

    def generate_similarity_matrix(self):
        for row1 in self.matrix1:
            sim_row = []
            for row2 in self.matrix2:
                similarity = sum(f1 == f2 for f1, f2 in zip(row1, row2))
                sim_row.append(similarity)
            self.similarity_matrix.append(sim_row)

    def print_similarity_matrix(self):
        print("  ",end="")
        for i in self.letters2:
            print(i, end="  ")
        print()
        for i in range(len(self.similarity_matrix)):
            print(self.letters1[i], end=" ")
            for val in self.similarity_matrix[i]:
                print(val, end=" ")
                if(val//10 == 0):
                    print(" ",end="")
            print()

    def draw_similarity_matrix(self):
        matrix = np.array(self.similarity_matrix)
        num_rows, num_cols = matrix.shape
        fig, ax = plt.subplots()
        ax.set_xticks(range(num_cols), labels=self.letters2)
        ax.set_yticks(range(num_rows), labels=self.letters1)
        ax.matshow(matrix)
        for i in range(num_cols):
            for j in range(num_rows):
                c = matrix[j, i]
                ax.text(i, j, str(c), va='center', ha='center')
        plt.show()
