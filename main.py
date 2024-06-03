import requests

def bestInGenre(movies):
  genre = 'Action'
  bestMovie = None
  newRating = -1
  for movie in movies:    
      for detailMovie in movie:
          if genre in detailMovie['genre']:              
              nameMovie = detailMovie['name']
              rating = detailMovie['imdb_rating']
              if (rating > newRating) or (rating == newRating and nameMovie <  bestMovie['name']):
                  bestMovie = detailMovie
                  newRating = rating
  print(bestMovie['name'])  


def getAllMovies(page, totalPages):
  pages = totalPages
  movies = []
  while page <= pages:
    urlByPage = f'https://jsonmock.hackerrank.com/api/tvseries?page={page}'
    response = requests.get(urlByPage)
    moviesList = response.json()
    movies.append(moviesList['data'])
    page += 1
  return bestInGenre(movies)


def getInfoApi():
  url = 'https://jsonmock.hackerrank.com/api/tvseries'
  response = requests.get(url)
  data = response.json()
  page = data['page']
  totalPages = data['total_pages']
  return getAllMovies(page, totalPages)


if __name__ == '__main__':
  getInfoApi()