
function get_l1_data() {
	$.ajax({
		url:"/l1",
		success: function(data) {
			option_left1.xAxis.data = data.year
			option_left1.series[0].data = data.world
			option_left1.series[1].data = data.asia
			option_left1.series[2].data = data.europe
			option_left1.series[3].data = data.africa
			option_left1.series[4].data = data.amrica
			allyear.setOption(option_left1)
		},
		error: function(xhr, type, errorThrown) {

		}
	})
}

function get_c1_data() {
	$.ajax({
		url: "/c1",
		success: function(data) {
			$(".num h1").eq(0).html(data.world)
			$(".num h1").eq(1).html(data.china)
			console.log("c1hl")

		},
		error: function(xhr, type, errorThrown) {

		}
	})
}

function get_c2_data(){
    $.ajax({
        url:"/c2",
        // dataType: 'jsonp',  // 请求方式为jsonp
        success:function(data){
            console.log(data.data[1])
            ecc_world_option.series[0].data=data.data;
            maps.setOption(ecc_world_option)
        }
    })
}


function get_l2_data() {
	$.ajax({
		url:"/l2",
		success: function(data) {
			option_right1.xAxis.data = data.country
			console.log("city_r1"+data.country)
			option_right1.series[0].data = data.population
			top_now.setOption(option_right1)
		},
		error: function(xhr, type, errorThrown) {

		}
	})
}

function get_r1_data() {
	$.ajax({
		url:"/r1",
		success: function(data) {
			console.log(data)
			option_r1.series[0].data=data;
            partation.setOption(option_r1)
		},
		error: function(xhr, type, errorThrown) {

		}
	})
}

get_c1_data()
get_c2_data()
get_l1_data()
get_l2_data()
get_r1_data()
// setInterval(get_c1_data,1000);
// setInterval(get_c2_data,1000*10);
// setInterval(get_rw_data,1000*10);

