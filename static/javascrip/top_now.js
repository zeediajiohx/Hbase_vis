var top_now = echarts.init(document.getElementById("l2"),"dark");

option_right1 = {
	backgroundColor:'',
	title: {
		text: '2019年人口TOP5国家',
		textStyle: {
			color: 'white'
		},
		left: 'left'
	},

	color: ['#3398DB'],
	tooltip: {
		trigger: 'axis',
		axisPointer: {
			type: 'shadow'
		}
	},
	xAxis: {
		type: 'category',
		// scale:true,
		data: []
	},
	yAxis: {
		type: 'value',
		axisLabel: {
				show: true,
				color: 'white',
				fontSize: 12,
				formatter: function(value) {
					if (value >= 100000000) {
						value = value / 100000000 + '亿';
					}
					return value;
				}
			},
		//坐标轴刻度设置
		},
	grid: {
      		top: 50, // 等价于 y: '16%'
      		left: '4%',
      		right: '6%',
      		bottom: '4%',
      		containLabel: true
      	},

	series: [{
		type: 'bar',
		data: [],
		barMaxWidth: "50%",
		itemStyle:{color:new echarts.graphic.LinearGradient(0,0,0,1,[{offset:0,color:"#83bff6"},{offset:0.5,color:"#188df0"},{offset:1,color:"#188df0"}])}
	}]
};
top_now.setOption(option_right1)
// ,tooltip:{trigger:"axis",axisPointer:{type:"shadow"}},xAxis:{type:"category",data:[]},yAxis:{type:"value"},series:[{data:[],type:"bar",barMaxWidth:"50%",itemStyle:{color:new echarts.graphic.LinearGradient(0,0,0,1,[{offset:0,color:"#83bff6"},{offset:0.5,color:"#188df0"},{offset:1,color:"#188df0"}])},}]};top_now.setOption(ec_right1_option);
