import csv
from SimilarityMatrix import SimilarityMatrix

DEBUG = True
INPUT_PATH1 = "Data/Elder Futhark.txt"
INPUT_PATH2 = "Data/Old Hungarian.txt"
def LoadData(path):
    letters = []
    matrix = []
    with open(path, 'r', encoding="utf-8") as csv_file:
        for line in csv_file:
            row = line.strip().split()
            letters.append(row[0])
            matrix.append(row[1:-1])
    return matrix, letters


if __name__ == "__main__":
    if DEBUG: print("**********************************")
    if DEBUG: print("*** START SIMILARITY MATRIX ***")
    if DEBUG: print("**********************************")
    if DEBUG: print()
    if DEBUG: print("Loading input from,", INPUT_PATH1)
    matrix1, letters1 = LoadData(INPUT_PATH1)
    if DEBUG: print("Loading input from,", INPUT_PATH2)
    matrix2, letters2 = LoadData(INPUT_PATH2)
    if DEBUG: print("***Generating the similarity matrix***")
    sm = SimilarityMatrix(matrix1, matrix2, letters1, letters2)
    sm.generate_similarity_matrix()
    if DEBUG: sm.print_similarity_matrix()
    #sm.draw_similarity_matrix()
    if DEBUG: print()
    if DEBUG: print("********************************")
    if DEBUG: print("*** END SIMILAIRTY MATRIX ***")
    if DEBUG: print("********************************")
    
