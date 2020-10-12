import os

from google.cloud import bigquery

path = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(
    path, "sample_dashboard", "google_analytics",
    "data", "google_analytics_data.csv"
)
csv_path = os.path.join(
    path, "sample_dashboard", "google_analytics",
    "data", "google_analytics_data.csv"
)
json_path = os.path.join(path, "key", "big-query-284408-e895d0eb5b23.json")


if os.path.isfile(csv_path):
    print("Google data already downloaded")
else:
    print("Downloading google data")
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = json_path

    client = bigquery.Client()  # Start the BigQuery Client
    # Input your Query Syntax here; You may try it first at
    # https://console.cloud.google.com/bigquery
    sql = """SELECT trafficSource.source, trafficSource.campaign, 
    trafficSource.keyword, trafficSource.adContent, device.browser,
    device.operatingSystem, device.isMobile, device.mobileDeviceModel, 
    geoNetwork.continent,  sum(totals.visits) as visitors
    FROM `bigquery-public-data.google_analytics_sample.*`
    group by source, trafficSource.campaign, trafficSource.keyword, 
    trafficSource.adContent,  device.browser, device.operatingSystem, 
    device.isMobile, device.mobileDeviceModel, geoNetwork.continent,
    totals.visits
    ORDER BY visitors desc
    LIMIT 2000"""
    df = client.query(sql).to_dataframe()
    df.head()
    df.to_csv(csv_path, index=False, header=True)
