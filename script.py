import requests
from datetime import datetime

# Configurações
repo_owner = 'Pablios'
repo_name = 'Pablios'
year = 2024
api_url = f'https://api.github.com/repos/{repo_owner}/{repo_name}/commits'
token = 'ACTIONS_PAT'  # Substitua pelo seu token de acesso pessoal

# Função para obter commits da API
def get_commits():
    headers = {
        'Authorization': f'token {token}'
    }
    commits = []
    page = 1
    while True:
        response = requests.get(api_url, headers=headers, params={'page': page, 'per_page': 100})
        response.raise_for_status()
        data = response.json()
        if not data:
            break
        commits.extend(data)
        page += 1
    return commits

# Filtrar commits por ano
def filter_commits(commits):
    return [commit for commit in commits if datetime.strptime(commit['commit']['committer']['date'], "%Y-%m-%dT%H:%M:%SZ").year == year]

# Gerar o SVG
def generate_svg(filtered_commits):
    width = 800
    height = 600
    cell_size = 10
    columns = width // cell_size
    rows = height // cell_size
    grid = [[0] * columns for _ in range(rows)]

    # Simular a geração do SVG (exemplo básico)
    with open('contribution-grid.svg', 'w') as f:
        f.write(f'<svg width="{width}" height="{height}" xmlns="http://www.w3.org/2000/svg">')
        for i, commit in enumerate(filtered_commits):
            x = (i % columns) * cell_size
            y = (i // columns) * cell_size
            f.write(f'<rect x="{x}" y="{y}" width="{cell_size}" height="{cell_size}" fill="green"/>')
        f.write('</svg>')

def main():
    commits = get_commits()
    filtered_commits = filter_commits(commits)
    generate_svg(filtered_commits)

if __name__ == '__main__':
    main()
