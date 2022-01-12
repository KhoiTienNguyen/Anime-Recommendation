import pandas as pd
import numpy as np
from scipy.sparse import csr_matrix
import pickle
from sklearn.neighbors import NearestNeighbors
import argparse


def main():

    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group(required=True)
    # Optional knn model outputted
    group.add_argument('-o', '--output_model')
    # Optional knn model inputted
    group.add_argument('-i', '--input_model')
    # Anime csv converted from json to csv
    parser.add_argument('-a', '--anime_csv', required=True)
    # Users csv converted from json to csv
    parser.add_argument('-u', '--users_csv', required=True)
    args = parser.parse_args()

    print("Loading Data")
    knn = -1
    users = pd.read_csv(args.users_csv)
    anime = pd.read_csv(args.anime_csv)
    combined = pd.merge(users, anime, on="ID")
    user_ratings = combined.drop_duplicates(['user', 'title'])
    users_ratings_matrix = user_ratings.pivot(index='title', columns='user', values='score').fillna(0)

    if args.input_model == None:
        compressed_matrix = csr_matrix(users_ratings_matrix.values)
        knn = NearestNeighbors(algorithm='brute', metric='cosine')
        knn.fit(compressed_matrix)
        pickle.dump(knn, open(args.output_model,'wb'))
    else:
        knn = pickle.load(open(args.input_model, 'rb'))

    def get_recommendations(title, matrix=users_ratings_matrix, model=knn, topn=10):
        try:
            anime_index = list(matrix.index).index(title)
            distances, indices = model.kneighbors(matrix.iloc[anime_index,:].values.reshape(1,-1), n_neighbors=topn+1)
            print('Recommendations for {}:'.format(matrix.index[anime_index]))
            for i in range(1, len(distances.flatten())):
                print('{}. {}, distance = {}'.format(i, matrix.index[indices.flatten()[i]], "%.3f"%distances.flatten()[i]))
            print()
        except Exception as e:
            print("Invalid anime name: Please use exact name as MyAnimeList")

    print("Enter Anime Name:", end=" ")
    temp = input()
    while temp != "quit":
        get_recommendations(temp)
        print("Enter Anime Name:", end=" ")
        temp = input()

if __name__ == '__main__':
    main()