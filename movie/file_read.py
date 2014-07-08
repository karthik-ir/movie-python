'''
Created on 07-Jul-2014

@author: hasher
'''
movie_map = dict()
user_map = dict()
ratings_map = dict()
genre_map = dict()

def read_movie_file(file_name):
    f = open(file_name, 'r')
    data = dict();
    for line in f:
        words = line.split('|')
        
        data_map = dict()
        data_map.__setitem__('id', words[0])
        data_map.__setitem__('title', words[1])
        data_map.__setitem__('releaseDate', words[2])
        data_map.__setitem__('videoReleaseDate', words[3])
        data_map.__setitem__('url', words[4])
        data_map.__setitem__('avg_rating', 0.0)
        data_map.__setitem__('rating_ids', list())
        genre_list = words[5:]
        i = 0
        for genre in genre_list:
            if genre == '1':
                genre_temp = genre_map.get(str(i), list())
                genre_temp.append(words[0])
                genre_map.__setitem__(str(i), genre_temp)
            i = i + 1
        
        # data_map.__setitem__('genre', words[5:])
        data.__setitem__(words[0], data_map)
    return data
    

def read_user_file(file_name):
    f = open(file_name, 'r')
    data = dict();
    for line in f:
        words = line.split('|')
        data_map = dict()
        data_map.__setitem__('id', words[0])
        data_map.__setitem__('age', words[1])
        data_map.__setitem__('gender', words[2])
        data_map.__setitem__('occupation', words[3])
        data_map.__setitem__('zipcode', words[4])
        data_map.__setitem__('rating_ids', list())
        data.__setitem__(words[0], data_map)
    return data

def read_rating_file(file_name):
    f = open(file_name, 'r')
    data = dict();
    for line in f:
        words = line.split('\t')
        data_map = dict()
        idd = ratings_map.__len__() + 1
        data_map.__setitem__('id', idd)
        data_map.__setitem__('rating', words[2])
        data_map.__setitem__('time_stamp', words[3])
        user_map.get(words[0]).get('rating_ids').append(idd)
        movie_map.get(words[1]).get('rating_ids').append(idd)
        avg_rating = movie_map.get(words[1]).get('avg_rating')
        rating_number = movie_map.get(words[1]).get('rating_ids').__len__()
        avg_rate_temp = (avg_rating * (rating_number - 1) + float(words[2])) / rating_number
        movie_map.get(words[1])['avg_rating'] = avg_rate_temp
        ratings_map.__setitem__(idd, data_map)
    return data
     
def get_most_active_user():
    max_length = 0
    idd = ''
    for user in user_map.values():
        if len(user.get('rating_ids')) > max_length:
            max_length = user.get('rating_ids').__len__()
            idd = user.get('id')
    return user_map.get(idd)
            
def get_most_watched_movie():
    max_length = 0
    idd = ''
    for movie in movie_map.values():
        if len(movie.get('rating_ids')) > max_length:
            max_length = movie.get('rating_ids').__len__()
            idd = movie.get('id')
    return movie_map.get(idd)

def get_top_movie_by_genre(genre):
    movie_ids=genre_map.get(genre)
    filtered_list=list()
    for movie_id in movie_ids:
        filtered_list.append(movie_map.get(movie_id))
    max_length = 0
    idd = ''
    for movie in filtered_list:
        if len(movie.get('rating_ids')) > max_length:
            max_length = movie.get('rating_ids').__len__()
            idd = movie.get('id')
    return movie_map.get(idd)
      
movie_map = read_movie_file('/home/hasher/workspace/Movie/movie.data')
user_map = read_user_file('/home/hasher/workspace/Movie/user.data')
ratings_map = read_rating_file('/home/hasher/workspace/Movie/ratings.data')

movie = movie_map.get('304')
print movie
print get_most_active_user()
print get_most_watched_movie()
print get_top_movie_by_genre('9')



# print genre_map
