from github import Github
import pandas as pd

g = Github(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)

# Setup query parameters
query = 'language:python stars:>1000'

# Search repositories
result = g.search_repositories(query=query)

# Limit number of repositories
repos = []
for repo in result[:50]:  # fetch only 50 repos
    repos.append({
        'Name': repo.name,
        'Owner': repo.owner.login,
        'Stars': repo.stargazers_count,
        'Forks': repo.forks_count,
        'Watchers': repo.watchers_count,
        'Open Issues': repo.open_issues_count
    })

# Create DataFrame
df = pd.DataFrame(repos)

# Calculate some statistics
print("Average Stars:", df['Stars'].mean())
print("Average Forks:", df['Forks'].mean())
print("Total Repositories Mined:", len(df))

# Save data
df.to_csv('repository_data.csv', index=False)
print("Data saved to repository_data.csv")
