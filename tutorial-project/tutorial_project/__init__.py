from dagster import (
    AssetSelection,
    Definitions,
    ScheduleDefinition,
    define_asset_job,
    # load_assets_from_modules,
    FilesystemIOManager,  # Update the imports at the top of the file to also include this
)

from dagster_duckdb_pandas import DuckDBPandasIOManager

# from . import assets
# from .assets import concept, hacker_news
# all_assets = [*concept, *hacker_news]

from assets import concept_assets, hacker_news_assets
all_assets = [*concept_assets, *hacker_news_assets]


# Define a job that will materialize the assets
hackernews_job = define_asset_job("hackernews_job", selection=AssetSelection.all())

hackernews_schedule = ScheduleDefinition(
    job=hackernews_job, cron_schedule="0 * * * *"  # every hour
)

io_manager = FilesystemIOManager(
    base_dir="data",  # Path is built relative to where `dagster dev` is run
)

database_io_manager = DuckDBPandasIOManager(database="analytics.hackernews")

defs = Definitions(
    assets=all_assets,
    schedules=[hackernews_schedule],
    resources={
        "io_manager": io_manager,
        "database_io_manager": database_io_manager,  # Define the I/O manager here
    },
)



# if __name__ == "__main__":
#     pprint(
#         dir(assets_concept)
#         )

# EXAMPLE of ROOT __init__ ###########################################################################
# import os

# from dagster import Definitions

# from .assets import activity_analytics_assets, core_assets, dbt_assets, recommender_assets
# from .jobs import activity_analytics_assets_sensor, core_assets_schedule, recommender_assets_sensor
# from .resources import RESOURCES_LOCAL, RESOURCES_PROD, RESOURCES_STAGING
# from .sensors import make_slack_on_failure_sensor

# all_assets = [*core_assets, *recommender_assets, *dbt_assets, *activity_analytics_assets]

# resources_by_deployment_name = {
#     "prod": RESOURCES_PROD,
#     "staging": RESOURCES_STAGING,
#     "local": RESOURCES_LOCAL,
# }

# deployment_name = os.environ.get("DAGSTER_DEPLOYMENT", "local")

# all_sensors = [activity_analytics_assets_sensor, recommender_assets_sensor]
# if deployment_name in ["prod", "staging"]:
#     all_sensors.append(make_slack_on_failure_sensor(base_url="my_dagit_url"))

# defs = Definitions(
#     assets=all_assets,
#     resources=resources_by_deployment_name[deployment_name],
#     schedules=[core_assets_schedule],
#     sensors=all_sensors,
# )