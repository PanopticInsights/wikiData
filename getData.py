import pandas as pd

url= "https://wikimedia.org/api/rest_v1/metrics/pageviews/per-article/"
enWiki = "en.wikipedia/"
access = "all-access/"
agents = "all-agents/"
article = "Startups/"
granularity = "daily/"
start = "20151010/"
end = "20151015"

tab = pd.read_csv(url + enWiki + access + agents + article + granularity + start + end)

print(tab)


