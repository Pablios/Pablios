import os
import requests

def get_commits():
    repo_owner = 'Pablios'
    repo_name = 'Pablios'
    api_url = f'https://api.github.com/repos/{repo_owner}/{repo_name}/commits'
    
    # Obtém o token de autenticação do ambiente
    token = os.getenv('GITHUB_TOKEN')
    if token is None:
        raise EnvironmentError("GITHUB_TOKEN not found in environment variables.")
    
    headers = {'Authorization': f'token {token}'}
    response = requests.get(api_url, headers=headers, params={'page': 1, 'per_page': 100})
    
    # Verifica se a resposta é bem-sucedida
    response.raise_for_status()
    return response.json()

def main():
    commits = get_commits()
    print(f"Retrieved {len(commits)} commits.")
    # Adicione a lógica para gerar o SVG com base nos commits filtrados aqui

if __name__ == "__main__":
    main()
