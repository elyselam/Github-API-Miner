import requests as req
import json

username = 'octocat'


def jsonify(url):
    ''''''  
    response = req.get(url) 
    json = response.json()
    return json

def gather_data(username):
    user_url = "https://api.github.com/users/{}".format(username)
    main_page = jsonify(user_url)
    total_repos = main_page['public_repos']
    followers = main_page['followers']


    repo_url = 'https://api.github.com/users/{}/repos'.format(username)
    repo = jsonify(repo_url)
   
    forks_sum, stars_sum = 0, 0

    for i, fork_star in enumerate(repo):
        forks_count = repo[i]["forks_count"]
        forks_sum = forks_sum + forks_count

        stars_count = repo[i]["stargazers_count"]
        stars_sum = stars_sum + stars_count


    github_dict = {
        "User": username,
        "Total Repos": total_repos,
        "Total Followers": followers,
        "Total Stars": stars_sum,
        "Total Forks": forks_sum
    }
    return github_dict

if __name__ == '__main__':
    user = input("What's your username? ")
    print(gather_data(user))

 