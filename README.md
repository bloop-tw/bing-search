# Bing Search
This is an unofficial Bing Search API for Python. Note that this is still in active development, and pull requests are welcomed!

## Usage
To search:
```py
from bing_search import bing_search
print(bing_search("chocolate"))
```
```jsonc
{
  "url": "https://www.bing.com/search?q=chocolate&setlang=en&count=20&form=QBRE",
  "results": [
    {
      "url": "https://www.lindtusa.com/",
      "title": "Gourmet Chocolate by Lindt for Every Occasion | Lindt \u2026",
      "caption": "\u00a0\u00b7 <strong>Chocolate</strong> comes from cacao, a plant with high levels of minerals and antioxidants. Commercial milk <strong>chocolate</strong> contains cocoa butter, sugar, milk, and small \u2026"
    },
    {
      "url": "https://www.healthline.com/nutrition/dark-chocolate-buyers-guide",
      "title": "Best Dark Chocolate: The Ultimate Buyer's Guide - Healthline",
      "caption": "\u00a0\u00b7 Read this guide to find the best types of dark <strong>chocolate</strong> to buy, as well as which to avoid. There are hundreds of different types of dark <strong>chocolate</strong>. Health Conditions"
    },
    {
      "url": "https://www.foodnetwork.com/topics/chocolate-cookie",
      "title": "Chocolate Cookie Recipes : Food Network | Food Network",
      "caption": "\u00a0\u00b7 <strong>Chocolate</strong> Cookie Recipes. What could possibly make a cookie better than the addition of <strong>chocolate</strong>? Bake up any of these <strong>chocolate</strong> cookie recipes for a delicious sweet \u2026"
    },
    // ...
  ]
}
```

If you prefer to use `pydantic` models:
```py
from bing_search import bing_search, Results
result = Results(**bing_search)

# you can get intelligence autocomplete
result.url
result.results[0].title
# ...
```

## Observation & Plans
1. UserAgent: For the prototype of this project, I've tried to directly use `request.get` to fetch results. However, some results were blocked and it seemed like Bing had a "User-Agent" detection. So, in this project, I used [`fake-useragent`](https://pypi.org/project/fake-useragent) to implement content fetching.
2. Regex: Both beautiful soup and Python built-in regex library are slow. Therefore, I used [rure-python](https://github.com/davidblewett/rure-python) to make the process faster.
3. Autocomplete Support: In the future, this project might also include the Bing autocomplete feature.
4. **The Current Problem: The current problem is that I cannot really understand how the parameters work for [bing.com/search](https://bing.com/search), as there are many variations and I cannot really ensure which leads to which kind of search result page. [I really need help with this one](https://github.com/bloop-tw/bing-search/issues/new).**

## Contributors
Thanks to myself... :(
