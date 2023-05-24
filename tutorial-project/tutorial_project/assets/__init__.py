from dagster import load_assets_from_package_module, load_assets_from_package_name
from pprint import pprint

# from . import concept, hacker_news
import concept, hacker_news

# concept_assets = load_assets_from_package_name(
#     package_name="concept",
#     group_name="assets_concept"
# )
hacker_news_assets = load_assets_from_package_name(
    package_name="hacker_news",
    group_name="hacker_news",
)

# hacker_news_assets = load_assets_from_package_name(
#     package_module=hacker_news,
#     group_name="hacker_news",
# )


# EXAMPLE of assets' folder (package) __init__ ##############################################
# __
#     assets
#         activity_analytics
#         core
#         recommender
#         __init__.py

#         __init__.py
# from . import activity_analytics, core, recommender
if __name__ == "__main__":
    pprint(dir(hacker_news))