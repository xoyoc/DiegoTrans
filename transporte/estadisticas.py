from highcharts_core.chart import Chart
from highcharts_core.options.title import Title

datos = [
            [1,0.00], 
            [2,0.00], 
            [3,0.00], 
            [4,0.00], 
            [5,146180.08], 
            [6,0.00]
        ]

# Create a new Chart instance from the CSV file "my-csv-file.csv".
my_chart = Chart(data = datos, series_type='column')
my_chart.options.title = Title(text='Estadisticas de Transporte Diego')
# Download a PNG version of the chart in memory within your Python code.
my_png_image = my_chart.download_chart(format = 'png')
# Download a PNG version of the chart and save it the file "/images/my-chart-file.png"
my_png_image = my_chart.download_chart(
  format = 'png',
  filename = 'static/estadistica.png'
)