# django_dashboard

# Django web analytics menu
[![Django web analytics menu](https://github.com/Georgitanev/django_dashboard/blob/main/Big_Analytics.png)](https://github.com/Georgitanev/django_dashboard/blob/main/Big_Analytics.png)

# Django big chart - top 20 aquisition sources
[![Browser chart pie](https://github.com/Georgitanev/django_dashboard/blob/main/Big_Analytics_top_grapchics.png)](https://github.com/Georgitanev/django_dashboard/blob/main/Big_Analytics_top_grapchics.png)

# Browser pie - top 20 visitors brouwsers
[![Browser chart pie](https://github.com/Georgitanev/django_dashboard/blob/main/browser_pie.png)](https://github.com/Georgitanev/django_dashboard/blob/main/browser_pie.png)

# Brief report
[![Brief report](https://github.com/Georgitanev/django_dashboard/blob/main/Big_Analytics_brief_report.png)](https://github.com/Georgitanev/django_dashboard/blob/main/Big_Analytics_brief_report.png)


### Installation
Install the dependencies

Please install required modules with:
```sh 
pip -r requirements.txt
```

You need to put your json credentil key in folder 'key' with your 'your_filename.json'
And edit the name for 'key' in 'google_data.py'

You can download data from google analytics public dataset with this python script: [google_data.py](https://github.com/Georgitanev/django_dashboard/blob/main/google_data.py)
You can run the script with command:
```sh 
python google_data.py
```


It download data in folder 'data' (path) 'django_dashboard\sample_dashboard\google_analytics\data' in 'google_analytics_data.csv'

To run django web page use:
go to 'sample_dashboard' folder with command:
```sh 
cd sample_dashboard
```

and run with command:
```sh 
python manage.py runserver
```

If it working, it will print:
Starting development server at  [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

Click on the URL address to visit the webpage
