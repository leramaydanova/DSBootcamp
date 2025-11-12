import datetime, re, os
from collections import Counter
from functools import reduce

class Math:

    def average(rate: list):
        if len(rate) == 0:
            return 0.0
        else:
            average = reduce(lambda x, y: x + y, rate) / len(rate)
            return average
        
    def median(rate: list):
        rate.sort()
        l = len(rate)
        halfL = int(l / 2)
        if l == 0:
            return 0.0
        elif l % 2:
            return (rate[halfL - 1] + rate[halfL]) / 2
        else:
            return rate[halfL]
        
    def variance(rate: list):
        l = len(rate)
        if l == 0:
            return 0.0
        else:
            avg = reduce(lambda x, y: x + y, rate) / l
            devsSq = [(n - avg)**2 for n in rate]
            return reduce(lambda x, y: x + y, devsSq) / l


class Ratings:
    """
    Analyzing data from ratings.csv
    """
    def __init__(self, path_to_the_file: str, n = 1000):
        self.ratings = self.get_ratings(path_to_the_file, n)

    def get_ratings(self, path, n):
        try:
            with open(path, "r") as f:
                next(f)
                data = [next(f) for _ in range(n)]
                data = list(map(lambda line: str(line).split(","), data))
            return data
        except:
            print("Incorrect filename")
            return []

    class Movies:    

        def __init__(self, ratings_path: str, movies_path: str, n = 1000):
            self.ratings = Ratings(ratings_path, n).ratings
            self.movies = self.get_movies(movies_path)

        def get_movies(self, path):
            try:
                movies = dict()
                with open(path, "r") as f:
                    next(f)
                    for line in f:
                        req_line = re.findall(r'(".+?"|[^,]+)', line)
                        movies[req_line[0]] = req_line[1].strip('"')
                return movies
            except:
                print("Incorrect filename")
                return {}

        def dist_by_year(self, n):
            """
            The method returns a dict where the keys are years and the values are counts. 
            Sort it by years ascendingly. You need to extract years from timestamps.
            """
            def get_year(timestamp: int):
                date = (datetime.datetime(1970, 1, 1) + datetime.timedelta(days = timestamp / 86400))
                return date.year
            
            years = list(map(lambda ts: get_year(int(ts[3])), self.ratings))
            years_count = Counter(years)
            years_sorted = sorted(years_count.items())[:n]
            ratings_by_year = {year : count for year, count in years_sorted}
            return ratings_by_year
        
        def dist_by_rating(self, n):
            """
            The method returns a dict where the keys are ratings and the values are counts.
         Sort it by ratings ascendingly.
            """
            ratings = [float(rate[2]) for rate in self.ratings]
            ratings_count = Counter(ratings)
            ratings_sorted = sorted(ratings_count.items())[:n]
            ratings_distribution = {rating : count for rating, count in ratings_sorted}
            return ratings_distribution
        
        def top_by_num_of_ratings(self, n):
            """
            The method returns top-n movies by the number of ratings. 
            It is a dict where the keys are movie titles and the values are numbers.
            Sort it by numbers descendingly.
            """
            if n <= 0:
                return {}
            
            movieId = [movieId[1] for movieId in self.ratings]
            movieId_count = Counter(movieId)
            sorted_count = sorted(movieId_count.items(), key=lambda item: item[1], reverse=True)[:n]
            top_movies = {self.movies[id]: count for id, count in sorted_count}
            return top_movies
        
        def top_by_ratings(self, n, metric=Math.average):
            """
            The method returns top-n movies by the average or median of the ratings.
            It is a dict where the keys are movie titles and the values are metric values.
            Sort it by metric descendingly.
            The values should be rounded to 2 decimals.
            """
            if n <= 0:
                return {}
            
            movieRate = {}
            for rate in self.ratings:
                if rate[1] not in movieRate:
                    movieRate[rate[1]] = []
                movieRate[rate[1]].append(float(rate[2]))

            movieMetric = {movie[0] : metric(movie[1]) for movie in movieRate.items()}
            movieMetric_sorted = sorted(movieMetric.items(), key = lambda item: item[1], reverse = True)[:n]
            top_movies = {self.movies[id] : round(metric, 2) for id, metric in movieMetric_sorted}
            return top_movies
        
        def top_controversial(self, n):
            """
            The method returns top-n movies by the variance of the ratings.
            It is a dict where the keys are movie titles and the values are the variances.
          Sort it by variance descendingly.
            The values should be rounded to 2 decimals.
            """
            if n <= 0:
                return {}
            
            movieRate = {}
            for rate in self.ratings:
                if rate[1] not in movieRate:
                    movieRate[rate[1]] = []
                movieRate[rate[1]].append(float(rate[2]))
            
            movieVariance = {id: Math.variance(rate) for id, rate in movieRate.items()}
            movieVariance_sorted = sorted(movieVariance.items(), key = lambda item: item[1], reverse = True)[:n]
            top_movies = {self.movies[id] : round(var, 2) for id, var in movieVariance_sorted}
            return top_movies
        
        def top_range(self, n):
            if n <= 0:
                return {}
            
            ratings = {}
            for line in self.ratings:
                id = line[1]
                rating = float(line[2])
                if id not in ratings:
                    ratings[id] = []
                ratings[id].append(rating)
            range = [(id, (max(r) - min(r))) for id, r in ratings.items()]
            range_sorted = sorted(range, key = lambda item: item[1])[:n]
            top_range = {self.movies[id] : value for id, value in range_sorted}
            return top_range
        
    class Users(Movies):
        """
        In this class, three methods should work. 
        The 1st returns the distribution of users by the number of ratings made by them.
        The 2nd returns the distribution of users by average or median ratings made by them.
        The 3rd returns top-n users with the biggest variance of their ratings.
     Inherit from the class Movies. Several methods are similar to the methods from it.
        """
        def top_by_num_of_ratings(self, n):
            if n <= 0:
                return {}
            
            userId = [int(line[0]) for line in self.ratings]
            userId_count = Counter(userId)
            userId_count_sorted = sorted(userId_count.items(), key = lambda item: item[1], reverse = True)[:n]
            top_users = {id : count for id, count in userId_count_sorted}
            return top_users

        
        def top_by_ratings(self, n, metric=Math.average):
            if n <= 0:
                return {}
            
            ratings = {}
            for line in self.ratings:
                id = int(line[0])
                rating = float(line[2])
                if id not in ratings:
                    ratings[id] = []
                ratings[id].append(rating)
            
            ratings_metric = [(id, metric(rating)) for id, rating in ratings.items()]
            ratings_metric_sorted = sorted(ratings_metric, key = lambda item: item[1], reverse = True)[:n]
            top_movies = {id : round(metric, 2) for id, metric in ratings_metric_sorted}
            return top_movies
        
        def top_controversial(self, n):
            if n <= 0:
                return {}
            
            ratings = {}
            for line in self.ratings:
                id = int(line[0])
                rating = float(line[2])
                if id not in ratings:
                    ratings[id] = []
                ratings[id].append(rating)
            ratings_variance = [(id, Math.variance(ratings)) for id, ratings in ratings.items()]
            ratings_variance_sorted = sorted(ratings_variance, key = lambda item: item[1], reverse = True)[:n]
            top_variance = {id : round(variance, 2) for id, variance in ratings_variance_sorted}
            return top_variance

# Ratings.Movies("ratings.csv").top_controversial(10)
# print(Ratings(sys.argv[1]))

