<style>

.logo_replacement {
      display: inline-grid;
}

.logo_replacement > span {
      color:black;
      font-weight: 800;
      margin-top: -10px;
}

.logo_replacement > span > svg {
      fill: #00dbce;
}
.dl-divider-violet{
      fill: #9194C3 !important;
}

.dl-section-violet {
     background-color: #9194C3 !important;
}

.text-violet {
     color: #9194C3 !important;
}

/* TOP MENU STYLING*/
#top-menu > li.current-menu-item > a, #top-menu > li.current-menu-item > a:hover {
      color: #9194C3;

}

#top-menu-nav > ul > li > a:before {
      background: #9194C3 !important;
}

#top-menu > li.cta-menu-item > a {
      background: rgba(255, 188, 7, 0.88);
      border: 2px rgba(255, 188, 7, 0.88) solid;
}

#top-menu > li.cta-menu-item > a:hover {
      color: rgba(255, 188, 7, 0.88);
}

.orange-button {
    background: rgba(255, 188, 7, 0.88) !important;
    border: 2px rgba(255, 188, 7, 0.88) solid !important;
}

.dl-cta-button::after .orange-button{
    color: rgba(255, 188, 7, 0.88) !important;
}

.dl-speaker:hover .et_pb_team_member_image:before{
    background: rgba(145, 148, 195, 0.7);

}

.et-social-nlpi a.icon:before{
      content:url(http://www.nlpkonferenca.si/wp-content/uploads/2017/04/nlpi-logo_a.png)
}

.et-social-icon a{
      width: 180px !important;
    height: 180px !important;
    line-height: 240px !important;
}

.initial-line-height{
      line-height: initial;
}

@media (min-width: 981px){

      #last-speaker_row > div.et_pb_column.et_pb_column_1_4.et_pb_column_12{
            margin-left: 10%
      }

      #logo {
          max-height: 78% !important;
      }
}

@media (min-width: 1330px){

      #logo {
          max-height: 78% !important;
      }
}

.et_pb_image_0 > img {
  height: 100% !important;
}


</style>



<script type="text/javascript">



      jQuery(document).ready(function(){

            // Change text in message send button
            jQuery("button.et_pb_contact_submit.et_pb_button").ready(function(){
                  jQuery("button.et_pb_contact_submit.et_pb_button").text("POŠLJI SPOROČILO");
            });

            // Customize message form
            et_pb_custom["fill_message"] = "Prosim, izpolnite polja:";
            et_pb_custom["contact_error_message"] = "Prosimo odpravite naslednje napake:";

            
            jQuery(".et-social-icons").ready(function(){
                  jQuery(".et-social-icons").append('<li class="et-social-icon et-social-nlpi"><a href="http://nlpi.si/" class="icon" target="_blank"><span>Nlpi</span></a></li>');
            });

            // Dolar sign in price list replacement
            jQuery(".prices_list").ready(function(){
                  var elements = jQuery(".prices_list").find(".et_pb_sum");
                  for( i = 0; i < elements.length; i++)
                  {
                        var str = elements[i].innerHTML
                        elements[i].innerHTML = str.replace('::€::','<span class="et_pb_dollar_sign initial-line-height" style="margin-left: -14px;">€</span>');
                  }                 
            });

            jQuery(".et_pb_countdown_timer_container").ready(function(){

              jQuery(".et_pb_countdown_timer_container > .days > .label")[0].innerText="dni";
              jQuery(".et_pb_countdown_timer_container > .hours > .label")[0].innerText="ur";
              jQuery(".et_pb_countdown_timer_container > .minutes > .label")[0].innerText="minut";
              jQuery(".et_pb_countdown_timer_container > .seconds > .label")[0].innerText="sekund";
            });

            jQuery(".logo_container").ready(function(){

              jQuery(".logo_container > a").attr("href","http://nlpi.si/");
              jQuery(".logo_container > a").attr("target","_blank");

            });
            
            
            

      });
</script>