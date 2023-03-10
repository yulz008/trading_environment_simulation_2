// Initialize chart
// 

var chart_height = document.getElementById('chart').offsetHeight;
var chart_width =  document.getElementById('chart').offsetWidth;
console.log ('test');
console.log(chart_width);




var chart = LightweightCharts.createChart(document.getElementById('chart'), {
	priceScale: { autoScale: true},
	width: chart_width-10,
    height: chart_height-10,
	layout: {
		backgroundColor: '#FFFFFF', 
		textColor:'#000000' ,
	},
	grid: {
		vertLines: {
			color: 'rgba(255, 255, 255, 255)',
		},
		horzLines: {
			color: 'rgba(255, 255, 255, 255)',
		},
	},
	crosshair: {
		mode: LightweightCharts.CrosshairMode.Normal,
	},
	rightPriceScale: {
		borderColor: 'rgba(197, 203, 206, 0.8)',
	},
	timeScale: {
		borderColor: 'rgba(197, 203, 206, 0.8)',
		timeVisible: true,
		secondsVisible: false,
	},

	pane: 0
	
});

var candleSeries = chart.addCandlestickSeries({

  //red-green template	
  upColor: 'rgb(0, 163, 108)',
  downColor: 'rgb(255,0,0)',
  borderDownColor: 'rgb(255,0,0)',
  borderUpColor: 'rgb(0, 163, 108)',
  wickDownColor: 'rgb(255,0,0)',
  wickUpColor: 'rgb(0, 163, 108)',

   //black white template
   //upColor: 'rgb(255, 255, 255)',
   //downColor: 'rgb(0,0,0)',
   //borderDownColor: 'rgb(0,0,0)',
   //borderUpColor: 'rgb(0, 0, 0)',
   //wickDownColor: 'rgb(0,0,0)',
   //wickUpColor: 'rgb(0,0,0)',
  
  
});


var rsi_data;
var ma_20_data;
var ma_50_date;
var ma_100_data;



//var rsi_series = chart.addLineSeries({color: 'red', linewidth: 0.5 , pane: 1});
//RSI plots
var rsi_series = chart.addLineSeries({
	color: 'red',
	lineWidth: 1 ,
	pane: 1,
	priceLineVisible: false,
});
 

//upper RSI
var upper_rsi_limit = chart.addLineSeries({
	color: 'black',
	lineWidth: 1,
	lineStyle: 2,
	pane: 1,
	});
	upper_rsi_limit.setData([
		
		{ time: '2024-04-12', value: 70},
	
	]);


//lower RSI
var lower_rsi_limit = chart.addLineSeries({
	color: 'black',
	lineWidth: 1,
	lineStyle: 2,
	pane: 1,
	});
	lower_rsi_limit.setData([
		
		{ time: '2024-04-12', value: 30},
	
	]);



//20MA
var ma_20 = chart.addLineSeries({
	color: 'red',
	lineWidth: 0.5,
	lineStyle: 0,
	pane: 0,
	priceLineVisible: false,
	crosshairMarkerVisible: false,
	
	});

//50MA
var ma_50 = chart.addLineSeries({
	color: 'orange',
	lineWidth: 0.5,
	lineStyle: 0,
	pane: 0,
	priceLineVisible: false,
	crosshairMarkerVisible: false,
	});

//20MA
var ma_100 = chart.addLineSeries({
	color: 'blue',
	lineWidth: 0.5,
	lineStyle: 0,
	priceLineVisible: false,
	crosshairMarkerVisible: false,
	pane: 0,
	});



var base_url = 'http://'+ app_host + ':'+ app_port + '/history';
console.log(app_host);


var timeframe = document.getElementById('timeframe').value;
//alert(timeframe)


fetch(base_url,   {



	method: "POST",
	headers: {  "timeframe": timeframe }


  })
	
	
	

	.then((r) => r.json())
	.then((response) => {
          console.log(response);


		 // rsi_series.setData(response);

		  candleSeries.setData(response);
                  
		  document.getElementById("Output_box2").innerHTML = response[response.length -1].close;

	})

/* */

//var binancesocket = new WebSocket("wss://stream.binance.com:9443/ws/btcusdt@kline_15m");




binancesocket.onmessage =function(event) {
	var message = JSON.parse(event.data)

	var candlestick = message.k;
	

	candleSeries.update({
       
		time: candlestick.t / 1000,
		open: candlestick.o, 
		high: candlestick.h,
		low:  candlestick.l,
		close: candlestick.c

         

	})
}
