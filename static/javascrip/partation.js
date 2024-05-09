var partation = echarts.init(document.getElementById("r1"),"vintage");
var option_r1 = {
    backgroundColor:"",
    tooltip: {
        trigger: 'item',
        formatter: '{a} <br/>{b}: {c} ({d}%)'
    },
    legend: {
        orient: 'vertical',
        left: 7,
        data: ['亚洲', '欧洲', '非洲', '美洲', '大洋洲'],
        textStyle:{

            color:"#fdfcfc"
        },
    },
    series: [
        {
            name: '人口占比',
            type: 'pie',
            radius: ['50%', '70%'],
            avoidLabelOverlap: false,
            label: {
                show: false,
                position: 'center'
            },
            emphasis: {
                label: {
                    show: true,
                    fontSize: '30',
                    fontWeight: 'bold'
                }
            },
            labelLine: {
                show: false
            },
            data: [
                // {value: 335, name: '直接访问'},
                // {value: 310, name: '邮件营销'},
                // {value: 234, name: '联盟广告'},
                // {value: 135, name: '视频广告'},
                // {value: 1548, name: '搜索引擎'}
            ]
        }
    ]
};
partation.setOption(option_r1)
