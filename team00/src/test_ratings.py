import ratings, pytest, os

class Test_Ratings:
    #----------Ratings----------#

    def create_csv(self):
        r_data = "userId,movieId,rating,timestamp\n" \
            "1,1,4.0,964982703\n" \
            "1,3,4.0,964981247\n" \
            "1,3,4.0,964981247\n" \
            "1,6,4.0,964982224\n" \
            "1,6,4.0,964982224\n" \
            "1,6,4.0,964982224\n" \
            "2,47,5.0,964983815\n" \
            "2,1,4.0,964982703\n" \
            "3,3,4.0,964981247\n" \
            "3,3,4.0,964981247\n" \
            "3,6,4.0,964982224\n" \
            "7,6,4.0,964982224\n" \
            "18,6,4.0,964982224\n" \
            "18,47,5.0,964983815" 
        m_data = "movieId,title,genres\n" \
            "1,Toy Story (1995),Adventure|Animation|Children|Comedy|Fantasy\n" \
            "3,Grumpier Old Men (1995),Comedy|Romance\n" \
            "6,Heat (1995),Action|Crime|Thriller\n" \
            "47,Seven (a.k.a. Se7en) (1995),Mystery|Thriller"
        
        rp = "ratings.csv"
        mp = "movies.csv"
        n = 14
        with open(rp, "w") as f:
            print(r_data, file=f)
        with open(mp, "w") as f:
            print(m_data, file=f)
        return [rp, mp, n]
    
    #----------Ratings----------#

    @pytest.mark.parametrize("f", [
        "ratings.txt", "_"
    ])
    def test_ratings_incorrect_init(self, f):
        rp, mp, n = self.create_csv()
        data = ratings.Ratings(f, n)
        assert data.ratings == []

    #----------Movies----------#

    @pytest.mark.parametrize("r, m", [
        ["ratings.txt", "_"],
        ["ratings.cv", "_"],
        ["_", "movies.txt"]
    ])
    def test_ratings_incorrect_init(self, r, m):
        rp, mp, n = self.create_csv()
        data = ratings.Ratings.Movies(r, m, n)
        assert data.ratings == []
        assert data.movies == {}

    @pytest.mark.parametrize("n", [
        -1, 0, 1, 999
    ])
    def test_movies_dist_by_year(self, n):
        rp, mp, count = self.create_csv()
        count = ratings.Ratings.Movies(rp, mp, count).dist_by_year(n)
        os.remove(rp)
        os.remove(mp)
        isinstance(count, dict)
        for x, y in count.items():
            assert isinstance(x, int)
            assert isinstance(y, int)
        assert list(count.keys()) == sorted(count.keys())

    @pytest.mark.parametrize("n", [
        -1, 0, 1, 999
    ])
    def test_movies_dist_by_ratings(self, n):
        rp, mp, count = self.create_csv()
        count = ratings.Ratings.Movies(rp, mp, count).dist_by_rating(n)
        os.remove(rp)
        os.remove(mp)
        isinstance(count, dict)
        for x, y in count.items():
            assert isinstance(x, float)
            assert isinstance(y, int)
        assert list(count.keys()) == sorted(count.keys())

    @pytest.mark.parametrize("n", [
        -1, 0, 1, 999
    ])
    def test_movies_top_by_num_of_ratings(self, n):
        rp, mp, count = self.create_csv()
        count = ratings.Ratings.Movies(rp, mp, count).top_by_num_of_ratings(n)
        os.remove(rp)
        os.remove(mp)
        if n in [-1, 0]:
            assert count == {}
            return
        
        isinstance(count, dict)
        for x, y in count.items():
            assert isinstance(x, str)
            assert isinstance(y, int)
        assert list(count.items()) == sorted(count.items(), key = lambda item: item[1], reverse=True)

    @pytest.mark.parametrize("n, func", [
        (-1, ratings.Math.average),
        (0, ratings.Math.median),
        (1, ratings.Math.median),
        (999, ratings.Math.average),
    ])
    def test_movies_top_by_ratings(self, n, func):
        rp, mp, count = self.create_csv()
        count = ratings.Ratings.Movies(rp, mp, count).top_by_ratings(n, func)
        os.remove(rp)
        os.remove(mp)
        if n in [-1, 0]:
            assert count == {}
            return
        
        isinstance(count, dict)
        for x, y in count.items():
            assert isinstance(x, str)
            assert isinstance(y, float)
        assert list(count.items()) == sorted(count.items(), key = lambda item: item[1], reverse=True)

    @pytest.mark.parametrize("n", [
        -1, 0, 1, 999
    ])
    def test_movies_top_controversial(self, n):
        rp, mp, count = self.create_csv()
        count = ratings.Ratings.Movies(rp, mp, count).top_controversial(n)
        os.remove(rp)
        os.remove(mp)
        if n in [-1, 0]:
            assert count == {}
            return
        
        isinstance(count, dict)
        for x, y in count.items():
            assert isinstance(x, str)
            assert isinstance(y, float)
        assert list(count.items()) == sorted(count.items(), key = lambda item: item[1], reverse=True)

    @pytest.mark.parametrize("n", [
        -1, 0, 1, 999
    ])
    def test_movies_top_range(self, n):
        rp, mp, count = self.create_csv()
        top_range = ratings.Ratings.Movies(rp, mp, count).top_range(n)
        os.remove(rp)
        os.remove(mp)
        if n in [-1, 0]:
            assert top_range == {}
            return
        
        isinstance(top_range, dict)
        for x, y in top_range.items():
            isinstance(x, str)
            isinstance(y, float)
        
        assert list(top_range.items()) == sorted(top_range.items(), key = lambda item: item[1])
    
    #----------Users----------#
    @pytest.mark.parametrize("n", [
        -1, 0, 1, 999
    ])
    def test_users_dist_by_year(self, n):
        rp, mp, count = self.create_csv()
        count = ratings.Ratings.Users(rp, mp, count).dist_by_year(n)
        os.remove(rp)
        os.remove(mp)
        isinstance(count, dict)
        for x, y in count.items():
            assert isinstance(x, int)
            assert isinstance(y, int)
        assert list(count.keys()) == sorted(count.keys())

    @pytest.mark.parametrize("n", [
        -1, 0, 1, 999
    ])
    def test_users_dist_by_ratings(self, n):
        rp, mp, count = self.create_csv()
        count = ratings.Ratings.Users(rp, mp, count).dist_by_rating(n)
        os.remove(rp)
        os.remove(mp)
        isinstance(count, dict)
        for x, y in count.items():
            assert isinstance(x, float)
            assert isinstance(y, int)
        assert list(count.keys()) == sorted(count.keys())

    @pytest.mark.parametrize("n", [
        -1, 0, 1, 999
    ])
    def test_users_top_by_num_of_ratings(self, n):
        rp, mp, count = self.create_csv()
        count = ratings.Ratings.Users(rp, mp, count).top_by_num_of_ratings(n)
        os.remove(rp)
        os.remove(mp)
        isinstance(count, dict)
        for x, y in count.items():
            assert isinstance(x, int)
            assert isinstance(y, int)
        assert list(count.items()) == sorted(count.items(), key = lambda item: item[1], reverse=True)

    @pytest.mark.parametrize("n, func", [
        (-1, ratings.Math.average),
        (0, ratings.Math.median),
        (1, ratings.Math.median),
        (999, ratings.Math.average),
    ])
    def test_users_top_by_ratings(self, n, func):
        rp, mp, count = self.create_csv()
        count = ratings.Ratings.Users(rp, mp, count).top_by_ratings(n, func)
        os.remove(rp)
        os.remove(mp)
        if n in [-1, 0]:
            assert count == {}
            return
        
        isinstance(count, dict)
        for x, y in count.items():
            assert isinstance(x, int)
            assert isinstance(y, float)
        assert list(count.items()) == sorted(count.items(), key = lambda item: item[1], reverse=True)

    @pytest.mark.parametrize("n", [
        -1, 0, 1, 999
    ])
    def test_users_top_controversial(self, n):
        rp, mp, count = self.create_csv()
        count = ratings.Ratings.Users(rp, mp, count).top_controversial(n)
        os.remove(rp)
        os.remove(mp)
        if n in [-1, 0]:
            assert count == {}
            return
        
        isinstance(count, dict)
        for x, y in count.items():
            assert isinstance(x, int)
            assert isinstance(y, float)
        assert list(count.items()) == sorted(count.items(), key = lambda item: item[1], reverse=True)



    