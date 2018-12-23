import requests
import pygal
from pygal.style import LightColorizedStyle as LSC, LightenStyle as LS

# Make an API call and store the responce.
url = "https://api.github.com/search/repositories?q=language:python&sorted=stars"
r = requests.get(url)
print("Status code: ", r.status_code)

# Store API response in a var.
response_dict = r.json()
print("Total resos:", response_dict['total_count'])

# Explore information about the repositories.
repo_dicts = response_dict['items']

names, plot_dicts = [], []
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])
    
    plot_dict = {
        'value' : repo_dict['stargazers_count'],
        'lanel' : repo_dict['description'],
        'xlink' : repo_dict['html_url']
    }
    plot_dicts.append(plot_dict)
    
# Make visualization.
my_style = LS('#333366', base_style=LSC)

my_config = pygal.Config()
my_config.x_label_rotation = 45
my_config.show_legend = False
my_config.title_font_size = 24
my_config.label_font_size = 14
my_config.major_label_font_size = 18
my_config.truncate_label = 15 # short the long names to 15 characters
my_config.show_y_guides = False # hide the horizontal lines
my_config.width = 1000

chart = pygal.Bar(my_config, style=my_style)
chart.title = 'Most-Starred Python Projects on GitHub'
chart.x_labels = names
chart.add('', plot_dicts) # we don't need this data series to be labelled, so we pass an empty string for that label.
chart.render_to_file('C:/Users/Maria/Documents/MyCodes/DataVisualization/Working with APIs/python_repos.svg')

# Examine the first respository.
repo_dict = repo_dicts[0]
print('\nKeys: ', len(repo_dict))
for key in sorted(repo_dict):
    print(key)