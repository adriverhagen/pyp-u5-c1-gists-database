import requests
import sqlite3

def import_gists_to_database(db, username, commit=True):
    query = "SELECT github_id, html_url, git_pull_url, git_push_url, commits_url, forks_url, public, created_at, updated_at, comments, comments_url FROM gists WHERE github_id = :github_id"
    url= 'https://api.github.com/users/{username}/gists'
    
    #get gist from user
    r = requests.get(url.format(username))
    
    #raise error if data is not receive
    r.raise_for_status()
    
    #convert all gist to json
    gists = r.json()
    
    for gist in gists:
        params = {'github_id': gist['id'],
               'html_url': gist['html_url'],
               'git_pull_url': gist['git_pull_url'],
               'git_push_url': gist['git_push_url'],
               'commits_url': gist['commits_url'],
               'forks_url': gist['forks_url'],
               'public': gist['public'],
               'created_at': gist['created_at'],
               'updated_at': gist['updated_at'],
               'comments': gist['comments'],
               'comments_url': gist['comments_url']}
        
        db.execute(query, params)
        
        if commit:
            db.commit()
