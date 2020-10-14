import os

import pandas as pd
from django.shortcuts import render

path = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(path, "data\\google_analytics_data.csv")


def index(request):
    """ view function for google_analytics app """
    df = pd.read_csv(csv_path)
    df["keyword"].fillna("no data", inplace=True)
    df["adContent"].fillna("no data", inplace=True)
    source_and_visitors = df.groupby("source")["visitors"].agg("sum")
    source_and_visitors = source_and_visitors[0:20]
    source_and_visitors_pie = df.groupby("browser")["visitors"].agg("sum")
    source_and_visitors_pie = source_and_visitors_pie[0:10]
    categories = list(source_and_visitors.index)
    values = list(source_and_visitors.values)
    data = []
    for index in range(0, len(source_and_visitors_pie.index)):
        value = {
            "name": source_and_visitors_pie.index[index],
            "y": source_and_visitors_pie.values[index],
        }
        data.append(value)
    table_content = df.to_html(index=None)
    table_content = table_content.replace("", "")
    table_content = table_content.replace(
        'class="dataframe"',
        "id='big_tables' class='table table-striped table-bordered'",
    )
    table_content = table_content.replace('border="1"', "")

    context = {
        "categories": categories,
        "values": values,
        "data": data,
        "table_data": table_content,
    }
    return render(request, "index.html", context=context)
