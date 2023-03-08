
$(document).ready(function () {
    var search_form = document.getElementById('resultx');
    const searchBTN = document.getElementById('perform-search');

    $("#current_location").click(function () {
        if ($(this).is(":checked")) {
            $("#geocode").removeAttr("disabled");
            $("#geocode").focus();
        } else {
            $("#geocode").attr("disabled", "disabled");
        }
    })




    // searchBTN.onclick = (e) => {
    //     search_form.innerHTML = 'loading.........'
    // //     // fetchResult();
    //   }


    //   async function performSearch() {
    //     console.log('sded');
    //     keyword = document.getElementById('keyword').value;
    //     distance = document.getElementById('geocode').value;
    //     language = document.getElementById('language').value;
    //     type_ = document.getElementById('result_type').value;
    //     current_location = document.getElementById('current_location').value;

    //     const data = await fetchResult(keyword, distance, language, type_, current_location)
        
    //     console.log(keyword, distance, language, type_, current_location, data)

    //     const city_tag = document.getElementById('city_tag');
    //     const keyword_tag = document.getElementById('keyword_tag');
        
    //     const city_data = "{{ data.city|safe }}"
    //     const keyword_data = "{{ data.keyword|safe }}"
    //     if (city_data) {
    //         city_tag.innerHTML = `<b>${city_data}</b>`

    //     }
    //     else{
    //         city_tag.innerHTML = 'n/a'
    //     }

    //     if (keyword_data) {
    //         keyword_tag.innerHTML = `<b>${keyword_data}</b>`

    //     }
    //     else{
    //         keyword_tag.innerHTML = 'n/a'
    //     }

    //     console.log(data, data.data);

    //     // const container = document.getElementById('accordion')
    //     // data.data.forEach((result, idx) => {
    //     //     const card = document.createElement('div')
    //     //     card.classList = 'card-body';

    //     //     const content = `
    //     //     <input class="form-check-input me-${idx}" type="checkbox" value="" aria-label="...">
    //     //     <div class="avatar">
    //     //         <img src=${result.dp_link}>
    //     //         <div class="relationship-count">
    //     //             <p class="text-center follower-following"><span id="friends_count"></span> | <span id="followers_count">${result.followers_count}</span></p>
    //     //             <p class="profile-age"> <i class="fa-solid fa-heart-pulse" style="color:green;"></i>${result.user_created_at} day${result.user_created_at} old</p>
    //     //         </div>
    //     //     </div>

    //     //     <div class="bubble-container">
    //     //         <div class="bubble">
    //     //         <div class="tweet_status">
    //     //             { if result.is_quote == True }
    //     //             <i style="color: white;" class="fa-solid fa-retweet"></i> 
    //     //             {% elif result.is_reply %}
    //     //                 <i style="color: white;" class="fa-solid fa-comment"></i> 
    //     //             {% else %}
    //     //                 <i style="color: white;" class="fa-brands fa-twitter"></i> 
    //     //             {% endif %}
    //     //                 <div class="icon-retweet"></div>
    //     //         </div>
    //     //         <h3>${result.name} <span><i class="fa-solid fa-${result.verified}" style="color:blue;"></i></span> @${result.screen_name} <span><i class="fa-solid fa-${result.contributors_enabled}"></i></span></h3>
    //     //             <p>${result.tweet}</p>

    //     //             <p> <i class="fa-solid fa-comment"></i> <span style="padding: 0 30px 0 3px">0</span><i class="fa-solid fa-heart"></i> <span style="padding: 0 30px 0 3px"><span id="fav_count"></span></span> <i class="fa-solid fa-retweet"></i> <span style="padding: 0 30px 0 3px">${result.retweet_count}</span></p>
                    
    //     //             <div class="d-flex bd-highlight">
    //     //                 <div class="p-2 flex-grow-1 bd-highlight">${result.tweet_created_at} <i class="fa-solid fa-clock"></i> ${result.tweet_created_at }</div>
    //     //                 <div class="p-2 bd-highlight"><i class="fa-solid fa-location-dot"></i> ${result.location }</div>
    //     //                 <div class="p-2 bd-highlight">
    //     //                     {% if 'apple' in result.source or 'android' in result.source %}
    //     //                     <span><i class="fa-brands fa-${result.source}"></i></span>
    //     //                     {% else  %}
    //     //                     <span><i class="fa-solid fa-${result.source}"></i></span>
    //     //                     {% endif %}
    //     //                 </div>
    //     //               </div>
    //     //             <div class="over-bubble">
    //     //                 <div class="icon-mail-reply action"></div>
    //     //                 <div class="icon-retweet action"></div>
    //     //                 <div class="icon-star"></div>
    //     //             </div>
    //     //         </div>
                
    //     //         <div class="arrow"></div>
    //     //         <div class="arrow-profile"></div>
    //     //     </div>
            
    //     //     `;
    //     // container.innerHTML += content;
    //     // });


        
    //   }

    //   
});