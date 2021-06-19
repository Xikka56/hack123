function resize_back(obj) {
    // obj.style = ''
    obj = document.getElementsByClassName('jobs_org')
    obj[0].remove();
    obj[0].style = 'display:block';

    // obj[0].remove();



}



async function filling_blocks() {
    count_el = document.getElementsByClassName('jobs_org').length
    console.log(count_el);
    if (count_el <= 5) {

        m_url = '/api/v0.1/get_block'
        data = {
            'count': 5
        }
        sender(m_url, data).then(data => {
            // console.log(data);

            for (el in data['mass_data']) {
                el = data['mass_data'][el]


                qwer = `
                    <div id='jobs_slide' style='display:none' class="jobs_org">
                        <div class="slide_box">
                            <div class="header_Text">
                                <h1 style="text-align: left;">${el['title']}</h1>
                            </div>
                            <div class="types_info">
                                <h3 style="text-align: left;">${el['type']}</h3>
                                <div>
                                    <h3 style="text-align: right;">${el['data']}</h3>
                                </div>
                            </div>
                        </div>
                        <div id='box_info' class="slide_box_info"></div>
                    </div>
                `
                document.getElementById('lister').innerHTML += qwer


            }


        });
    }
}

filling_blocks()
var tn = 0
$(function() {
    $("div").swipe({
        //Generic swipe handler for all directions
        swipe: function(event, direction, distance, duration, fingerCount, fingerData) {
            // $(this).text("You swiped " + direction);l\

            var pasivity = false
            for (el in event.path) {
                if (event.path[el].id == 'jobs_slide') {
                    pasivity = true
                    break
                }
            }
            if (pasivity) {
                console.log('Свайп там, logic');
                console.log(direction);
                if (direction == 'up') {
                    document.getElementById('box_info').classList.add('slide_box_info_active')
                }

                if (direction == 'down') {
                    document.getElementById('box_info').classList.remove('slide_box_info_active')
                }

                if (direction == 'left') {
                    document.getElementById('jobs_slide').style = 'transform: translateX(-100%) scale(0.5)'
                }
                if (direction == 'right') {
                    document.getElementById('jobs_slide').style = 'transform: translateX(100%) scale(0.5)'
                }

                if (direction == 'right' || direction == 'left') {
                    document.getElementById('box_info').classList.remove('slide_box_info_active')
                    if (parseInt(new Date().getTime() / 1000) > tn + 0.3) {
                        setTimeout(resize_back, 300, document.getElementById('jobs_slide'));
                        console.log('sqq');
                        tn = parseInt(new Date().getTime() / 1000)
                        filling_blocks()

                    }


                }


            }
        }
    });

    //Set some options later
    $("#test").swipe({ fingers: 2 });
});