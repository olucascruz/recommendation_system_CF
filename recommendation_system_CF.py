import pandas as pd
my_rating = {"11":{"67": 4,"6702": 8,"415":2,"40852": 10, "1250": 9}}

print(my_rating)

def manhattan(rating1, rating2):
    distance = 0
    for key in rating1:
        if key in rating2:
            distance += abs(rating1[key] - rating2[key])
    return distance


def computer_nearest_neighbor(user_rating, users):
    distances = []
    for user in users:
        distance = manhattan(users[user], user_rating)
        distances.append((distance, user))
    distances.sort()
    return distances

def recomended(user_rating, users):
    nearest = computer_nearest_neighbor(user_rating, users)[0][1]
    print(nearest)
    recommendations = []
    neighbor_ratings = users[nearest]
    for anime in neighbor_ratings:
        if anime not in user_rating:
            recommendations.append((anime, neighbor_ratings[anime]))
    
    return sorted(recommendations)



if __name__ == "__main__":
    df = pd.read_csv(r"dataset_anime\relation_rating.csv")
    valid = list(my_rating["11"].keys())
    for i in range(len(valid)):
        valid[i] = int(valid[i])
    lis = df.query("anime_id in @valid")
    obj = dict()
    for user, anime, rating in zip(lis["user_id"], lis["anime_id"], lis["rating"]):
        try: 
            obj[str(user)].update({str(anime):rating})
        except KeyError:
            obj[str(user)] = {str(anime):rating}

    print(obj)
    result = recomended(my_rating, obj)
    print(result)