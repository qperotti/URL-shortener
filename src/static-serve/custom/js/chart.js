$(function () {


    var id = $('#id').text()
    console.log(id)
    var shortUrl = $('#short-url').text()

    chartConfig = {
        chart: {
            type: 'column'
        },
        title: {
            text: 'Average Clicks'
        },
        subtitle: {
            text: '(Number of times used during last two week)'
        },
        xAxis: {
            categories: [],
            crosshair: true
        },
        yAxis: {
            min: 0,
            title: {
                text: 'Number of clickss'
            }
        },
        tooltip: {
            headerFormat: '<span style="font-size:10px">{point.key}</span><table>',
            pointFormat: '<tr><td style="color:{series.color};padding:0"># clicks: </td>' +
                '<td style="padding:0"><b>{point.y}</b></td></tr>',
            footerFormat: '</table>',
            shared: true,
            useHTML: true
        },
        plotOptions: {
            column: {
                pointPadding: 0.2,
                borderWidth: 0
            }
        },
        series: [{
            name: '',
            color: '#3076B3',
            data: []

        }]
    }

    $.ajax({
        url: "/api/analytics/" + id + "/",
        method: "GET",
        success: function(data){
            
            chartConfig.xAxis.categories = data.chart_dates;
            chartConfig.series[0].data = data.clicks_average;
            chartConfig.series[0].name = shortUrl

            Highcharts.chart('container', chartConfig );
        },
        error: function(data){
            console.log("error")
            console.log(data)
        }
    })



    
});