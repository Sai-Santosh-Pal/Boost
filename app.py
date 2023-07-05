from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = 'sai2010**'

@app.route('/auth/<token>')
def authenticate(token):
    if token.strip() != "":
        return "Authentication successful"
    else:
        return "Invalid token"

@app.route('/')
def home():
    return '''
    <html class="wf-inter-n1-active wf-inter-n2-active wf-inter-n3-active wf-inter-n4-active wf-inter-n5-active wf-inter-n6-active wf-inter-n7-active wf-inter-n8-active wf-poppins-n7-active wf-poppins-n6-active wf-poppins-n4-active wf-poppins-n1-active wf-poppins-n2-active wf-poppins-n3-active wf-poppins-n5-active wf-poppins-n8-active wf-active"><head> <meta charset="utf-8"> <title>boost.io</title> <meta name="google-site-verification" content="jwjHQ5CVGwwCNeZTGmcRlrQWnlCasUvsrz6LKVN9khw" /> <meta content="width=1240, initial-scale=0" name="viewport"> <meta name="description" content=""> <meta property="og:type" content="article"> <meta property="og:title" content="boost.io"> <meta property="og:description" content=""> <meta property="og:image" content="https://s3.us-east-1.amazonaws.com/cdn-siter/7b3fc051-d938-4992-9f6e-0bc04def0ad6-url_og_image.png"> <meta property="twitter:card" content="summary_large_image"> <meta property="twitter:title" content="boost.io"> <meta property="twitter:description" content=""> <meta property="twitter:image" content="https://s3.us-east-1.amazonaws.com/cdn-siter/7b3fc051-d938-4992-9f6e-0bc04def0ad6-url_og_image.png"> <script type="text/javascript" id="www-widgetapi-script" src="https://www.youtube.com/s/player/23604418/www-widgetapi.vflset/www-widgetapi.js" async=""></script><script type="text/javascript" id="variables">
      window.devices = {
        mobile: false,
        tablet: false
      }
       function detectMob() {
        if ( ( window.innerWidth <= 768 ) && ( window.innerHeight <= 1024 ) ) {
                alert("MOBILE OR TABLET");
            }
      }
      
      window.site_id = 'boostio-1688456519347'
      window.page_id = 'pg_Hxy1AtxR8qrL1HTaXF6THWM7P'
      window.pages = [{"path":"boostio","id":"pg_Hxy1AtxR8qrL1HTaXF6THWM7P","home":true},{"path":"privacy-policy","id":"pg_n2prXkLTBBAugZnXyddEPLx3W","home":false}];
      window.preview = true;
    </script> <link rel="stylesheet" media="screen" href="https://api.siter.io/assets/application-4024ba90e1f34a0be61507b2881bf775b48256845135858801ad3db2ab8f89e2.css"><link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Inter:100,200,300,400,500,600,700,800%7CPoppins:100,200,300,400,500,600,700,800" media="all"> <script type="text/javascript" charset="UTF-8" src="https://maps.googleapis.com/maps-api-v3/api/js/53/8/common.js"></script><script type="text/javascript" charset="UTF-8" src="https://maps.googleapis.com/maps-api-v3/api/js/53/8/util.js"></script></head><body> <div class="siter-page page_pg_Hxy1AtxR8qrL1HTaXF6THWM7P"> <div class="page-content"> <div class="page-content__inner" id="page-content" style="transform: scale(1) translateZ(0px);"><div id="9ed0bc87-8f7b-4401-8ff7-4dab05ba6627" class="group_9ed0bc87-8f7b-4401-8ff7-4dab05ba6627" data-type="group">
  
      <div id="634b87a8-190a-4783-a5ab-89a2c719b6cb" class="group_634b87a8-190a-4783-a5ab-89a2c719b6cb" data-type="group">
  
      <div data-unit="px" class="page-content__component rectangle_e6201671-21c7-4040-89cd-41310d2b392a" data-container="grid" id="e6201671-21c7-4040-89cd-41310d2b392a" data-type="rectangle">
  <div class="strw-shape"></div>
  
</div><div id="8b210b7d-01c6-477a-9e27-70b705642aba" class="group_8b210b7d-01c6-477a-9e27-70b705642aba" data-type="group">

      <div class="page-content__component text_f5aed3a3-3e39-46ef-ad05-c5c1fec00a7e" data-container="grid" id="f5aed3a3-3e39-46ef-ad05-c5c1fec00a7e" data-type="text"><div data-wysiwyg="true">Runs At Realtime</div></div><div class="page-content__component text_79db6e15-7846-4c67-ae98-8c67bc25e694" data-container="grid" id="79db6e15-7846-4c67-ae98-8c67bc25e694" data-type="text"><div data-wysiwyg="true">It uses the Official YouTube API</div></div><style>.text_f5aed3a3-3e39-46ef-ad05-c5c1fec00a7e [data-wysiwyg="true"] {
  display: table-cell;
  vertical-align: middle
}


  


.text_f5aed3a3-3e39-46ef-ad05-c5c1fec00a7e {
  
  color: rgba(255, 255, 255, 1);
  
}



.text_f5aed3a3-3e39-46ef-ad05-c5c1fec00a7e { top: 1869.23px;left: 875.868px;width: 201.976px;height: 29.889px;display: table;opacity: 1;font-size: 24px;position: absolute;text-align: left;font-family: Inter;font-weight: 500;line-height: 30px;text-shadow: none;visibility: inherit;letter-spacing: -0.041666666666666664em;box-shadow: none;text-transform: normal;text-decoration: none; }.text_f5aed3a3-3e39-46ef-ad05-c5c1fec00a7e {
            left: -moz-calc(50% - 600px + 875.868px);
            left: -webkit-calc(50% - 600px + 875.868px);
            left: -o-calc(50% - 600px + 875.868px);
            left: calc(50% - 600px + 875.868px)
          }.text_79db6e15-7846-4c67-ae98-8c67bc25e694 [data-wysiwyg="true"] {
  display: table-cell;
  vertical-align: top
}


  


.text_79db6e15-7846-4c67-ae98-8c67bc25e694 {
  
  color: rgba(255, 255, 255, 0.699999988079071);
  
}



.text_79db6e15-7846-4c67-ae98-8c67bc25e694 { top: 1910.23px;left: 875.868px;width: 220.828px;height: 59.778px;display: table;opacity: 1;font-size: 21px;position: absolute;text-align: left;font-family: Inter;font-weight: 400;line-height: 30px;text-shadow: none;visibility: inherit;letter-spacing: -0.038095238662901376em;box-shadow: none;text-transform: normal;text-decoration: none; }.text_79db6e15-7846-4c67-ae98-8c67bc25e694 {
            left: -moz-calc(50% - 600px + 875.868px);
            left: -webkit-calc(50% - 600px + 875.868px);
            left: -o-calc(50% - 600px + 875.868px);
            left: calc(50% - 600px + 875.868px)
          }</style>
  
</div><div id="49249130-3b13-4288-b35d-f70b195c1073" class="group_49249130-3b13-4288-b35d-f70b195c1073" data-type="group">
  
      <div class="page-content__component text_fcdd19c4-9e3f-4fc2-83ed-5066029eb9e9" data-container="grid" id="fcdd19c4-9e3f-4fc2-83ed-5066029eb9e9" data-type="text"><div data-wysiwyg="true">The charts based on your data are shown </div></div><div class="page-content__component text_fd72cc75-e643-45fd-b7c5-a496b7d9e94b" data-container="grid" id="fd72cc75-e643-45fd-b7c5-a496b7d9e94b" data-type="text"><div data-wysiwyg="true">Shows Charts</div></div><style>.text_fcdd19c4-9e3f-4fc2-83ed-5066029eb9e9 [data-wysiwyg="true"] {
  display: table-cell;
  vertical-align: top
}


  


.text_fcdd19c4-9e3f-4fc2-83ed-5066029eb9e9 {
  
  color: rgba(255, 255, 255, 0.699999988079071);
  
}



.text_fcdd19c4-9e3f-4fc2-83ed-5066029eb9e9 { top: 1910.23px;left: 578.743px;width: 215.442px;height: 59.778px;display: table;opacity: 1;font-size: 21px;position: absolute;text-align: left;font-family: Inter;font-weight: 400;line-height: 30px;text-shadow: none;visibility: inherit;letter-spacing: -0.038095238662901376em;box-shadow: none;text-transform: normal;text-decoration: none; }.text_fcdd19c4-9e3f-4fc2-83ed-5066029eb9e9 {
            left: -moz-calc(50% - 600px + 578.743px);
            left: -webkit-calc(50% - 600px + 578.743px);
            left: -o-calc(50% - 600px + 578.743px);
            left: calc(50% - 600px + 578.743px)
          }.text_fd72cc75-e643-45fd-b7c5-a496b7d9e94b [data-wysiwyg="true"] {
  display: table-cell;
  vertical-align: middle
}


  


.text_fd72cc75-e643-45fd-b7c5-a496b7d9e94b {
  
  color: rgba(255, 255, 255, 1);
  
}



.text_fd72cc75-e643-45fd-b7c5-a496b7d9e94b { top: 1867.23px;left: 578.743px;width: 249.553px;height: 31.8816px;display: table;opacity: 1;font-size: 24px;position: absolute;text-align: left;font-family: Inter;font-weight: 500;line-height: 30px;text-shadow: none;visibility: inherit;letter-spacing: -0.041666666666666664em;box-shadow: none;text-transform: normal;text-decoration: none; }.text_fd72cc75-e643-45fd-b7c5-a496b7d9e94b {
            left: -moz-calc(50% - 600px + 578.743px);
            left: -webkit-calc(50% - 600px + 578.743px);
            left: -o-calc(50% - 600px + 578.743px);
            left: calc(50% - 600px + 578.743px)
          }</style>
  
</div><div id="76aa68c4-6caf-4dfc-b02f-296a8a80d686" class="group_76aa68c4-6caf-4dfc-b02f-296a8a80d686" data-type="group">
  
      <div class="page-content__component text_54472877-7a07-416e-9d2b-396ab0934e36" data-container="grid" id="54472877-7a07-416e-9d2b-396ab0934e36" data-type="text"><div data-wysiwyg="true">Your data is read by the systems to make charts and predictions.</div></div><div class="page-content__component text_dd17364a-9ace-4277-9591-e77ada923cac" data-container="grid" id="dd17364a-9ace-4277-9591-e77ada923cac" data-type="text"><div data-wysiwyg="true">Read Your Data</div></div><style>.text_54472877-7a07-416e-9d2b-396ab0934e36 [data-wysiwyg="true"] {
  display: table-cell;
  vertical-align: top
}


  


.text_54472877-7a07-416e-9d2b-396ab0934e36 {
  
  color: rgba(255, 255, 255, 0.699999988079071);
  
}



.text_54472877-7a07-416e-9d2b-396ab0934e36 { top: 1910.23px;left: 284.306px;width: 244.167px;height: 89.667px;display: table;opacity: 1;font-size: 21px;position: absolute;text-align: left;font-family: Inter;font-weight: 400;line-height: 30px;text-shadow: none;visibility: inherit;letter-spacing: -0.038095238662901376em;box-shadow: none;text-transform: normal;text-decoration: none; }.text_54472877-7a07-416e-9d2b-396ab0934e36 {
            left: -moz-calc(50% - 600px + 284.306px);
            left: -webkit-calc(50% - 600px + 284.306px);
            left: -o-calc(50% - 600px + 284.306px);
            left: calc(50% - 600px + 284.306px)
          }.text_dd17364a-9ace-4277-9591-e77ada923cac [data-wysiwyg="true"] {
  display: table-cell;
  vertical-align: middle
}


  


.text_dd17364a-9ace-4277-9591-e77ada923cac {
  
  color: rgba(255, 255, 255, 1);
  
}



.text_dd17364a-9ace-4277-9591-e77ada923cac { top: 1869.23px;left: 284.306px;width: 201.976px;height: 29.889px;display: table;opacity: 1;font-size: 24px;position: absolute;text-align: left;font-family: Inter;font-weight: 500;line-height: 30px;text-shadow: none;visibility: inherit;letter-spacing: -0.041666666666666664em;box-shadow: none;text-transform: normal;text-decoration: none; }.text_dd17364a-9ace-4277-9591-e77ada923cac {
            left: -moz-calc(50% - 600px + 284.306px);
            left: -webkit-calc(50% - 600px + 284.306px);
            left: -o-calc(50% - 600px + 284.306px);
            left: calc(50% - 600px + 284.306px)
          }</style>
  
</div><div id="7025729d-d92f-432f-9381-e20ca3ff15ba" class="group_7025729d-d92f-432f-9381-e20ca3ff15ba" data-type="group">
  
      <div class="page-content__component text_8a1cd686-f9f7-49ca-861d-5c5406b274ba" data-container="grid" id="8a1cd686-f9f7-49ca-861d-5c5406b274ba" data-type="text"><div data-wysiwyg="true">We ask you for you google authentication, so that we can access your YouTube channel’s data.</div></div><div class="page-content__component text_14fc2264-3093-46fc-9db2-692dd0efad70" data-container="grid" id="14fc2264-3093-46fc-9db2-692dd0efad70" data-type="text"><div data-wysiwyg="true">Authenticate</div></div><style>.text_8a1cd686-f9f7-49ca-861d-5c5406b274ba [data-wysiwyg="true"] {
  display: table-cell;
  vertical-align: top
}


  


.text_8a1cd686-f9f7-49ca-861d-5c5406b274ba {
  
  color: rgba(255, 255, 255, 0.699999988079071);
  
}



.text_8a1cd686-f9f7-49ca-861d-5c5406b274ba { top: 1910.23px;left: -12.823999999999998px;width: 242.372px;height: 119.556px;display: table;opacity: 1;font-size: 21px;position: absolute;text-align: left;font-family: Inter;font-weight: 400;line-height: 30px;text-shadow: none;visibility: inherit;letter-spacing: -0.038095238662901376em;box-shadow: none;text-transform: normal;text-decoration: none; }.text_8a1cd686-f9f7-49ca-861d-5c5406b274ba {
            left: -moz-calc(50% - 600px + -12.823999999999998px);
            left: -webkit-calc(50% - 600px + -12.823999999999998px);
            left: -o-calc(50% - 600px + -12.823999999999998px);
            left: calc(50% - 600px + -12.823999999999998px)
          }.text_14fc2264-3093-46fc-9db2-692dd0efad70 [data-wysiwyg="true"] {
  display: table-cell;
  vertical-align: middle
}


  


.text_14fc2264-3093-46fc-9db2-692dd0efad70 {
  
  color: rgba(255, 255, 255, 1);
  
}



.text_14fc2264-3093-46fc-9db2-692dd0efad70 { top: 1869.23px;left: -12.823999999999998px;width: 249.553px;height: 29.889px;display: table;opacity: 1;font-size: 24px;position: absolute;text-align: left;font-family: Inter;font-weight: 500;line-height: 30px;text-shadow: none;visibility: inherit;letter-spacing: -0.041666666666666664em;box-shadow: none;text-transform: normal;text-decoration: none; }.text_14fc2264-3093-46fc-9db2-692dd0efad70 {
            left: -moz-calc(50% - 600px + -12.823999999999998px);
            left: -webkit-calc(50% - 600px + -12.823999999999998px);
            left: -o-calc(50% - 600px + -12.823999999999998px);
            left: calc(50% - 600px + -12.823999999999998px)
          }</style>
  
</div><div id="c91423fe-3870-4527-83ab-8f355bfed45c" class="group_c91423fe-3870-4527-83ab-8f355bfed45c" data-type="group">
  
      <div data-unit="px" class="page-content__component rectangle_c5cc1b9a-8f88-4b7b-a2d8-8a43b6aa7cc6" data-container="grid" id="c5cc1b9a-8f88-4b7b-a2d8-8a43b6aa7cc6" data-type="rectangle">
  <div class="strw-shape"></div>
  
</div><div data-unit="px" class="page-content__component rectangle_392c031c-918f-4967-98e0-bc2d28cd3580" data-container="grid" id="392c031c-918f-4967-98e0-bc2d28cd3580" data-type="rectangle">
  <div class="strw-shape"></div>
  
</div><div data-unit="px" class="page-content__component rectangle_0d3ee2d6-aa91-48f3-97ca-74bce8b9a788" data-container="grid" id="0d3ee2d6-aa91-48f3-97ca-74bce8b9a788" data-type="rectangle">
  <div class="strw-shape"></div>
  
</div><div data-unit="px" class="page-content__component rectangle_ca7580b4-dff8-47fe-9bbb-68874264c72f" data-container="grid" id="ca7580b4-dff8-47fe-9bbb-68874264c72f" data-type="rectangle">
  <div class="strw-shape"></div>
  
</div><div data-unit="px" class="page-content__component rectangle_384bfd56-c85b-452f-bdba-17064135a753" data-container="grid" id="384bfd56-c85b-452f-bdba-17064135a753" data-type="rectangle">
  <div class="strw-shape"></div>
  
</div><div data-unit="px" class="page-content__component rectangle_c7ddcec4-4f85-49ac-a70d-117818a6481c" data-container="grid" id="c7ddcec4-4f85-49ac-a70d-117818a6481c" data-type="rectangle">
  <div class="strw-shape"></div>
  
</div><style>.rectangle_c5cc1b9a-8f88-4b7b-a2d8-8a43b6aa7cc6 .strw-shape {
  content: '';
  position: absolute;
  top:0;
  left: 0;
  right:0;
  bottom:0;
  background-image: -webkit-linear-gradient(90.00000000000253deg,rgba(255, 255, 255, 1) NaN%, rgba(255, 255, 255, 0) NaN%);
  background-image:    -moz-linear-gradient(90.00000000000253deg,rgba(255, 255, 255, 1) NaN%, rgba(255, 255, 255, 0) NaN%);
  background-image:     -ms-linear-gradient(90.00000000000253deg,rgba(255, 255, 255, 1) NaN%, rgba(255, 255, 255, 0) NaN%);
  background-image:      -o-linear-gradient(90.00000000000253deg,rgba(255, 255, 255, 1) NaN%, rgba(255, 255, 255, 0) NaN%);
  background-image:         linear-gradient(90.00000000000253deg,rgba(255, 255, 255, 1) NaN%, rgba(255, 255, 255, 0) NaN%);
}

.rectangle_c5cc1b9a-8f88-4b7b-a2d8-8a43b6aa7cc6:hover .strw-shape {
  
    opacity: 1;
    background-image: -webkit-;
    background-image:    -moz-;
    background-image:     -ms-;
    background-image:      -o-;
    background-image:         ;
  
}.rectangle_c5cc1b9a-8f88-4b7b-a2d8-8a43b6aa7cc6 { top: 1832.23px;left: -12.823999999999998px;width: 1157.1px;border: none;height: 1.9926px;opacity: 1;overflow: hidden;position: absolute;box-shadow: none;visibility: inherit;background-size: cover;background-repeat: no-repeat;background-position: center;border-radius: 0px 0px 0px 0px; }.rectangle_c5cc1b9a-8f88-4b7b-a2d8-8a43b6aa7cc6 {
            left: -moz-calc(50% - 600px + -12.823999999999998px);
            left: -webkit-calc(50% - 600px + -12.823999999999998px);
            left: -o-calc(50% - 600px + -12.823999999999998px);
            left: calc(50% - 600px + -12.823999999999998px)
          }.rectangle_392c031c-918f-4967-98e0-bc2d28cd3580 .strw-shape {
  content: '';
  position: absolute;
  top:0;
  left: 0;
  right:0;
  bottom:0;
  background-image: -webkit-linear-gradient(to right, rgba(255, 255, 255, 1), rgba(255, 255, 255, 1));
  background-image:    -moz-linear-gradient(to right, rgba(255, 255, 255, 1), rgba(255, 255, 255, 1));
  background-image:     -ms-linear-gradient(to right, rgba(255, 255, 255, 1), rgba(255, 255, 255, 1));
  background-image:      -o-linear-gradient(to right, rgba(255, 255, 255, 1), rgba(255, 255, 255, 1));
  background-image:         linear-gradient(to right, rgba(255, 255, 255, 1), rgba(255, 255, 255, 1));
}

.rectangle_392c031c-918f-4967-98e0-bc2d28cd3580:hover .strw-shape {
  
    opacity: 1;
    background-image: -webkit-;
    background-image:    -moz-;
    background-image:     -ms-;
    background-image:      -o-;
    background-image:         ;
  
}.rectangle_392c031c-918f-4967-98e0-bc2d28cd3580 { top: 1826.23px;left: -13.721999999999994px;width: 10.7721px;border: none;height: 11.9556px;opacity: 1;overflow: hidden;position: absolute;box-shadow: none;visibility: inherit;background-size: cover;background-repeat: no-repeat;background-position: center;border-radius: 50%; }.rectangle_392c031c-918f-4967-98e0-bc2d28cd3580 {
            left: -moz-calc(50% - 600px + -13.721999999999994px);
            left: -webkit-calc(50% - 600px + -13.721999999999994px);
            left: -o-calc(50% - 600px + -13.721999999999994px);
            left: calc(50% - 600px + -13.721999999999994px)
          }.rectangle_0d3ee2d6-aa91-48f3-97ca-74bce8b9a788 .strw-shape {
  content: '';
  position: absolute;
  top:0;
  left: 0;
  right:0;
  bottom:0;
  background-image: -webkit-linear-gradient(to right, rgba(255, 255, 255, 1), rgba(255, 255, 255, 1));
  background-image:    -moz-linear-gradient(to right, rgba(255, 255, 255, 1), rgba(255, 255, 255, 1));
  background-image:     -ms-linear-gradient(to right, rgba(255, 255, 255, 1), rgba(255, 255, 255, 1));
  background-image:      -o-linear-gradient(to right, rgba(255, 255, 255, 1), rgba(255, 255, 255, 1));
  background-image:         linear-gradient(to right, rgba(255, 255, 255, 1), rgba(255, 255, 255, 1));
}

.rectangle_0d3ee2d6-aa91-48f3-97ca-74bce8b9a788:hover .strw-shape {
  
    opacity: 1;
    background-image: -webkit-;
    background-image:    -moz-;
    background-image:     -ms-;
    background-image:      -o-;
    background-image:         ;
  
}.rectangle_0d3ee2d6-aa91-48f3-97ca-74bce8b9a788 { top: 1826.23px;left: 284.306px;width: 10.7721px;border: none;height: 11.9556px;opacity: 1;overflow: hidden;position: absolute;box-shadow: none;visibility: inherit;background-size: cover;background-repeat: no-repeat;background-position: center;border-radius: 50%; }.rectangle_0d3ee2d6-aa91-48f3-97ca-74bce8b9a788 {
            left: -moz-calc(50% - 600px + 284.306px);
            left: -webkit-calc(50% - 600px + 284.306px);
            left: -o-calc(50% - 600px + 284.306px);
            left: calc(50% - 600px + 284.306px)
          }.rectangle_ca7580b4-dff8-47fe-9bbb-68874264c72f .strw-shape {
  content: '';
  position: absolute;
  top:0;
  left: 0;
  right:0;
  bottom:0;
  background-image: -webkit-linear-gradient(to right, rgba(255, 255, 255, 1), rgba(255, 255, 255, 1));
  background-image:    -moz-linear-gradient(to right, rgba(255, 255, 255, 1), rgba(255, 255, 255, 1));
  background-image:     -ms-linear-gradient(to right, rgba(255, 255, 255, 1), rgba(255, 255, 255, 1));
  background-image:      -o-linear-gradient(to right, rgba(255, 255, 255, 1), rgba(255, 255, 255, 1));
  background-image:         linear-gradient(to right, rgba(255, 255, 255, 1), rgba(255, 255, 255, 1));
}

.rectangle_ca7580b4-dff8-47fe-9bbb-68874264c72f:hover .strw-shape {
  
    opacity: 1;
    background-image: -webkit-;
    background-image:    -moz-;
    background-image:     -ms-;
    background-image:      -o-;
    background-image:         ;
  
}.rectangle_ca7580b4-dff8-47fe-9bbb-68874264c72f { top: 1826.23px;left: 284.306px;width: 10.7721px;border: none;height: 11.9556px;opacity: 1;overflow: hidden;position: absolute;box-shadow: none;visibility: inherit;background-size: cover;background-repeat: no-repeat;background-position: center;border-radius: 50%; }.rectangle_ca7580b4-dff8-47fe-9bbb-68874264c72f {
            left: -moz-calc(50% - 600px + 284.306px);
            left: -webkit-calc(50% - 600px + 284.306px);
            left: -o-calc(50% - 600px + 284.306px);
            left: calc(50% - 600px + 284.306px)
          }.rectangle_384bfd56-c85b-452f-bdba-17064135a753 .strw-shape {
  content: '';
  position: absolute;
  top:0;
  left: 0;
  right:0;
  bottom:0;
  background-image: -webkit-linear-gradient(to right, rgba(231, 234, 252, 1), rgba(231, 234, 252, 1));
  background-image:    -moz-linear-gradient(to right, rgba(231, 234, 252, 1), rgba(231, 234, 252, 1));
  background-image:     -ms-linear-gradient(to right, rgba(231, 234, 252, 1), rgba(231, 234, 252, 1));
  background-image:      -o-linear-gradient(to right, rgba(231, 234, 252, 1), rgba(231, 234, 252, 1));
  background-image:         linear-gradient(to right, rgba(231, 234, 252, 1), rgba(231, 234, 252, 1));
}

.rectangle_384bfd56-c85b-452f-bdba-17064135a753:hover .strw-shape {
  
    opacity: 1;
    background-image: -webkit-;
    background-image:    -moz-;
    background-image:     -ms-;
    background-image:      -o-;
    background-image:         ;
  
}.rectangle_384bfd56-c85b-452f-bdba-17064135a753 { top: 1826.23px;left: 578.743px;width: 10.7721px;border: none;height: 11.9556px;opacity: 1;overflow: hidden;position: absolute;box-shadow: none;visibility: inherit;background-size: cover;background-repeat: no-repeat;background-position: center;border-radius: 50%; }.rectangle_384bfd56-c85b-452f-bdba-17064135a753 {
            left: -moz-calc(50% - 600px + 578.743px);
            left: -webkit-calc(50% - 600px + 578.743px);
            left: -o-calc(50% - 600px + 578.743px);
            left: calc(50% - 600px + 578.743px)
          }.rectangle_c7ddcec4-4f85-49ac-a70d-117818a6481c .strw-shape {
  content: '';
  position: absolute;
  top:0;
  left: 0;
  right:0;
  bottom:0;
  background-image: -webkit-linear-gradient(to right, rgba(181, 190, 244, 1), rgba(181, 190, 244, 1));
  background-image:    -moz-linear-gradient(to right, rgba(181, 190, 244, 1), rgba(181, 190, 244, 1));
  background-image:     -ms-linear-gradient(to right, rgba(181, 190, 244, 1), rgba(181, 190, 244, 1));
  background-image:      -o-linear-gradient(to right, rgba(181, 190, 244, 1), rgba(181, 190, 244, 1));
  background-image:         linear-gradient(to right, rgba(181, 190, 244, 1), rgba(181, 190, 244, 1));
}

.rectangle_c7ddcec4-4f85-49ac-a70d-117818a6481c:hover .strw-shape {
  
    opacity: 1;
    background-image: -webkit-;
    background-image:    -moz-;
    background-image:     -ms-;
    background-image:      -o-;
    background-image:         ;
  
}.rectangle_c7ddcec4-4f85-49ac-a70d-117818a6481c { top: 1826.23px;left: 875.868px;width: 10.7721px;border: none;height: 11.9556px;opacity: 1;overflow: hidden;position: absolute;box-shadow: none;visibility: inherit;background-size: cover;background-repeat: no-repeat;background-position: center;border-radius: 50%; }.rectangle_c7ddcec4-4f85-49ac-a70d-117818a6481c {
            left: -moz-calc(50% - 600px + 875.868px);
            left: -webkit-calc(50% - 600px + 875.868px);
            left: -o-calc(50% - 600px + 875.868px);
            left: calc(50% - 600px + 875.868px)
          }</style>
  
</div><div class="page-content__component text_17b54a45-9376-42a3-b844-bfc64cdac492" data-container="grid" id="17b54a45-9376-42a3-b844-bfc64cdac492" data-type="text"><div data-wysiwyg="true"><div style="vertical-align: top;" tab-index="3" text-content="true">We Believe In Transparency,<br class="nl-desktop">
So Do Our Systems</div>

</div></div><style>.rectangle_e6201671-21c7-4040-89cd-41310d2b392a .strw-shape {
  content: '';
  position: absolute;
  top:0;
  left: 0;
  right:0;
  bottom:0;
  background-image: -webkit-linear-gradient(to right, rgba(72, 95, 229, 1), rgba(72, 95, 229, 1));
  background-image:    -moz-linear-gradient(to right, rgba(72, 95, 229, 1), rgba(72, 95, 229, 1));
  background-image:     -ms-linear-gradient(to right, rgba(72, 95, 229, 1), rgba(72, 95, 229, 1));
  background-image:      -o-linear-gradient(to right, rgba(72, 95, 229, 1), rgba(72, 95, 229, 1));
  background-image:         linear-gradient(to right, rgba(72, 95, 229, 1), rgba(72, 95, 229, 1));
}

.rectangle_e6201671-21c7-4040-89cd-41310d2b392a:hover .strw-shape {
  
    opacity: 1;
    background-image: -webkit-;
    background-image:    -moz-;
    background-image:     -ms-;
    background-image:      -o-;
    background-image:         ;
  
}.rectangle_e6201671-21c7-4040-89cd-41310d2b392a { top: 1564.23px;left: -400.271px;width: 1894.89px;border: none;height: 567.891px;opacity: 1;overflow: hidden;position: absolute;box-shadow: none;visibility: inherit;background-size: cover;background-repeat: no-repeat;background-position: center;border-radius: 0px 0px 0px 0px; }.rectangle_e6201671-21c7-4040-89cd-41310d2b392a {
            left: -moz-calc(50% - 600px + -400.271px);
            left: -webkit-calc(50% - 600px + -400.271px);
            left: -o-calc(50% - 600px + -400.271px);
            left: calc(50% - 600px + -400.271px)
          }.group_8b210b7d-01c6-477a-9e27-70b705642aba { top: 0px;left: 0px;width: 100%;height: 0px;opacity: 1;position: absolute;visibility: inherit;background-color: transparent; }.group_49249130-3b13-4288-b35d-f70b195c1073 { top: 0px;left: 0px;width: 100%;height: 0px;opacity: 1;position: absolute;visibility: inherit;background-color: transparent; }.group_76aa68c4-6caf-4dfc-b02f-296a8a80d686 { top: 0px;left: 0px;width: 100%;height: 0px;opacity: 1;position: absolute;visibility: inherit;background-color: transparent; }.group_7025729d-d92f-432f-9381-e20ca3ff15ba { top: 0px;left: 0px;width: 100%;height: 0px;opacity: 1;position: absolute;visibility: inherit;background-color: transparent; }.group_c91423fe-3870-4527-83ab-8f355bfed45c { top: 0px;left: 0px;width: 100%;height: 0px;opacity: 1;position: absolute;visibility: inherit;background-color: transparent; }.text_17b54a45-9376-42a3-b844-bfc64cdac492 [data-wysiwyg="true"] {
  display: table-cell;
  vertical-align: top
}


  


.text_17b54a45-9376-42a3-b844-bfc64cdac492 {
  
  color: rgba(255, 255, 255, 1);
  
}



.text_17b54a45-9376-42a3-b844-bfc64cdac492 { top: 1660.23px;left: -15.516999999999996px;width: 687.984px;height: 107.6px;display: table;opacity: 1;font-size: 48px;position: absolute;text-align: left;font-family: Inter;font-weight: 500;line-height: 54px;text-shadow: none;visibility: inherit;letter-spacing: -0.033333333830038704em;box-shadow: none;text-transform: normal;text-decoration: none; }.text_17b54a45-9376-42a3-b844-bfc64cdac492 {
            left: -moz-calc(50% - 600px + -15.516999999999996px);
            left: -webkit-calc(50% - 600px + -15.516999999999996px);
            left: -o-calc(50% - 600px + -15.516999999999996px);
            left: calc(50% - 600px + -15.516999999999996px)
          }</style>
  
</div><div id="f05805d9-d324-4615-b4ba-1596188c2c7c" class="group_f05805d9-d324-4615-b4ba-1596188c2c7c" data-type="group">
  
      <div id="3fad6432-d672-4b8d-8977-e69a509c3e8a" class="group_3fad6432-d672-4b8d-8977-e69a509c3e8a" data-type="group">
  
      <div data-unit="px" class="page-content__component rectangle_cc838662-cfe6-4a33-9bd9-5b57c8a00f55" data-container="grid" id="cc838662-cfe6-4a33-9bd9-5b57c8a00f55" data-type="rectangle">
  <div class="strw-shape"></div>
  
</div><div id="048472ea-972a-41b6-b183-b92ffffbfe51" class="group_048472ea-972a-41b6-b183-b92ffffbfe51" data-type="group">
  
      <div data-unit="px" class="page-content__component rectangle_97aee2fc-34be-4138-97a5-e382cb6f8eb6" data-container="grid" id="97aee2fc-34be-4138-97a5-e382cb6f8eb6" data-type="rectangle">
  <div class="strw-shape"></div>
  
</div><div id="f6c4ff10-f003-4b6a-96f1-ab53642c562d" class="group_f6c4ff10-f003-4b6a-96f1-ab53642c562d" data-type="group">
  
      <div data-unit="px" data-container="grid" id="866a517b-5720-463e-8361-c4b3111f6f9e" data-type="image" class="page-content__component image_866a517b-5720-463e-8361-c4b3111f6f9e" style="background-image:url('https://cdn.siter.io/assets/ast_4j4oHgyWXTtHQTwYrUvP6LTH7/68eb988c-66ea-43c5-b7e0-414fdc8fea2d.svg');" data-bg="image">
  <div class="strw-shape"></div>
  
</div><div data-unit="px" data-container="grid" id="945271bd-a880-4290-adb0-f0a4664059f8" data-type="image" class="page-content__component image_945271bd-a880-4290-adb0-f0a4664059f8" style="background-image:url('https://cdn.siter.io/assets/ast_u6WkiAMeDuMnTva1VqACpKimi/08979a1b-cf43-4d4f-b08a-0d010f09d5ee.svg');" data-bg="image">
  <div class="strw-shape"></div>
  
</div><div data-unit="px" data-container="grid" id="f5ca08f2-85ed-4a2d-a98c-ed5a75a1a13e" data-type="image" class="page-content__component image_f5ca08f2-85ed-4a2d-a98c-ed5a75a1a13e" style="background-image:url('https://cdn.siter.io/assets/ast_G4znsheAUnTdr3wNArvHyE7Nn/b5e343e9-20de-4d90-b2cc-396248fcf599.svg');" data-bg="image">
  <div class="strw-shape"></div>
  
</div><div id="546f6bfe-47d3-4ae8-80ff-badba63c4378" class="group_546f6bfe-47d3-4ae8-80ff-badba63c4378" data-type="group">
  
      <div data-unit="px" class="page-content__component rectangle_cbaa9d6f-bcc0-40c0-8369-fdfb1d9e64c6" data-container="grid" id="cbaa9d6f-bcc0-40c0-8369-fdfb1d9e64c6" data-type="rectangle">
  <div class="strw-shape"></div>
  
</div><style>.rectangle_cbaa9d6f-bcc0-40c0-8369-fdfb1d9e64c6 .strw-shape {
  content: '';
  position: absolute;
  top:0;
  left: 0;
  right:0;
  bottom:0;
  background-image: -webkit-linear-gradient(to right, rgba(98, 76, 224, 1), rgba(98, 76, 224, 1));
  background-image:    -moz-linear-gradient(to right, rgba(98, 76, 224, 1), rgba(98, 76, 224, 1));
  background-image:     -ms-linear-gradient(to right, rgba(98, 76, 224, 1), rgba(98, 76, 224, 1));
  background-image:      -o-linear-gradient(to right, rgba(98, 76, 224, 1), rgba(98, 76, 224, 1));
  background-image:         linear-gradient(to right, rgba(98, 76, 224, 1), rgba(98, 76, 224, 1));
}

.rectangle_cbaa9d6f-bcc0-40c0-8369-fdfb1d9e64c6:hover .strw-shape {
  
    opacity: 1;
    background-image: -webkit-;
    background-image:    -moz-;
    background-image:     -ms-;
    background-image:      -o-;
    background-image:         ;
  
}.rectangle_cbaa9d6f-bcc0-40c0-8369-fdfb1d9e64c6 { top: 1311.23px;left: 1054.1px;width: 9px;border: none;height: 8.9667px;opacity: 1;overflow: hidden;position: absolute;box-shadow: none;visibility: inherit;background-size: cover;background-repeat: no-repeat;background-position: center;border-radius: 50%; }.rectangle_cbaa9d6f-bcc0-40c0-8369-fdfb1d9e64c6 {
            left: -moz-calc(50% - 600px + 1054.1px);
            left: -webkit-calc(50% - 600px + 1054.1px);
            left: -o-calc(50% - 600px + 1054.1px);
            left: calc(50% - 600px + 1054.1px)
          }</style>
  
</div><div data-unit="px" data-container="grid" id="b9c0aa7f-7bc1-44d5-9508-51392da851aa" data-type="image" class="page-content__component image_b9c0aa7f-7bc1-44d5-9508-51392da851aa" style="background-image:url('https://cdn.siter.io/assets/ast_c6GfetQ56oA1miaLk1aDwUgxF/002311c4-f6e9-491a-878f-d8cda8a84040.svg');" data-bg="image">
  <div class="strw-shape"></div>
  
</div><style>.image_866a517b-5720-463e-8361-c4b3111f6f9e:before {
  content: '';
  position: absolute;
  top:0;
  left: 0;
  right:0;
  bottom:0;

  background-image: -webkit-;
  background-image:    -moz-;
  background-image:     -ms-;
  background-image:      -o-;
  background-image:         ;
}.image_866a517b-5720-463e-8361-c4b3111f6f9e { top: 1138.23px;left: 692.006px;width: 526px;height: 341.731px;opacity: 1;overflow: hidden;position: absolute;visibility: inherit;background-size: cover;background-image: none;background-repeat: no-repeat;background-position: center;box-shadow: none;border-radius: 0px 0px 0px 0px; }.image_866a517b-5720-463e-8361-c4b3111f6f9e {
            left: -moz-calc(50% - 600px + 692.006px);
            left: -webkit-calc(50% - 600px + 692.006px);
            left: -o-calc(50% - 600px + 692.006px);
            left: calc(50% - 600px + 692.006px)
          }.image_945271bd-a880-4290-adb0-f0a4664059f8:before {
  content: '';
  position: absolute;
  top:0;
  left: 0;
  right:0;
  bottom:0;

  background-image: -webkit-;
  background-image:    -moz-;
  background-image:     -ms-;
  background-image:      -o-;
  background-image:         ;
}.image_945271bd-a880-4290-adb0-f0a4664059f8 { top: 1312.23px;left: 1019.6199999999999px;width: 81px;height: 167.378px;opacity: 1;overflow: hidden;position: absolute;visibility: inherit;background-size: cover;background-image: none;background-repeat: no-repeat;background-position: center;box-shadow: none;border-radius: 0px 0px 0px 0px; }.image_945271bd-a880-4290-adb0-f0a4664059f8 {
            left: -moz-calc(50% - 600px + 1019.6199999999999px);
            left: -webkit-calc(50% - 600px + 1019.6199999999999px);
            left: -o-calc(50% - 600px + 1019.6199999999999px);
            left: calc(50% - 600px + 1019.6199999999999px)
          }.image_f5ca08f2-85ed-4a2d-a98c-ed5a75a1a13e:before {
  content: '';
  position: absolute;
  top:0;
  left: 0;
  right:0;
  bottom:0;

  background-image: -webkit-;
  background-image:    -moz-;
  background-image:     -ms-;
  background-image:      -o-;
  background-image:         ;
}.image_f5ca08f2-85ed-4a2d-a98c-ed5a75a1a13e { top: 1138.23px;left: 690.86px;width: 526px;height: 332.764px;opacity: 1;overflow: hidden;position: absolute;visibility: inherit;background-size: cover;background-image: none;background-repeat: no-repeat;background-position: center;box-shadow: none;border-radius: 0px 0px 0px 0px; }.image_f5ca08f2-85ed-4a2d-a98c-ed5a75a1a13e {
            left: -moz-calc(50% - 600px + 690.86px);
            left: -webkit-calc(50% - 600px + 690.86px);
            left: -o-calc(50% - 600px + 690.86px);
            left: calc(50% - 600px + 690.86px)
          }.group_546f6bfe-47d3-4ae8-80ff-badba63c4378 { top: 0px;left: 0px;width: 100%;height: 0px;opacity: 1;position: absolute;visibility: inherit;background-color: transparent; }.image_b9c0aa7f-7bc1-44d5-9508-51392da851aa:before {
  content: '';
  position: absolute;
  top:0;
  left: 0;
  right:0;
  bottom:0;

  background-image: -webkit-;
  background-image:    -moz-;
  background-image:     -ms-;
  background-image:      -o-;
  background-image:         ;
}.image_b9c0aa7f-7bc1-44d5-9508-51392da851aa { top: 1445.23px;left: 1019.6199999999999px;width: 80px;height: 9.963px;opacity: 1;overflow: hidden;position: absolute;visibility: inherit;background-size: cover;background-image: none;background-repeat: no-repeat;background-position: center;box-shadow: none;border-radius: 0px 0px 0px 0px; }.image_b9c0aa7f-7bc1-44d5-9508-51392da851aa {
            left: -moz-calc(50% - 600px + 1019.6199999999999px);
            left: -webkit-calc(50% - 600px + 1019.6199999999999px);
            left: -o-calc(50% - 600px + 1019.6199999999999px);
            left: calc(50% - 600px + 1019.6199999999999px)
          }</style>
  
</div><div id="d24decd6-261f-4b44-b3d0-701cf90a6639" class="group_d24decd6-261f-4b44-b3d0-701cf90a6639" data-type="group">
  
      <div class="page-content__component text_abce10d4-25a2-46d5-a2e8-f823e4d712d2" data-container="grid" id="abce10d4-25a2-46d5-a2e8-f823e4d712d2" data-type="text"><div data-wysiwyg="true">Views</div></div><div class="page-content__component text_f8c09f08-97d7-4880-b359-b0250541b8c4" data-container="grid" id="f8c09f08-97d7-4880-b359-b0250541b8c4" data-type="text"><div data-wysiwyg="true">10,230</div></div><style>.text_abce10d4-25a2-46d5-a2e8-f823e4d712d2 [data-wysiwyg="true"] {
  display: table-cell;
  vertical-align: top
}


  


.text_abce10d4-25a2-46d5-a2e8-f823e4d712d2 {
  
  color: rgba(0, 0, 0, 1);
  
}



.text_abce10d4-25a2-46d5-a2e8-f823e4d712d2 { top: 1035.23px;left: 709.139px;width: 36px;height: 15.9408px;display: table;opacity: 1;font-size: 13px;position: absolute;text-align: left;font-family: Inter;font-weight: 500;line-height: normal;text-shadow: none;visibility: inherit;letter-spacing: -0.038461538461538464em;box-shadow: none;text-transform: normal;text-decoration: none; }.text_abce10d4-25a2-46d5-a2e8-f823e4d712d2 {
            left: -moz-calc(50% - 600px + 709.139px);
            left: -webkit-calc(50% - 600px + 709.139px);
            left: -o-calc(50% - 600px + 709.139px);
            left: calc(50% - 600px + 709.139px)
          }.text_f8c09f08-97d7-4880-b359-b0250541b8c4 [data-wysiwyg="true"] {
  display: table-cell;
  vertical-align: top
}


  


.text_f8c09f08-97d7-4880-b359-b0250541b8c4 {
  
  color: rgba(0, 0, 0, 1);
  
}



.text_f8c09f08-97d7-4880-b359-b0250541b8c4 { top: 1055.23px;left: 709.139px;width: 100px;height: 38.8557px;display: table;opacity: 1;font-size: 32px;position: absolute;text-align: left;font-family: Inter;font-weight: 700;line-height: normal;text-shadow: none;visibility: inherit;letter-spacing: -0.0625em;box-shadow: none;text-transform: normal;text-decoration: none; }.text_f8c09f08-97d7-4880-b359-b0250541b8c4 {
            left: -moz-calc(50% - 600px + 709.139px);
            left: -webkit-calc(50% - 600px + 709.139px);
            left: -o-calc(50% - 600px + 709.139px);
            left: calc(50% - 600px + 709.139px)
          }</style>
  
</div><div id="cd62cdd6-9852-4e46-a6b3-83149772e08e" class="group_cd62cdd6-9852-4e46-a6b3-83149772e08e" data-type="group">
  
      <div class="page-content__component text_0ca65177-2785-4336-885c-9d00760ee85c" data-container="grid" id="0ca65177-2785-4336-885c-9d00760ee85c" data-type="text"><div data-wysiwyg="true">4.2%</div></div><div class="page-content__component text_b670dfce-bf33-4e13-b141-b2c0cc4c7dba" data-container="grid" id="b670dfce-bf33-4e13-b141-b2c0cc4c7dba" data-type="text"><div data-wysiwyg="true">vs last week</div></div><div id="65511ea4-5088-4abd-b552-4a4dfc2509c9" class="group_65511ea4-5088-4abd-b552-4a4dfc2509c9" data-type="group">
  
      <div id="405db716-c319-4ab1-bf36-6fe066f048b2" class="group_405db716-c319-4ab1-bf36-6fe066f048b2" data-type="group">
  
      <div data-unit="px" data-container="grid" id="37b0a2ba-b4e0-45da-813b-fa58e1b87a0c" data-type="image" class="page-content__component image_37b0a2ba-b4e0-45da-813b-fa58e1b87a0c" style="background-image:url('https://cdn.siter.io/assets/ast_sSN8yQsvEEwrXQF9PDdPkR8QT/206c78a3-53e3-42bd-806c-3a527ba5e15b.svg');" data-bg="image">
  <div class="strw-shape"></div>
  
</div><style>.image_37b0a2ba-b4e0-45da-813b-fa58e1b87a0c:before {
  content: '';
  position: absolute;
  top:0;
  left: 0;
  right:0;
  bottom:0;

  background-image: -webkit-;
  background-image:    -moz-;
  background-image:     -ms-;
  background-image:      -o-;
  background-image:         ;
}.image_37b0a2ba-b4e0-45da-813b-fa58e1b87a0c { top: 1036.23px;left: 1188.48px;width: 14px;height: 13.9482px;opacity: 1;overflow: hidden;position: absolute;visibility: inherit;background-size: cover;background-image: none;background-repeat: no-repeat;background-position: center;box-shadow: none;border-radius: 0px 0px 0px 0px; }.image_37b0a2ba-b4e0-45da-813b-fa58e1b87a0c {
            left: -moz-calc(50% - 600px + 1188.48px);
            left: -webkit-calc(50% - 600px + 1188.48px);
            left: -o-calc(50% - 600px + 1188.48px);
            left: calc(50% - 600px + 1188.48px)
          }</style>
  
</div><style>.group_405db716-c319-4ab1-bf36-6fe066f048b2 { top: 0px;left: 0px;width: 100%;height: 0px;opacity: 1;position: absolute;visibility: inherit;background-color: transparent; }</style>
  
</div><style>.text_0ca65177-2785-4336-885c-9d00760ee85c [data-wysiwyg="true"] {
  display: table-cell;
  vertical-align: top
}


  


.text_0ca65177-2785-4336-885c-9d00760ee85c {
  
  color: rgba(0, 0, 0, 1);
  
}



.text_0ca65177-2785-4336-885c-9d00760ee85c { top: 1035.23px;left: 1153.14px;width: 32px;height: 16.9371px;display: table;opacity: 1;font-size: 14px;position: absolute;text-align: right;font-family: Inter;font-weight: 500;line-height: normal;text-shadow: none;visibility: inherit;letter-spacing: -0.03571428571428571em;box-shadow: none;text-transform: normal;text-decoration: none; }.text_0ca65177-2785-4336-885c-9d00760ee85c {
            left: -moz-calc(50% - 600px + 1153.14px);
            left: -webkit-calc(50% - 600px + 1153.14px);
            left: -o-calc(50% - 600px + 1153.14px);
            left: calc(50% - 600px + 1153.14px)
          }.text_b670dfce-bf33-4e13-b141-b2c0cc4c7dba [data-wysiwyg="true"] {
  display: table-cell;
  vertical-align: middle
}


  


.text_b670dfce-bf33-4e13-b141-b2c0cc4c7dba {
  
  color: rgba(178.00000458955765, 178.00000458955765, 178.00000458955765, 1);
  
}



.text_b670dfce-bf33-4e13-b141-b2c0cc4c7dba { top: 1055.23px;left: 1143.14px;width: 59px;height: 12.9519px;display: table;opacity: 1;font-size: 11px;position: absolute;text-align: left;font-family: Inter;font-weight: 400;line-height: normal;text-shadow: none;visibility: inherit;letter-spacing: -0.045454545454545456em;box-shadow: none;text-transform: normal;text-decoration: none; }.text_b670dfce-bf33-4e13-b141-b2c0cc4c7dba {
            left: -moz-calc(50% - 600px + 1143.14px);
            left: -webkit-calc(50% - 600px + 1143.14px);
            left: -o-calc(50% - 600px + 1143.14px);
            left: calc(50% - 600px + 1143.14px)
          }.group_65511ea4-5088-4abd-b552-4a4dfc2509c9 { top: 0px;left: 0px;width: 100%;height: 0px;opacity: 1;position: absolute;visibility: inherit;background-color: transparent; }</style>
  
</div><div id="8ce333d9-b31b-4260-bf44-d4fc2fcfb9f4" class="group_8ce333d9-b31b-4260-bf44-d4fc2fcfb9f4" data-type="group">
  
      <div id="759d3b2e-88b0-4653-8d63-0ff05d6bded0" class="group_759d3b2e-88b0-4653-8d63-0ff05d6bded0" data-type="group">
  
      <div id="bac4e43a-6abf-4b32-8844-ff069e250fe7" class="group_bac4e43a-6abf-4b32-8844-ff069e250fe7" data-type="group">
  
      <div data-unit="px" class="page-content__component rectangle_060537bf-609b-47aa-94d3-d13b91e17c9d" data-container="grid" id="060537bf-609b-47aa-94d3-d13b91e17c9d" data-type="rectangle">
  <div class="strw-shape"></div>
  
</div><div class="page-content__component text_b48c3c34-0b5c-4cb3-9cc0-201f5bda789e" data-container="grid" id="b48c3c34-0b5c-4cb3-9cc0-201f5bda789e" data-type="text"><div data-wysiwyg="true">+3,450</div></div><div class="page-content__component text_e5470a19-67c3-414e-ace7-6d0a3deaab00" data-container="grid" id="e5470a19-67c3-414e-ace7-6d0a3deaab00" data-type="text"><div data-wysiwyg="true">24.22</div></div><style>.rectangle_060537bf-609b-47aa-94d3-d13b91e17c9d .strw-shape {
  content: '';
  position: absolute;
  top:0;
  left: 0;
  right:0;
  bottom:0;
  background-image: -webkit-linear-gradient(to right, rgba(0, 0, 0, 1), rgba(0, 0, 0, 1));
  background-image:    -moz-linear-gradient(to right, rgba(0, 0, 0, 1), rgba(0, 0, 0, 1));
  background-image:     -ms-linear-gradient(to right, rgba(0, 0, 0, 1), rgba(0, 0, 0, 1));
  background-image:      -o-linear-gradient(to right, rgba(0, 0, 0, 1), rgba(0, 0, 0, 1));
  background-image:         linear-gradient(to right, rgba(0, 0, 0, 1), rgba(0, 0, 0, 1));
}

.rectangle_060537bf-609b-47aa-94d3-d13b91e17c9d:hover .strw-shape {
  
    opacity: 1;
    background-image: -webkit-;
    background-image:    -moz-;
    background-image:     -ms-;
    background-image:      -o-;
    background-image:         ;
  
}.rectangle_060537bf-609b-47aa-94d3-d13b91e17c9d { top: 1255.23px;left: 1024.91px;width: 63px;border: none;height: 38.8557px;opacity: 1;overflow: hidden;position: absolute;box-shadow: none;visibility: inherit;background-size: cover;background-repeat: no-repeat;background-position: center;border-radius: 4px 4px 4px 4px; }.rectangle_060537bf-609b-47aa-94d3-d13b91e17c9d {
            left: -moz-calc(50% - 600px + 1024.91px);
            left: -webkit-calc(50% - 600px + 1024.91px);
            left: -o-calc(50% - 600px + 1024.91px);
            left: calc(50% - 600px + 1024.91px)
          }.text_b48c3c34-0b5c-4cb3-9cc0-201f5bda789e [data-wysiwyg="true"] {
  display: table-cell;
  vertical-align: middle
}


  


.text_b48c3c34-0b5c-4cb3-9cc0-201f5bda789e {
  
  color: rgba(255, 255, 255, 1);
  
}



.text_b48c3c34-0b5c-4cb3-9cc0-201f5bda789e { top: 1259.23px;left: 1032.91px;width: 47px;height: 16.9371px;display: table;opacity: 1;font-size: 14px;position: absolute;text-align: right;font-family: Inter;font-weight: 500;line-height: normal;text-shadow: none;visibility: inherit;letter-spacing: -0.03571428571428571em;box-shadow: none;text-transform: normal;text-decoration: none; }.text_b48c3c34-0b5c-4cb3-9cc0-201f5bda789e {
            left: -moz-calc(50% - 600px + 1032.91px);
            left: -webkit-calc(50% - 600px + 1032.91px);
            left: -o-calc(50% - 600px + 1032.91px);
            left: calc(50% - 600px + 1032.91px)
          }.text_e5470a19-67c3-414e-ace7-6d0a3deaab00 [data-wysiwyg="true"] {
  display: table-cell;
  vertical-align: middle
}


  


.text_e5470a19-67c3-414e-ace7-6d0a3deaab00 {
  
  color: rgba(178.00000458955765, 178.00000458955765, 178.00000458955765, 1);
  
}



.text_e5470a19-67c3-414e-ace7-6d0a3deaab00 { top: 1276.23px;left: 1042.41px;width: 28px;height: 12.9519px;display: table;opacity: 1;font-size: 11px;position: absolute;text-align: left;font-family: Inter;font-weight: 400;line-height: normal;text-shadow: none;visibility: inherit;letter-spacing: -0.045454545454545456em;box-shadow: none;text-transform: normal;text-decoration: none; }.text_e5470a19-67c3-414e-ace7-6d0a3deaab00 {
            left: -moz-calc(50% - 600px + 1042.41px);
            left: -webkit-calc(50% - 600px + 1042.41px);
            left: -o-calc(50% - 600px + 1042.41px);
            left: calc(50% - 600px + 1042.41px)
          }</style>
  
</div><div data-unit="px" data-container="grid" id="b54a1b49-4989-4ffb-ada6-fdc35b2438ae" data-type="image" class="page-content__component image_b54a1b49-4989-4ffb-ada6-fdc35b2438ae" style="background-image:url('https://cdn.siter.io/assets/ast_napgrF7p1q6tzCi1bWprbdGrN/7b833dcb-db0e-4eb4-bc97-91e340fc4260.svg');" data-bg="image">
  <div class="strw-shape"></div>
  
</div><style>.group_bac4e43a-6abf-4b32-8844-ff069e250fe7 { top: 0px;left: 0px;width: 100%;height: 0px;opacity: 1;position: absolute;visibility: inherit;background-color: transparent; }.image_b54a1b49-4989-4ffb-ada6-fdc35b2438ae:before {
  content: '';
  position: absolute;
  top:0;
  left: 0;
  right:0;
  bottom:0;

  background-image: -webkit-;
  background-image:    -moz-;
  background-image:     -ms-;
  background-image:      -o-;
  background-image:         ;
}.image_b54a1b49-4989-4ffb-ada6-fdc35b2438ae { top: 1293.23px;left: 1056.41px;width: 2px;height: 41.8446px;opacity: 1;overflow: hidden;position: absolute;visibility: inherit;background-size: cover;background-image: none;background-repeat: no-repeat;background-position: center;box-shadow: none; }.image_b54a1b49-4989-4ffb-ada6-fdc35b2438ae {
            left: -moz-calc(50% - 600px + 1056.41px);
            left: -webkit-calc(50% - 600px + 1056.41px);
            left: -o-calc(50% - 600px + 1056.41px);
            left: calc(50% - 600px + 1056.41px)
          }</style>
  
</div><style>.group_759d3b2e-88b0-4653-8d63-0ff05d6bded0 { top: 0px;left: 0px;width: 100%;height: 0px;opacity: 1;position: absolute;visibility: inherit;background-color: transparent; }</style>
  
</div><style>.rectangle_97aee2fc-34be-4138-97a5-e382cb6f8eb6 .strw-shape {
  content: '';
  position: absolute;
  top:0;
  left: 0;
  right:0;
  bottom:0;
  background-image: -webkit-linear-gradient(to right, rgba(255, 255, 255, 1), rgba(255, 255, 255, 1));
  background-image:    -moz-linear-gradient(to right, rgba(255, 255, 255, 1), rgba(255, 255, 255, 1));
  background-image:     -ms-linear-gradient(to right, rgba(255, 255, 255, 1), rgba(255, 255, 255, 1));
  background-image:      -o-linear-gradient(to right, rgba(255, 255, 255, 1), rgba(255, 255, 255, 1));
  background-image:         linear-gradient(to right, rgba(255, 255, 255, 1), rgba(255, 255, 255, 1));
}

.rectangle_97aee2fc-34be-4138-97a5-e382cb6f8eb6:hover .strw-shape {
  
    opacity: 1;
    background-image: -webkit-;
    background-image:    -moz-;
    background-image:     -ms-;
    background-image:      -o-;
    background-image:         ;
  
}.rectangle_97aee2fc-34be-4138-97a5-e382cb6f8eb6 { top: 1015.23px;left: 693.139px;width: 526.369px;border: none;height: 464.162px;opacity: 1;overflow: hidden;position: absolute;box-shadow: none;visibility: inherit;background-size: cover;background-repeat: no-repeat;background-position: center;border-radius: 6px 6px 6px 6px; }.rectangle_97aee2fc-34be-4138-97a5-e382cb6f8eb6 {
            left: -moz-calc(50% - 600px + 693.139px);
            left: -webkit-calc(50% - 600px + 693.139px);
            left: -o-calc(50% - 600px + 693.139px);
            left: calc(50% - 600px + 693.139px)
          }.group_f6c4ff10-f003-4b6a-96f1-ab53642c562d { top: 0px;left: 0px;width: 100%;height: 0px;opacity: 1;position: absolute;visibility: inherit;background-color: transparent; }.group_d24decd6-261f-4b44-b3d0-701cf90a6639 { top: 0px;left: 0px;width: 100%;height: 0px;opacity: 1;position: absolute;visibility: inherit;background-color: transparent; }.group_cd62cdd6-9852-4e46-a6b3-83149772e08e { top: 0px;left: 0px;width: 100%;height: 0px;opacity: 1;position: absolute;visibility: inherit;background-color: transparent; }.group_8ce333d9-b31b-4260-bf44-d4fc2fcfb9f4 { top: 0px;left: 0px;width: 100%;height: 0px;opacity: 1;position: absolute;visibility: inherit;background-color: transparent; }</style>
  
</div><style>.rectangle_cc838662-cfe6-4a33-9bd9-5b57c8a00f55 .strw-shape {
  content: '';
  position: absolute;
  top:0;
  left: 0;
  right:0;
  bottom:0;
  background-image: -webkit-linear-gradient(to right, rgba(242, 243, 255, 1), rgba(242, 243, 255, 1));
  background-image:    -moz-linear-gradient(to right, rgba(242, 243, 255, 1), rgba(242, 243, 255, 1));
  background-image:     -ms-linear-gradient(to right, rgba(242, 243, 255, 1), rgba(242, 243, 255, 1));
  background-image:      -o-linear-gradient(to right, rgba(242, 243, 255, 1), rgba(242, 243, 255, 1));
  background-image:         linear-gradient(to right, rgba(242, 243, 255, 1), rgba(242, 243, 255, 1));
}

.rectangle_cc838662-cfe6-4a33-9bd9-5b57c8a00f55:hover .strw-shape {
  
    opacity: 1;
    background-image: -webkit-;
    background-image:    -moz-;
    background-image:     -ms-;
    background-image:      -o-;
    background-image:         ;
  
}.rectangle_cc838662-cfe6-4a33-9bd9-5b57c8a00f55 { top: 1031.23px;left: 708.669px;width: 514.927px;border: none;height: 439.733px;opacity: 1;overflow: hidden;position: absolute;box-shadow: none;visibility: inherit;background-size: cover;background-repeat: no-repeat;background-position: center;border-radius: 10px 10px 10px 10px; }.rectangle_cc838662-cfe6-4a33-9bd9-5b57c8a00f55 {
            left: -moz-calc(50% - 600px + 708.669px);
            left: -webkit-calc(50% - 600px + 708.669px);
            left: -o-calc(50% - 600px + 708.669px);
            left: calc(50% - 600px + 708.669px)
          }.group_048472ea-972a-41b6-b183-b92ffffbfe51 { top: 0px;left: 0px;width: 100%;height: 0px;opacity: 1;position: absolute;visibility: inherit;background-color: transparent; }</style>
  
</div><div id="00dec337-b0ea-4a7d-9151-27efb973fc56" class="group_00dec337-b0ea-4a7d-9151-27efb973fc56" data-type="group">
  
      <div class="page-content__component text_6bf43117-d1a6-4b60-a4bd-ec56cf31593e" data-container="grid" id="6bf43117-d1a6-4b60-a4bd-ec56cf31593e" data-type="text"><div data-wysiwyg="true">When you collect and analyze a lot of data, you can make effective decisions: make profitable videos  or modify the content.</div></div><div class="page-content__component text_29e24d34-b568-4783-8be0-0b8f385ea880" data-container="grid" id="29e24d34-b568-4783-8be0-0b8f385ea880" data-type="text"><div data-wysiwyg="true"><div style="vertical-align: top;" tab-index="3" text-content="true">Proper Analysis For Free!</div>

</div></div><style>.text_6bf43117-d1a6-4b60-a4bd-ec56cf31593e [data-wysiwyg="true"] {
  display: table-cell;
  vertical-align: top
}


  


.text_6bf43117-d1a6-4b60-a4bd-ec56cf31593e {
  
  color: rgba(0, 0, 0, 0.800000011920929);
  
}



.text_6bf43117-d1a6-4b60-a4bd-ec56cf31593e { top: 1221.23px;left: -40.8613px;width: 589px;height: 89.667px;display: table;opacity: 1;font-size: 21px;position: absolute;text-align: left;font-family: Inter;font-weight: 400;line-height: 30px;text-shadow: none;visibility: inherit;letter-spacing: -0.038095238662901376em;box-shadow: none;text-transform: normal;text-decoration: none; }.text_6bf43117-d1a6-4b60-a4bd-ec56cf31593e {
            left: -moz-calc(50% - 600px + -40.8613px);
            left: -webkit-calc(50% - 600px + -40.8613px);
            left: -o-calc(50% - 600px + -40.8613px);
            left: calc(50% - 600px + -40.8613px)
          }.text_29e24d34-b568-4783-8be0-0b8f385ea880 [data-wysiwyg="true"] {
  display: table-cell;
  vertical-align: top
}


  


.text_29e24d34-b568-4783-8be0-0b8f385ea880 {
  
  color: rgba(0, 0, 0, 1);
  
}



.text_29e24d34-b568-4783-8be0-0b8f385ea880 { top: 1106.23px;left: -48.8613px;width: 590px;height: 107.6px;display: table;opacity: 1;font-size: 48px;position: absolute;text-align: left;font-family: Inter;font-weight: 500;line-height: 54px;text-shadow: none;visibility: inherit;letter-spacing: -0.033333333830038704em;box-shadow: none;text-transform: normal;text-decoration: none; }.text_29e24d34-b568-4783-8be0-0b8f385ea880 {
            left: -moz-calc(50% - 600px + -48.8613px);
            left: -webkit-calc(50% - 600px + -48.8613px);
            left: -o-calc(50% - 600px + -48.8613px);
            left: calc(50% - 600px + -48.8613px)
          }</style>
  
</div><style>.group_3fad6432-d672-4b8d-8977-e69a509c3e8a { top: 0px;left: 0px;width: 100%;height: 0px;opacity: 1;position: absolute;visibility: inherit;background-color: transparent; }.group_00dec337-b0ea-4a7d-9151-27efb973fc56 { top: 0px;left: 0px;width: 100%;height: 0px;opacity: 1;position: absolute;visibility: inherit;background-color: transparent; }</style>
  
</div><div id="0099e32e-0230-425a-87e0-aef48d3e962a" class="group_0099e32e-0230-425a-87e0-aef48d3e962a" data-type="group">
  
      <div id="d003a67a-a005-4d02-83be-5b74b0e5fee8" class="group_d003a67a-a005-4d02-83be-5b74b0e5fee8" data-type="group">
  
      
  
</div><div id="3a4e8bca-169f-4091-8765-9fbb232917f8" class="group_3a4e8bca-169f-4091-8765-9fbb232917f8" data-type="group">
  
      <div id="5e2a410a-371d-4af7-b27a-f2dd46e4b2ff" class="group_5e2a410a-371d-4af7-b27a-f2dd46e4b2ff" data-type="group">
  
      <div data-unit="px" class="page-content__component rectangle_39791d5e-41b0-49c8-beef-00daa519bb23" data-container="grid" id="39791d5e-41b0-49c8-beef-00daa519bb23" data-type="rectangle">
  <div class="strw-shape"></div>
  
</div><style>.rectangle_39791d5e-41b0-49c8-beef-00daa519bb23 .strw-shape {
  content: '';
  position: absolute;
  top:0;
  left: 0;
  right:0;
  bottom:0;
  background-image: -webkit-linear-gradient(to right, rgba(0, 0, 0, 0.1), rgba(0, 0, 0, 0.1));
  background-image:    -moz-linear-gradient(to right, rgba(0, 0, 0, 0.1), rgba(0, 0, 0, 0.1));
  background-image:     -ms-linear-gradient(to right, rgba(0, 0, 0, 0.1), rgba(0, 0, 0, 0.1));
  background-image:      -o-linear-gradient(to right, rgba(0, 0, 0, 0.1), rgba(0, 0, 0, 0.1));
  background-image:         linear-gradient(to right, rgba(0, 0, 0, 0.1), rgba(0, 0, 0, 0.1));
}

.rectangle_39791d5e-41b0-49c8-beef-00daa519bb23:hover .strw-shape {
  
    opacity: 1;
    background-image: -webkit-;
    background-image:    -moz-;
    background-image:     -ms-;
    background-image:      -o-;
    background-image:         ;
  
}.rectangle_39791d5e-41b0-49c8-beef-00daa519bb23 { top: 90.2298px;left: -150.8506px;width: 1454px;border: none;height: 0.9963px;opacity: 1;overflow: hidden;position: absolute;box-shadow: none;visibility: inherit;background-size: cover;background-repeat: no-repeat;background-position: center;border-radius: 0px 0px 0px 0px; }.rectangle_39791d5e-41b0-49c8-beef-00daa519bb23 {
            left: -moz-calc(50% - 600px + -150.8506px);
            left: -webkit-calc(50% - 600px + -150.8506px);
            left: -o-calc(50% - 600px + -150.8506px);
            left: calc(50% - 600px + -150.8506px)
          }</style>
  
</div><div id="c81f8126-785b-41d6-b6ce-09d4b37c942d" class="group_c81f8126-785b-41d6-b6ce-09d4b37c942d" data-type="group">
  
      <div class="page-content__component text_73283844-f3a3-4b2b-aa70-a67ec9d5e1d9" data-container="grid" id="73283844-f3a3-4b2b-aa70-a67ec9d5e1d9" data-type="text"><div data-wysiwyg="true"><a href="#" class="str-link" data-close-click-outside="true" data-id="link-46480253-6364-47e1-8257-717befe41524" data-overlay-color="rgba(0, 0, 0, 0.2)" data-popup-position="center" data-type="page" style="font-family:Poppins;font-weight:700;color:inherit;font-size:inherit;" href="" data-cke-saved-href="" target="_blank">home</a></div></div></a></div></div><div class="page-content__component text_7059bb13-4c03-4496-8c61-44bba42a086d" data-container="grid" id="7059bb13-4c03-4496-8c61-44bba42a086d" data-type="text"><div data-wysiwyg="true"><a href="https://boost-io.vercel.app/privacy-policy" class="str-link" data-close-click-outside="true" data-id="link-46480253-6364-47e1-8257-717befe41524" data-overlay-color="rgba(0, 0, 0, 0.2)" data-popup-position="center" data-type="page" style="font-family:Poppins;font-weight:700;color:inherit;font-size:inherit;" href="" data-cke-saved-href="" target="_blank">privacy policy</a></div></div><style>.text_73283844-f3a3-4b2b-aa70-a67ec9d5e1d9 [data-wysiwyg="true"] {
  display: table-cell;
  vertical-align: middle
}


  


.text_73283844-f3a3-4b2b-aa70-a67ec9d5e1d9 {
  
  color: rgba(0, 0, 0, 1);
  
}



.text_73283844-f3a3-4b2b-aa70-a67ec9d5e1d9 { top: 42.2298px;left: 1042.15px;width: 47px;height: 17.9334px;display: table;opacity: 1;font-size: 16px;position: absolute;text-align: left;font-family: Poppins;font-weight: 700;line-height: 18px;text-shadow: none;visibility: inherit;letter-spacing: -0.03125em;box-shadow: none;text-transform: normal;text-decoration: none; }.text_73283844-f3a3-4b2b-aa70-a67ec9d5e1d9 {
            left: -moz-calc(50% - 600px + 1042.15px);
            left: -webkit-calc(50% - 600px + 1042.15px);
            left: -o-calc(50% - 600px + 1042.15px);
            left: calc(50% - 600px + 1042.15px)
          }.text_7059bb13-4c03-4496-8c61-44bba42a086d [data-wysiwyg="true"] {
  display: table-cell;
  vertical-align: middle
}


  


.text_7059bb13-4c03-4496-8c61-44bba42a086d {
  
  color: rgba(0, 0, 0, 1);
  
}



.text_7059bb13-4c03-4496-8c61-44bba42a086d { top: 42.2298px;left: 1119.15px;width: 111px;height: 17.9334px;display: table;opacity: 1;font-size: 16px;position: absolute;text-align: left;font-family: Poppins;font-weight: 700;line-height: 18px;text-shadow: none;visibility: inherit;letter-spacing: -0.03125em;box-shadow: none;text-transform: normal;text-decoration: none; }.text_7059bb13-4c03-4496-8c61-44bba42a086d {
            left: -moz-calc(50% - 600px + 1119.15px);
            left: -webkit-calc(50% - 600px + 1119.15px);
            left: -o-calc(50% - 600px + 1119.15px);
            left: calc(50% - 600px + 1119.15px)
          }</style>
  
</div><div class="page-content__component text_d21dc38e-cda3-4178-9409-9e8fb8838d70" data-container="grid" id="d21dc38e-cda3-4178-9409-9e8fb8838d70" data-type="text"><div data-wysiwyg="true">Boost</div></div><style>.group_5e2a410a-371d-4af7-b27a-f2dd46e4b2ff { top: 0px;left: 0px;width: 100%;height: 0px;opacity: 1;position: absolute;visibility: inherit;background-color: transparent; }.group_c81f8126-785b-41d6-b6ce-09d4b37c942d { top: 0px;left: 0px;width: 100%;height: 0px;opacity: 1;position: absolute;visibility: inherit;background-color: transparent; }.text_d21dc38e-cda3-4178-9409-9e8fb8838d70 [data-wysiwyg="true"] {
  display: table-cell;
  vertical-align: middle
}


  


.text_d21dc38e-cda3-4178-9409-9e8fb8838d70 {
  
  color: rgba(0, 0, 0, 1);
  
}



.text_d21dc38e-cda3-4178-9409-9e8fb8838d70 { top: 36.2298px;left: -24.850300000000004px;width: 88px;height: 29.889px;display: table;opacity: 1;font-size: 32px;position: absolute;text-align: left;font-family: Poppins;font-weight: 600;line-height: 30px;text-shadow: none;visibility: inherit;letter-spacing: -0.03125em;box-shadow: none;text-transform: normal;text-decoration: none; }.text_d21dc38e-cda3-4178-9409-9e8fb8838d70 {
            left: -moz-calc(50% - 600px + -24.850300000000004px);
            left: -webkit-calc(50% - 600px + -24.850300000000004px);
            left: -o-calc(50% - 600px + -24.850300000000004px);
            left: calc(50% - 600px + -24.850300000000004px)
          }</style>
  
</div><div id="c2a0b1a0-443d-49b5-aae8-81f97881cc79" class="group_c2a0b1a0-443d-49b5-aae8-81f97881cc79" data-type="group">
  
      <div id="bb343c05-5769-4f66-815a-3670efd376cb" class="group_bb343c05-5769-4f66-815a-3670efd376cb" data-type="group">
  
      <div class="page-content__component text_254ce6ac-a8ef-484f-9974-d3b33b078ef4" data-container="grid" id="254ce6ac-a8ef-484f-9974-d3b33b078ef4" data-type="text"><div data-wysiwyg="true">With Boost, you can get answers about what happened, why, and how to improve your results</div></div><div id="d5e7fed4-cc20-4c58-b05c-82cc69df5c3e" class="group_d5e7fed4-cc20-4c58-b05c-82cc69df5c3e" data-type="group">
  
      <div id="c655a7c0-a4df-45b3-ae99-81a1cfd310e6" class="group_c655a7c0-a4df-45b3-ae99-81a1cfd310e6" data-type="group">
  
      <div data-unit="px" class="page-content__component rectangle_4c222724-2789-41f4-ab91-970fa88079a1" data-container="grid" id="4c222724-2789-41f4-ab91-970fa88079a1" data-type="rectangle">
  <div class="strw-shape"></div>
  
</div><div id="a6adcb18-2a69-450c-9ea9-f96df8151df4" class="group_a6adcb18-2a69-450c-9ea9-f96df8151df4" data-type="group">
    <a>
    <div class="page-content__component text_a541682d-9b09-4331-8ddd-fd94cba4e154" data-container="grid" id="a541682d-9b09-4331-8ddd-fd94cba4e154" data-type="text"><div data-wysiwyg="true">Download For MacOS</div></div><style>.text_a541682d-9b09-4331-8ddd-fd94cba4e154 [data-wysiwyg="true"] {
  display: table-cell;
  vertical-align: middle
}


  


.text_a541682d-9b09-4331-8ddd-fd94cba4e154 {
  
  color: rgba(255, 255, 255, 1);
  
}



.text_a541682d-9b09-4331-8ddd-fd94cba4e154 { top: 593.23px;left: 278.813px;width: 181px;height: 19.926px;display: table;opacity: 1;font-size: 18px;position: absolute;text-align: left;font-family: Inter;font-weight: 500;line-height: 20px;text-shadow: none;visibility: inherit;letter-spacing: -0.016666667328940496em;box-shadow: none;text-transform: normal;text-decoration: none; }.text_a541682d-9b09-4331-8ddd-fd94cba4e154 {
            left: -moz-calc(50% - 600px + 278.813px);
            left: -webkit-calc(50% - 600px + 278.813px);
            left: -o-calc(50% - 600px + 278.813px);
            left: calc(50% - 600px + 278.813px)
          }</style>
</a>  
</div><style>.rectangle_4c222724-2789-41f4-ab91-970fa88079a1 .strw-shape {
  content: '';
  position: absolute;
  top:0;
  left: 0;
  right:0;
  bottom:0;
  background-image: -webkit-linear-gradient(to right, rgba(72, 95, 229, 1), rgba(72, 95, 229, 1));
  background-image:    -moz-linear-gradient(to right, rgba(72, 95, 229, 1), rgba(72, 95, 229, 1));
  background-image:     -ms-linear-gradient(to right, rgba(72, 95, 229, 1), rgba(72, 95, 229, 1));
  background-image:      -o-linear-gradient(to right, rgba(72, 95, 229, 1), rgba(72, 95, 229, 1));
  background-image:         linear-gradient(to right, rgba(72, 95, 229, 1), rgba(72, 95, 229, 1));
}

.rectangle_4c222724-2789-41f4-ab91-970fa88079a1:hover .strw-shape {
  
    opacity: 1;
    background-image: -webkit-;
    background-image:    -moz-;
    background-image:     -ms-;
    background-image:      -o-;
    background-image:         ;
  
}.rectangle_4c222724-2789-41f4-ab91-970fa88079a1 { top: 578.23px;left: 260.813px;width: 250px;border: none;height: 49.815px;opacity: 1;overflow: hidden;position: absolute;box-shadow: none;visibility: inherit;background-size: cover;background-repeat: no-repeat;background-position: center;border-radius: 10px 10px 10px 10px; }.rectangle_4c222724-2789-41f4-ab91-970fa88079a1 {
            left: -moz-calc(50% - 600px + 260.813px);
            left: -webkit-calc(50% - 600px + 260.813px);
            left: -o-calc(50% - 600px + 260.813px);
            left: calc(50% - 600px + 260.813px)
          }.group_a6adcb18-2a69-450c-9ea9-f96df8151df4 { top: 0px;left: 0px;width: 100%;height: 0px;opacity: 1;position: absolute;visibility: inherit;background-color: transparent; }</style>
  
</div><div data-unit="px" data-container="grid" id="1e7b9454-f019-4321-ad06-1639f8690898" data-type="image" class="page-content__component image_1e7b9454-f019-4321-ad06-1639f8690898" style="background-image:url('https://cdn.siter.io/assets/ast_6HD1m9cazKiAKYzZCWiYGtqkF/74582cd2-c887-4d8f-a6da-57bef4f194c3.svg');" data-bg="image">
  <div class="strw-shape"></div>
  
</div><style>.group_c655a7c0-a4df-45b3-ae99-81a1cfd310e6 { top: 0px;left: 0px;width: 100%;height: 0px;opacity: 1;position: absolute;visibility: inherit;background-color: transparent; }.image_1e7b9454-f019-4321-ad06-1639f8690898:before {
  content: '';
  position: absolute;
  top:0;
  left: 0;
  right:0;
  bottom:0;

  background-image: -webkit-;
  background-image:    -moz-;
  background-image:     -ms-;
  background-image:      -o-;
  background-image:         ;
}.image_1e7b9454-f019-4321-ad06-1639f8690898 { top: 230.23px;left: 407.913px;width: 17px;height: 8.9667px;opacity: 1;overflow: hidden;position: absolute;visibility: inherit;background-size: cover;background-image: none;background-repeat: no-repeat;background-position: center;box-shadow: none;border-radius: 0px 0px 0px 0px; }.image_1e7b9454-f019-4321-ad06-1639f8690898 {
            left: -moz-calc(50% - 600px + 407.913px);
            left: -webkit-calc(50% - 600px + 407.913px);
            left: -o-calc(50% - 600px + 407.913px);
            left: calc(50% - 600px + 407.913px)
          }</style>
  
</div><div id="7a5d0f12-6a5e-46ea-936c-90e08baf9b1c" class="group_7a5d0f12-6a5e-46ea-936c-90e08baf9b1c" data-type="group">
  
      <div id="add81e72-9315-439c-8b8b-439b0c701f5a" class="group_add81e72-9315-439c-8b8b-439b0c701f5a" data-type="group">
  
      <div data-unit="px" class="page-content__component rectangle_805364f1-d724-48d2-baa2-eb90c17e1a43" data-container="grid" id="805364f1-d724-48d2-baa2-eb90c17e1a43" data-type="rectangle">
  <div class="strw-shape"></div>
  
</div><div id="0dd43654-5ec1-4927-9742-f70e355e2796" class="group_0dd43654-5ec1-4927-9742-f70e355e2796" data-type="group">
        <a>
            <!-- For donwloaddddddddddddddddddddd -->

      <div class="page-content__component text_0ddac9fd-eb57-404f-ba9a-8aa75d27ea01" data-container="grid" id="0ddac9fd-eb57-404f-ba9a-8aa75d27ea01" data-type="text"><div data-wysiwyg="true">Download For Windows</div></div><style>.text_0ddac9fd-eb57-404f-ba9a-8aa75d27ea01 [data-wysiwyg="true"] {
  display: table-cell;
  vertical-align: middle
}


  


.text_0ddac9fd-eb57-404f-ba9a-8aa75d27ea01 {
  
  color: rgba(255, 255, 255, 1);
  
}



.text_0ddac9fd-eb57-404f-ba9a-8aa75d27ea01 { top: 592.23px;left: -3.1869999999999976px;width: 197px;height: 19.926px;display: table;opacity: 1;font-size: 18px;position: absolute;text-align: right;font-family: Inter;font-weight: 500;line-height: 20px;text-shadow: none;visibility: inherit;letter-spacing: -0.016666667328940496em;box-shadow: none;text-transform: normal;text-decoration: none; }.text_0ddac9fd-eb57-404f-ba9a-8aa75d27ea01 {
            left: -moz-calc(50% - 600px + -3.1869999999999976px);
            left: -webkit-calc(50% - 600px + -3.1869999999999976px);
            left: -o-calc(50% - 600px + -3.1869999999999976px);
            left: calc(50% - 600px + -3.1869999999999976px)
          }</style>
</a>
<!-- For donwloaddddddddddddddddddddd -->
</div><style>.rectangle_805364f1-d724-48d2-baa2-eb90c17e1a43 .strw-shape {
  content: '';
  position: absolute;
  top:0;
  left: 0;
  right:0;
  bottom:0;
  background-image: -webkit-linear-gradient(to right, rgba(72, 95, 229, 1), rgba(72, 95, 229, 1));
  background-image:    -moz-linear-gradient(to right, rgba(72, 95, 229, 1), rgba(72, 95, 229, 1));
  background-image:     -ms-linear-gradient(to right, rgba(72, 95, 229, 1), rgba(72, 95, 229, 1));
  background-image:      -o-linear-gradient(to right, rgba(72, 95, 229, 1), rgba(72, 95, 229, 1));
  background-image:         linear-gradient(to right, rgba(72, 95, 229, 1), rgba(72, 95, 229, 1));
}

.rectangle_805364f1-d724-48d2-baa2-eb90c17e1a43:hover .strw-shape {
  
    opacity: 1;
    background-image: -webkit-;
    background-image:    -moz-;
    background-image:     -ms-;
    background-image:      -o-;
    background-image:         ;
  
}.rectangle_805364f1-d724-48d2-baa2-eb90c17e1a43 { top: 577.23px;left: -21.187299999999993px;width: 266px;border: none;height: 49.815px;opacity: 1;overflow: hidden;position: absolute;box-shadow: none;visibility: inherit;background-size: cover;background-repeat: no-repeat;background-position: center;border-radius: 10px 10px 10px 10px; }.rectangle_805364f1-d724-48d2-baa2-eb90c17e1a43 {
            left: -moz-calc(50% - 600px + -21.187299999999993px);
            left: -webkit-calc(50% - 600px + -21.187299999999993px);
            left: -o-calc(50% - 600px + -21.187299999999993px);
            left: calc(50% - 600px + -21.187299999999993px)
          }.group_0dd43654-5ec1-4927-9742-f70e355e2796 { top: 0px;left: 0px;width: 100%;height: 0px;opacity: 1;position: absolute;visibility: inherit;background-color: transparent; }</style>
  
</div><div data-unit="px" data-container="grid" id="5be93940-3c10-4fed-9833-54e8038af9c1" data-type="image" class="page-content__component image_5be93940-3c10-4fed-9833-54e8038af9c1" style="background-image:url('https://cdn.siter.io/assets/ast_uXpwzJkmvwnycdV8yAqgnVC8s/c1d2fef6-a40e-4e15-9266-565dd6aeb403.svg');" data-bg="image">
  <div class="strw-shape"></div>
  
</div><style>.group_add81e72-9315-439c-8b8b-439b0c701f5a { top: 0px;left: 0px;width: 100%;height: 0px;opacity: 1;position: absolute;visibility: inherit;background-color: transparent; }.image_5be93940-3c10-4fed-9833-54e8038af9c1:before {
  content: '';
  position: absolute;
  top:0;
  left: 0;
  right:0;
  bottom:0;

  background-image: -webkit-;
  background-image:    -moz-;
  background-image:     -ms-;
  background-image:      -o-;
  background-image:         ;
}.image_5be93940-3c10-4fed-9833-54e8038af9c1 { top: 231.23px;left: 169.413px;width: 21px;height: 7.9704px;opacity: 1;overflow: hidden;position: absolute;visibility: inherit;background-size: cover;background-image: none;background-repeat: no-repeat;background-position: center;box-shadow: none;border-radius: 0px 0px 0px 0px; }.image_5be93940-3c10-4fed-9833-54e8038af9c1 {
            left: -moz-calc(50% - 600px + 169.413px);
            left: -webkit-calc(50% - 600px + 169.413px);
            left: -o-calc(50% - 600px + 169.413px);
            left: calc(50% - 600px + 169.413px)
          }</style>
  
</div><div class="page-content__component text_1bcb804a-194a-4f19-8f44-48839577b0dd" data-container="grid" id="1bcb804a-194a-4f19-8f44-48839577b0dd" data-type="text"><div data-wysiwyg="true">Analyze and improve your YouTube Channel in detail</div></div><style>.text_254ce6ac-a8ef-484f-9974-d3b33b078ef4 [data-wysiwyg="true"] {
  display: table-cell;
  vertical-align: top
}


  


.text_254ce6ac-a8ef-484f-9974-d3b33b078ef4 {
  
  color: rgba(0, 0, 0, 0.800000011920929);
  
}



.text_254ce6ac-a8ef-484f-9974-d3b33b078ef4 { top: 491.23px;left: -30.187299999999993px;width: 453px;height: 54.0848px;display: table;opacity: 1;font-size: 21px;position: absolute;text-align: left;font-family: Inter;font-weight: 400;line-height: 30px;text-shadow: none;visibility: inherit;letter-spacing: -0.038095238662901376em;box-shadow: none;text-transform: normal;text-decoration: none; }.text_254ce6ac-a8ef-484f-9974-d3b33b078ef4 {
            left: -moz-calc(50% - 600px + -30.187299999999993px);
            left: -webkit-calc(50% - 600px + -30.187299999999993px);
            left: -o-calc(50% - 600px + -30.187299999999993px);
            left: calc(50% - 600px + -30.187299999999993px)
          }.group_d5e7fed4-cc20-4c58-b05c-82cc69df5c3e { top: 0px;left: 0px;width: 100%;height: 0px;opacity: 1;position: absolute;visibility: inherit;background-color: transparent; }.group_7a5d0f12-6a5e-46ea-936c-90e08baf9b1c { top: 0px;left: 0px;width: 100%;height: 0px;opacity: 1;position: absolute;visibility: inherit;background-color: transparent; }.text_1bcb804a-194a-4f19-8f44-48839577b0dd [data-wysiwyg="true"] {
  display: table-cell;
  vertical-align: middle
}


  


.text_1bcb804a-194a-4f19-8f44-48839577b0dd {
  
  color: rgba(0, 0, 0, 1);
  
}



.text_1bcb804a-194a-4f19-8f44-48839577b0dd { top: 175.23px;left: -31.8613px;width: 563px;height: 193.804px;display: table;opacity: 1;font-size: 72px;position: absolute;text-align: left;font-family: Inter;font-weight: 500;line-height: 80px;text-shadow: none;visibility: inherit;letter-spacing: -0.05555555555555555em;box-shadow: none;text-transform: normal;text-decoration: none; }.text_1bcb804a-194a-4f19-8f44-48839577b0dd {
            left: -moz-calc(50% - 600px + -31.8613px);
            left: -webkit-calc(50% - 600px + -31.8613px);
            left: -o-calc(50% - 600px + -31.8613px);
            left: calc(50% - 600px + -31.8613px)
          }</style>
  
</div><style>.group_bb343c05-5769-4f66-815a-3670efd376cb { top: 0px;left: 0px;width: 100%;height: 0px;opacity: 1;position: absolute;visibility: inherit;background-color: transparent; }</style>
  
</div><style>.group_d003a67a-a005-4d02-83be-5b74b0e5fee8 { top: 0px;left: 0px;width: 100%;height: 0px;opacity: 1;position: absolute;visibility: inherit;background-color: transparent; }.group_3a4e8bca-169f-4091-8765-9fbb232917f8 { top: 0px;left: 0px;width: 100%;height: 0px;opacity: 1;position: absolute;visibility: inherit;background-color: transparent; }.group_c2a0b1a0-443d-49b5-aae8-81f97881cc79 { top: 0px;left: 0px;width: 100%;height: 0px;opacity: 1;position: absolute;visibility: inherit;background-color: transparent; }</style>
  
</div><div id="622be72c-b9a4-4531-9291-61985618201e" class="group_622be72c-b9a4-4531-9291-61985618201e" data-type="group">
  
      <div id="4e38aa29-59be-44be-8f18-0661491da5a1" class="group_4e38aa29-59be-44be-8f18-0661491da5a1" data-type="group">
  
      <div class="page-content__component text_e610b575-c5f2-4575-bc74-f3f6709e1dc4" data-container="grid" id="e610b575-c5f2-4575-bc74-f3f6709e1dc4" data-type="text"><div data-wysiwyg="true">Get Noticed</div></div><div id="2b5793cd-b7e8-4f5c-be4d-99de04e00145" class="group_2b5793cd-b7e8-4f5c-be4d-99de04e00145" data-type="group">
  
      <div id="1641a432-c76f-4116-bc3d-3ffa377df384" class="group_1641a432-c76f-4116-bc3d-3ffa377df384" data-type="group">
  
      <div data-unit="px" data-container="grid" id="806ebd5c-00c0-4922-9f98-30fabee1b985" data-type="image" class="page-content__component image_806ebd5c-00c0-4922-9f98-30fabee1b985" style="background-image:url('https://cdn.siter.io/assets/ast_gdm4XUMA8RLt19JyouNzFAWKq/0e15cb48-e1cd-4a7e-96d5-8a7c0a9ab920.svg');" data-bg="image">
  <div class="strw-shape"></div>
  
</div><style>.image_806ebd5c-00c0-4922-9f98-30fabee1b985:before {
  content: '';
  position: absolute;
  top:0;
  left: 0;
  right:0;
  bottom:0;

  background-image: -webkit-;
  background-image:    -moz-;
  background-image:     -ms-;
  background-image:      -o-;
  background-image:         ;
}.image_806ebd5c-00c0-4922-9f98-30fabee1b985 { top: 840.23px;left: 606.7px;width: 34px;height: 31.8816px;opacity: 1;overflow: hidden;position: absolute;visibility: inherit;background-size: cover;background-image: none;background-repeat: no-repeat;background-position: center;box-shadow: none;border-radius: 0px 0px 0px 0px; }.image_806ebd5c-00c0-4922-9f98-30fabee1b985 {
            left: -moz-calc(50% - 600px + 606.7px);
            left: -webkit-calc(50% - 600px + 606.7px);
            left: -o-calc(50% - 600px + 606.7px);
            left: calc(50% - 600px + 606.7px)
          }</style>
  
</div><style>.group_1641a432-c76f-4116-bc3d-3ffa377df384 { top: 0px;left: 0px;width: 100%;height: 0px;opacity: 1;position: absolute;visibility: inherit;background-color: transparent; }</style>
  
</div><style>.text_e610b575-c5f2-4575-bc74-f3f6709e1dc4 [data-wysiwyg="true"] {
  display: table-cell;
  vertical-align: top
}


  


.text_e610b575-c5f2-4575-bc74-f3f6709e1dc4 {
  
  color: rgba(0, 0, 0, 1);
  
}



.text_e610b575-c5f2-4575-bc74-f3f6709e1dc4 { top: 795.23px;left: 559.139px;width: 301px;height: 29.889px;display: table;opacity: 1;font-size: 24px;position: absolute;text-align: left;font-family: Inter;font-weight: 500;line-height: 30px;text-shadow: none;visibility: inherit;letter-spacing: -0.041666666666666664em;box-shadow: none;text-transform: normal;text-decoration: none; }.text_e610b575-c5f2-4575-bc74-f3f6709e1dc4 {
            left: -moz-calc(50% - 600px + 559.139px);
            left: -webkit-calc(50% - 600px + 559.139px);
            left: -o-calc(50% - 600px + 559.139px);
            left: calc(50% - 600px + 559.139px)
          }.group_2b5793cd-b7e8-4f5c-be4d-99de04e00145 { top: 0px;left: 0px;width: 100%;height: 0px;opacity: 1;position: absolute;visibility: inherit;background-color: transparent; }</style>
  
</div><div id="843d0c9e-9efc-4a37-98b4-05614a975363" class="group_843d0c9e-9efc-4a37-98b4-05614a975363" data-type="group">
  
      <div class="page-content__component text_4bb9709b-cbd3-4471-ba33-c26232ba37e7" data-container="grid" id="4bb9709b-cbd3-4471-ba33-c26232ba37e7" data-type="text"><div data-wysiwyg="true">Repeat</div></div><div id="75bf153a-a1cf-4694-959c-822dd0d73404" class="group_75bf153a-a1cf-4694-959c-822dd0d73404" data-type="group">
  
      
  
</div><style>.text_4bb9709b-cbd3-4471-ba33-c26232ba37e7 [data-wysiwyg="true"] {
  display: table-cell;
  vertical-align: top
}


  


.text_4bb9709b-cbd3-4471-ba33-c26232ba37e7 {
  
  color: rgba(0, 0, 0, 1);
  
}



.text_4bb9709b-cbd3-4471-ba33-c26232ba37e7 { top: 739.23px;left: 1034.14px;width: 301px;height: 29.889px;display: table;opacity: 1;font-size: 24px;position: absolute;text-align: left;font-family: Inter;font-weight: 500;line-height: 30px;text-shadow: none;visibility: inherit;letter-spacing: -0.041666666666666664em;box-shadow: none;text-transform: normal;text-decoration: none; }.text_4bb9709b-cbd3-4471-ba33-c26232ba37e7 {
            left: -moz-calc(50% - 600px + 1034.14px);
            left: -webkit-calc(50% - 600px + 1034.14px);
            left: -o-calc(50% - 600px + 1034.14px);
            left: calc(50% - 600px + 1034.14px)
          }.group_75bf153a-a1cf-4694-959c-822dd0d73404 { top: 0px;left: 0px;width: 100%;height: 0px;opacity: 1;position: absolute;visibility: inherit;background-color: transparent; }</style>
  
</div><div id="90e6e193-d3e4-43c4-8806-99341d1f5e5d" class="group_90e6e193-d3e4-43c4-8806-99341d1f5e5d" data-type="group">
  
      <div class="page-content__component text_1ab00897-375a-4f89-a038-9d2a0ac98f41" data-container="grid" id="1ab00897-375a-4f89-a038-9d2a0ac98f41" data-type="text"><div data-wysiwyg="true">Create New Content</div></div><div id="96670e77-0022-4753-b18d-05bc76b5bdd8" class="group_96670e77-0022-4753-b18d-05bc76b5bdd8" data-type="group">
  
      <div id="025fab16-f3b6-4c28-8494-76c64756d557" class="group_025fab16-f3b6-4c28-8494-76c64756d557" data-type="group">
  
      <div data-unit="px" data-container="grid" id="168462d1-7bba-4c74-8dfb-a5a1ea3a4176" data-type="image" class="page-content__component image_168462d1-7bba-4c74-8dfb-a5a1ea3a4176" style="background-image:url('https://cdn.siter.io/assets/ast_HWVzpQa57qoqDo3Vv5MLQnqKW/ee88c622-eb66-4d39-92e0-17147dfb80eb.svg');" data-bg="image">
  <div class="strw-shape"></div>
  
</div><div data-unit="px" data-container="grid" id="dbcbcc7d-7bc0-48c9-8b3a-c97a899e95a3" data-type="image" class="page-content__component image_dbcbcc7d-7bc0-48c9-8b3a-c97a899e95a3" style="background-image:url('https://cdn.siter.io/assets/ast_CMkZMY9XMQTtHVwE1a9vUg3Sv/506340d7-aba9-4817-948b-7478f89bcc5e.svg');" data-bg="image">
  <div class="strw-shape"></div>
  
</div><style>.image_168462d1-7bba-4c74-8dfb-a5a1ea3a4176:before {
  content: '';
  position: absolute;
  top:0;
  left: 0;
  right:0;
  bottom:0;

  background-image: -webkit-;
  background-image:    -moz-;
  background-image:     -ms-;
  background-image:      -o-;
  background-image:         ;
}.image_168462d1-7bba-4c74-8dfb-a5a1ea3a4176 { top: 792.23px;left: 79.827px;width: 18px;height: 3.9852px;opacity: 1;overflow: hidden;position: absolute;visibility: inherit;background-size: cover;background-image: none;background-repeat: no-repeat;background-position: center;box-shadow: none;border-radius: 0px 0px 0px 0px; }.image_168462d1-7bba-4c74-8dfb-a5a1ea3a4176 {
            left: -moz-calc(50% - 600px + 79.827px);
            left: -webkit-calc(50% - 600px + 79.827px);
            left: -o-calc(50% - 600px + 79.827px);
            left: calc(50% - 600px + 79.827px)
          }.image_dbcbcc7d-7bc0-48c9-8b3a-c97a899e95a3:before {
  content: '';
  position: absolute;
  top:0;
  left: 0;
  right:0;
  bottom:0;

  background-image: -webkit-;
  background-image:    -moz-;
  background-image:     -ms-;
  background-image:      -o-;
  background-image:         ;
}.image_dbcbcc7d-7bc0-48c9-8b3a-c97a899e95a3 { top: 779.23px;left: 73.38499999999999px;width: 30px;height: 30.8853px;opacity: 1;overflow: hidden;position: absolute;visibility: inherit;background-size: cover;background-image: none;background-repeat: no-repeat;background-position: center;box-shadow: none;border-radius: 0px 0px 0px 0px; }.image_dbcbcc7d-7bc0-48c9-8b3a-c97a899e95a3 {
            left: -moz-calc(50% - 600px + 73.38499999999999px);
            left: -webkit-calc(50% - 600px + 73.38499999999999px);
            left: -o-calc(50% - 600px + 73.38499999999999px);
            left: calc(50% - 600px + 73.38499999999999px)
          }</style>
  
</div><style>.group_025fab16-f3b6-4c28-8494-76c64756d557 { top: 0px;left: 0px;width: 100%;height: 0px;opacity: 1;position: absolute;visibility: inherit;background-color: transparent; }</style>
  
</div><style>.text_1ab00897-375a-4f89-a038-9d2a0ac98f41 [data-wysiwyg="true"] {
  display: table-cell;
  vertical-align: top
}


  


.text_1ab00897-375a-4f89-a038-9d2a0ac98f41 {
  
  color: rgba(0, 0, 0, 1);
  
}



.text_1ab00897-375a-4f89-a038-9d2a0ac98f41 { top: 734.23px;left: -18.861000000000004px;width: 301px;height: 29.889px;display: table;opacity: 1;font-size: 24px;position: absolute;text-align: left;font-family: Inter;font-weight: 500;line-height: 30px;text-shadow: none;visibility: inherit;letter-spacing: -0.041666666666666664em;box-shadow: none;text-transform: normal;text-decoration: none; }.text_1ab00897-375a-4f89-a038-9d2a0ac98f41 {
            left: -moz-calc(50% - 600px + -18.861000000000004px);
            left: -webkit-calc(50% - 600px + -18.861000000000004px);
            left: -o-calc(50% - 600px + -18.861000000000004px);
            left: calc(50% - 600px + -18.861000000000004px)
          }.group_96670e77-0022-4753-b18d-05bc76b5bdd8 { top: 0px;left: 0px;width: 100%;height: 0px;opacity: 1;position: absolute;visibility: inherit;background-color: transparent; }</style>
  
</div><style>.group_4e38aa29-59be-44be-8f18-0661491da5a1 { top: 0px;left: 0px;width: 100%;height: 0px;opacity: 1;position: absolute;visibility: inherit;background-color: transparent; }.group_843d0c9e-9efc-4a37-98b4-05614a975363 { top: 0px;left: 0px;width: 100%;height: 0px;opacity: 1;position: absolute;visibility: inherit;background-color: transparent; }.group_90e6e193-d3e4-43c4-8806-99341d1f5e5d { top: 0px;left: 0px;width: 100%;height: 0px;opacity: 1;position: absolute;visibility: inherit;background-color: transparent; }</style>
  
</div><div id="1440a04f-0be9-4cee-ba44-fa3e27338ec6" class="group_1440a04f-0be9-4cee-ba44-fa3e27338ec6" data-type="group">
  
      <div data-unit="px" data-container="grid" id="8924cf74-9d90-4533-9e8a-1faca9b97357" data-type="image" class="page-content__component image_8924cf74-9d90-4533-9e8a-1faca9b97357" style="background-image:url('https://cdn.siter.io/assets/ast_eQUinqLbdj2N1hqbPBxGatcZW/bb17bf89-2607-483d-8429-6d50d8840f54.svg');" data-bg="image">
  <div class="strw-shape"></div>
  
</div><div data-unit="px" data-container="grid" id="2713ba85-f2f5-4967-840d-31b1e7e4a12b" data-type="image" class="page-content__component image_2713ba85-f2f5-4967-840d-31b1e7e4a12b" style="background-image:url('https://cdn.siter.io/assets/ast_v1uRHVmJ4v4twjh3P28L8Tcvc/f255916e-ef01-4790-80d3-600f1bce3970.svg');" data-bg="image">
  <div class="strw-shape"></div>
  
</div><div data-unit="px" data-container="grid" id="628cf418-0619-4961-af2a-d5ce89a5b5f6" data-type="image" class="page-content__component image_628cf418-0619-4961-af2a-d5ce89a5b5f6" style="background-image:url('https://cdn.siter.io/assets/ast_uxqobMG3yx6DNjRLmNFmFxn68/e0962c97-3189-4e34-aa8e-969fa1b35c34.svg');" data-bg="image">
  <div class="strw-shape"></div>
  
</div><style>.image_8924cf74-9d90-4533-9e8a-1faca9b97357:before {
  content: '';
  position: absolute;
  top:0;
  left: 0;
  right:0;
  bottom:0;

  background-image: -webkit-;
  background-image:    -moz-;
  background-image:     -ms-;
  background-image:      -o-;
  background-image:         ;
}.image_8924cf74-9d90-4533-9e8a-1faca9b97357 { top: 290.23px;left: 997.28px;width: 28px;height: 8.9667px;opacity: 1;overflow: hidden;position: absolute;visibility: inherit;background-size: cover;background-image: none;background-repeat: no-repeat;background-position: center;box-shadow: none;border-radius: 0px 0px 0px 0px; }.image_8924cf74-9d90-4533-9e8a-1faca9b97357 {
            left: -moz-calc(50% - 600px + 997.28px);
            left: -webkit-calc(50% - 600px + 997.28px);
            left: -o-calc(50% - 600px + 997.28px);
            left: calc(50% - 600px + 997.28px)
          }.image_2713ba85-f2f5-4967-840d-31b1e7e4a12b:before {
  content: '';
  position: absolute;
  top:0;
  left: 0;
  right:0;
  bottom:0;

  background-image: -webkit-;
  background-image:    -moz-;
  background-image:     -ms-;
  background-image:      -o-;
  background-image:         ;
}.image_2713ba85-f2f5-4967-840d-31b1e7e4a12b { top: 297.23px;left: 996.3399999999999px;width: 30px;height: 4.9815px;opacity: 1;overflow: hidden;position: absolute;visibility: inherit;background-size: cover;background-image: none;background-repeat: no-repeat;background-position: center;box-shadow: none;border-radius: 0px 0px 0px 0px; }.image_2713ba85-f2f5-4967-840d-31b1e7e4a12b {
            left: -moz-calc(50% - 600px + 996.3399999999999px);
            left: -webkit-calc(50% - 600px + 996.3399999999999px);
            left: -o-calc(50% - 600px + 996.3399999999999px);
            left: calc(50% - 600px + 996.3399999999999px)
          }.image_628cf418-0619-4961-af2a-d5ce89a5b5f6:before {
  content: '';
  position: absolute;
  top:0;
  left: 0;
  right:0;
  bottom:0;

  background-image: -webkit-;
  background-image:    -moz-;
  background-image:     -ms-;
  background-image:      -o-;
  background-image:         ;
}.image_628cf418-0619-4961-af2a-d5ce89a5b5f6 { top: 299.23px;left: 996.3399999999999px;width: 30px;height: 4.9815px;opacity: 1;overflow: hidden;position: absolute;visibility: inherit;background-size: cover;background-image: none;background-repeat: no-repeat;background-position: center;box-shadow: none;border-radius: 0px 0px 0px 0px; }.image_628cf418-0619-4961-af2a-d5ce89a5b5f6 {
            left: -moz-calc(50% - 600px + 996.3399999999999px);
            left: -webkit-calc(50% - 600px + 996.3399999999999px);
            left: -o-calc(50% - 600px + 996.3399999999999px);
            left: calc(50% - 600px + 996.3399999999999px)
          }</style>
  
</div><div data-unit="px" data-container="grid" id="d72c6b76-fbef-4206-bedd-4bbd731495d6" data-type="image" class="page-content__component image_d72c6b76-fbef-4206-bedd-4bbd731495d6" style="background-image:url('https://cdn.siter.io/assets/ast_nP3HD5vrwb6CTjK9N2NN4RxJ8/cce9b36d-fbfb-43af-b745-0a28e7a02ecf.svg');" data-bg="image">
  <div class="strw-shape"></div>
  
</div><div data-unit="px" data-container="grid" id="5ac3d3f3-8f97-4fd8-a832-68f1f9cd2b16" data-type="image" class="page-content__component image_5ac3d3f3-8f97-4fd8-a832-68f1f9cd2b16" style="background-image:url('https://cdn.siter.io/assets/ast_6jS5YuDqe17PaXYSZWmjRv4jN/844c25e8-a549-4f37-8a6e-5935265ee172.svg');" data-bg="image">
  <div class="strw-shape"></div>
  
</div><div data-unit="px" data-container="grid" id="3c37802c-dcf0-4ef0-a8e7-a9a225e33976" data-type="image" class="page-content__component image_3c37802c-dcf0-4ef0-a8e7-a9a225e33976" style="background-image:url('https://cdn.siter.io/assets/ast_Sz9zSJveFVgf58X8KiT6NKCYG/7100d6be-ce19-430c-bfbe-5c718a5e8acb.svg');" data-bg="image">
  <div class="strw-shape"></div>
  
</div><div data-unit="px" data-container="grid" id="75e7aa9f-9331-4b62-be23-a1c72c6aa1e3" data-type="image" class="page-content__component image_75e7aa9f-9331-4b62-be23-a1c72c6aa1e3" style="background-image:url('https://cdn.siter.io/assets/ast_dCkx3TWjbf5Jk2zDWWQJ1os2p/401ab768-fa1c-4f28-98ee-1ec4ed2cdc0b.svg');" data-bg="image">
  <div class="strw-shape"></div>
  
</div><div data-unit="px" data-container="grid" id="b5fbb8d7-39e9-437c-b323-42ab9c61824d" data-type="image" class="page-content__component image_b5fbb8d7-39e9-437c-b323-42ab9c61824d" style="background-image:url('https://cdn.siter.io/assets/ast_oGZwWNbAoCymxy5jT4gRDGmQg/bf15d986-bf76-48e1-982a-2ef02f50f8cd.svg');" data-bg="image">
  <div class="strw-shape"></div>
  
</div><div id="db3bdcff-1782-409f-9073-c83b16b1ca0c" class="group_db3bdcff-1782-409f-9073-c83b16b1ca0c" data-type="group">
  
      <div data-unit="px" class="page-content__component rectangle_bcbfa59a-4d51-4a6c-b670-f3472616b172" data-container="grid" id="bcbfa59a-4d51-4a6c-b670-f3472616b172" data-type="rectangle">
  <div class="strw-shape"></div>
  
</div><div id="f73d5a38-596d-47a1-ac13-e89b3144cb7b" class="group_f73d5a38-596d-47a1-ac13-e89b3144cb7b" data-type="group">
  
      
  
</div><style>.rectangle_bcbfa59a-4d51-4a6c-b670-f3472616b172 .strw-shape {
  content: '';
  position: absolute;
  top:0;
  left: 0;
  right:0;
  bottom:0;
  background-image: -webkit-linear-gradient(to right, rgba(0, 0, 0, 1), rgba(0, 0, 0, 1));
  background-image:    -moz-linear-gradient(to right, rgba(0, 0, 0, 1), rgba(0, 0, 0, 1));
  background-image:     -ms-linear-gradient(to right, rgba(0, 0, 0, 1), rgba(0, 0, 0, 1));
  background-image:      -o-linear-gradient(to right, rgba(0, 0, 0, 1), rgba(0, 0, 0, 1));
  background-image:         linear-gradient(to right, rgba(0, 0, 0, 1), rgba(0, 0, 0, 1));
}

.rectangle_bcbfa59a-4d51-4a6c-b670-f3472616b172:hover .strw-shape {
  
    opacity: 1;
    background-image: -webkit-;
    background-image:    -moz-;
    background-image:     -ms-;
    background-image:      -o-;
    background-image:         ;
  
}.rectangle_bcbfa59a-4d51-4a6c-b670-f3472616b172 { top: 2130px;left: -401px;width: 1911.46px;border: none;height: 187.82px;opacity: 1;overflow: hidden;position: absolute;box-shadow: none;visibility: inherit;background-size: cover;background-repeat: no-repeat;background-position: center;border-radius: 0px 0px 0px 0px; }.rectangle_bcbfa59a-4d51-4a6c-b670-f3472616b172 {
            left: -moz-calc(50% - 600px + -401px);
            left: -webkit-calc(50% - 600px + -401px);
            left: -o-calc(50% - 600px + -401px);
            left: calc(50% - 600px + -401px)
          }.group_f73d5a38-596d-47a1-ac13-e89b3144cb7b { top: 0px;left: 0px;width: 100%;height: 0px;opacity: 1;position: absolute;visibility: inherit;background-color: transparent; }</style>
  
</div><div id="d6481b03-13d6-4fda-be3b-929a2d5c0127" class="group_d6481b03-13d6-4fda-be3b-929a2d5c0127" data-type="group">
  
      <div class="page-content__component text_8775a9a2-3a83-40f6-bc93-747bb2ecaafc" data-container="grid" id="8775a9a2-3a83-40f6-bc93-747bb2ecaafc" data-type="text"><div data-wysiwyg="true">BOOST</div></div><div class="page-content__component text_0f2fde8f-2e8f-4532-a2b0-a5acfd96b515" data-container="grid" id="0f2fde8f-2e8f-4532-a2b0-a5acfd96b515" data-type="text"><div data-wysiwyg="true">Contact Us
codingprojects2018@gmail.com</div></div><div class="page-content__component text_c5b6770b-6b79-43a5-b0ac-6e1947d9f45c" data-container="grid" id="c5b6770b-6b79-43a5-b0ac-6e1947d9f45c" data-type="text"><div data-wysiwyg="true"><a href="#" class="str-link" data-close-click-outside="true" data-id="link-46480253-6364-47e1-8257-717befe41524" data-overlay-color="rgba(0, 0, 0, 0.2)" data-popup-position="center" data-type="page" style="font-family:Poppins;font-weight:700;color:inherit;font-size:inherit;" href="" data-cke-saved-href="" target="_blank">home</a></div></div><div class="page-content__component text_41985c3d-672d-4d81-acfb-a37a7d262788" data-container="grid" id="41985c3d-672d-4d81-acfb-a37a7d262788" data-type="text"><div data-wysiwyg="true"><a href="/privacy-policy" class="str-link" data-close-click-outside="true" data-id="link-46480253-6364-47e1-8257-717befe41524" data-overlay-color="rgba(0, 0, 0, 0.2)" data-popup-position="center" data-type="page" style="font-family:Poppins;font-weight:700;color:inherit;font-size:inherit;" href="" data-cke-saved-href="" target="_blank">privacy policy</a></div></div><style>.text_8775a9a2-3a83-40f6-bc93-747bb2ecaafc [data-wysiwyg="true"] {
  display: table-cell;
  vertical-align: top
}

  


.text_8775a9a2-3a83-40f6-bc93-747bb2ecaafc {
  
  color: rgba(255, 255, 255, 1);
  
}



.text_8775a9a2-3a83-40f6-bc93-747bb2ecaafc { top: 2178.0375727600194px;left: -4.505631131406201px;width: 444px;height: 44.8744px;display: table;opacity: 1;font-size: 64px;position: absolute;text-align: left;font-family: Poppins;font-weight: 700;line-height: 75px;text-shadow: none;visibility: inherit;letter-spacing: -0.005208333333333333em;box-shadow: none;text-transform: normal;text-decoration: none; }.text_8775a9a2-3a83-40f6-bc93-747bb2ecaafc {
            left: -moz-calc(50% - 600px + -4.505631131406201px);
            left: -webkit-calc(50% - 600px + -4.505631131406201px);
            left: -o-calc(50% - 600px + -4.505631131406201px);
            left: calc(50% - 600px + -4.505631131406201px)
          }.text_0f2fde8f-2e8f-4532-a2b0-a5acfd96b515 [data-wysiwyg="true"] {
  display: table-cell;
  vertical-align: top
}


  


.text_0f2fde8f-2e8f-4532-a2b0-a5acfd96b515 {
  
  color: rgba(255, 255, 255, 1);
  
}



.text_0f2fde8f-2e8f-4532-a2b0-a5acfd96b515 { top: 2184.0375727600194px;left: 336.4943688685938px;width: 534.358px;height: 89.667px;display: table;opacity: 1;font-size: 32px;position: absolute;text-align: left;font-family: Poppins;font-weight: 400;line-height: 30px;text-shadow: none;visibility: inherit;letter-spacing: -0.015625em;box-shadow: none;text-transform: normal;text-decoration: none; }.text_0f2fde8f-2e8f-4532-a2b0-a5acfd96b515 {
            left: -moz-calc(50% - 600px + 336.4943688685938px);
            left: -webkit-calc(50% - 600px + 336.4943688685938px);
            left: -o-calc(50% - 600px + 336.4943688685938px);
            left: calc(50% - 600px + 336.4943688685938px)
          }.text_c5b6770b-6b79-43a5-b0ac-6e1947d9f45c [data-wysiwyg="true"] {
  display: table-cell;
  vertical-align: top
}


  


.text_c5b6770b-6b79-43a5-b0ac-6e1947d9f45c {
  
  color: rgba(255, 255, 255, 1);
  
}



.text_c5b6770b-6b79-43a5-b0ac-6e1947d9f45c { top: 2175.0375727600194px;left: 1007.4943688685938px;width: 71px;height: 29.889px;display: table;opacity: 1;font-size: 24px;position: absolute;text-align: left;font-family: Poppins;font-weight: 700;line-height: 30px;text-shadow: none;visibility: inherit;letter-spacing: -0.020833333333333332em;box-shadow: none;text-transform: normal;text-decoration: none; }.text_c5b6770b-6b79-43a5-b0ac-6e1947d9f45c {
            left: -moz-calc(50% - 600px + 1007.4943688685938px);
            left: -webkit-calc(50% - 600px + 1007.4943688685938px);
            left: -o-calc(50% - 600px + 1007.4943688685938px);
            left: calc(50% - 600px + 1007.4943688685938px)
          }.text_41985c3d-672d-4d81-acfb-a37a7d262788 [data-wysiwyg="true"] {
  display: table-cell;
  vertical-align: top
}


  


.text_41985c3d-672d-4d81-acfb-a37a7d262788 {
  
  color: rgba(255, 255, 255, 1);
  
}



.text_41985c3d-672d-4d81-acfb-a37a7d262788 { top: 2208.0375727600194px;left: 1007.4943688685938px;width: 169px;height: 29.889px;display: table;opacity: 1;font-size: 24px;position: absolute;text-align: left;font-family: Poppins;font-weight: 700;line-height: 30px;text-shadow: none;visibility: inherit;letter-spacing: -0.020833333333333332em;box-shadow: none;text-transform: normal;text-decoration: none; }.text_41985c3d-672d-4d81-acfb-a37a7d262788 {
            left: -moz-calc(50% - 600px + 1007.4943688685938px);
            left: -webkit-calc(50% - 600px + 1007.4943688685938px);
            left: -o-calc(50% - 600px + 1007.4943688685938px);
            left: calc(50% - 600px + 1007.4943688685938px)
          }</style>
  
</div><div id="99acbf94-3969-4a93-a13c-2ab7b7d57002" class="group_99acbf94-3969-4a93-a13c-2ab7b7d57002" data-type="group">
  
      <div data-unit="px" class="page-content__component rectangle_28a7094a-1ead-4612-a193-8e8f83ba6cd9" data-container="grid" id="28a7094a-1ead-4612-a193-8e8f83ba6cd9" data-type="rectangle">
  <div class="strw-shape"></div>
  
</div><style>.rectangle_28a7094a-1ead-4612-a193-8e8f83ba6cd9 .strw-shape {
  content: '';
  position: absolute;
  top:0;
  left: 0;
  right:0;
  bottom:0;
  background-image: -webkit-linear-gradient(to right, rgba(0, 0, 0, 0), rgba(0, 0, 0, 0));
  background-image:    -moz-linear-gradient(to right, rgba(0, 0, 0, 0), rgba(0, 0, 0, 0));
  background-image:     -ms-linear-gradient(to right, rgba(0, 0, 0, 0), rgba(0, 0, 0, 0));
  background-image:      -o-linear-gradient(to right, rgba(0, 0, 0, 0), rgba(0, 0, 0, 0));
  background-image:         linear-gradient(to right, rgba(0, 0, 0, 0), rgba(0, 0, 0, 0));
}

.rectangle_28a7094a-1ead-4612-a193-8e8f83ba6cd9:hover .strw-shape {
  
    opacity: 1;
    background-image: -webkit-;
    background-image:    -moz-;
    background-image:     -ms-;
    background-image:      -o-;
    background-image:         ;
  
}.rectangle_28a7094a-1ead-4612-a193-8e8f83ba6cd9 { top: 738.23px;left: 489.139px;width: 25px;border: none;height: 24.9075px;opacity: 1;overflow: hidden;position: absolute;box-shadow: none;visibility: inherit;background-size: cover;background-repeat: no-repeat;background-position: center;border-radius: 0px 0px 0px 0px; }.rectangle_28a7094a-1ead-4612-a193-8e8f83ba6cd9 {
            left: -moz-calc(50% - 600px + 489.139px);
            left: -webkit-calc(50% - 600px + 489.139px);
            left: -o-calc(50% - 600px + 489.139px);
            left: calc(50% - 600px + 489.139px)
          }</style>
  
</div><div id="44863d38-1c6f-48ce-88e8-20aa823b6421" class="group_44863d38-1c6f-48ce-88e8-20aa823b6421" data-type="group">
  
      <div data-unit="px" class="page-content__component rectangle_ae93a2f2-4216-4be6-b5a4-424c5a378574" data-container="grid" id="ae93a2f2-4216-4be6-b5a4-424c5a378574" data-type="rectangle">
  <div class="strw-shape"></div>
  
</div><style>.rectangle_ae93a2f2-4216-4be6-b5a4-424c5a378574 .strw-shape {
  content: '';
  position: absolute;
  top:0;
  left: 0;
  right:0;
  bottom:0;
  background-image: -webkit-linear-gradient(to right, rgba(0, 0, 0, 0), rgba(0, 0, 0, 0));
  background-image:    -moz-linear-gradient(to right, rgba(0, 0, 0, 0), rgba(0, 0, 0, 0));
  background-image:     -ms-linear-gradient(to right, rgba(0, 0, 0, 0), rgba(0, 0, 0, 0));
  background-image:      -o-linear-gradient(to right, rgba(0, 0, 0, 0), rgba(0, 0, 0, 0));
  background-image:         linear-gradient(to right, rgba(0, 0, 0, 0), rgba(0, 0, 0, 0));
}

.rectangle_ae93a2f2-4216-4be6-b5a4-424c5a378574:hover .strw-shape {
  
    opacity: 1;
    background-image: -webkit-;
    background-image:    -moz-;
    background-image:     -ms-;
    background-image:      -o-;
    background-image:         ;
  
}.rectangle_ae93a2f2-4216-4be6-b5a4-424c5a378574 { top: 679.23px;left: 282.139px;width: 50px;border: none;height: 49.815px;opacity: 1;overflow: hidden;position: absolute;box-shadow: none;visibility: inherit;background-size: cover;background-repeat: no-repeat;background-position: center;border-radius: 0px 0px 0px 0px; }.rectangle_ae93a2f2-4216-4be6-b5a4-424c5a378574 {
            left: -moz-calc(50% - 600px + 282.139px);
            left: -webkit-calc(50% - 600px + 282.139px);
            left: -o-calc(50% - 600px + 282.139px);
            left: calc(50% - 600px + 282.139px)
          }</style>
  
</div><div data-unit="px" data-container="grid" id="a423caca-47b2-4ae2-8903-3bceb5b0f950" data-type="image" class="page-content__component image_a423caca-47b2-4ae2-8903-3bceb5b0f950" style="background-image:url('https://cdn.siter.io/assets/ast_tEJ2BY3msfvuoryQFe5z2bLn2/5a3ea3cf-c142-468c-854f-fe4ae7eff97e.svg');" data-bg="image">
  <div class="strw-shape"></div>
  
</div><div id="8df90d31-ca6f-424a-b478-20e70baa70b0" class="group_8df90d31-ca6f-424a-b478-20e70baa70b0" data-type="group">
  
      <div data-unit="px" class="page-content__component rectangle_a6de30eb-474f-475c-96bb-384a32d7daa6" data-container="grid" id="a6de30eb-474f-475c-96bb-384a32d7daa6" data-type="rectangle">
  <div class="strw-shape"></div>
  
</div><div data-unit="px" data-container="grid" id="a15a9195-be68-4e52-b3d0-e607d40032dd" data-type="image" class="page-content__component image_a15a9195-be68-4e52-b3d0-e607d40032dd" style="background-image:url('https://cdn.siter.io/assets/ast_mrnzL6vAU5d24QSTRYkBMVpDr/be756387-9ccf-49c2-9709-e96d4086c16b.svg');" data-bg="image">
  <div class="strw-shape"></div>
  
</div><style>.rectangle_a6de30eb-474f-475c-96bb-384a32d7daa6 .strw-shape {
  content: '';
  position: absolute;
  top:0;
  left: 0;
  right:0;
  bottom:0;
  background-image: -webkit-linear-gradient(to right, rgba(255, 255, 255, 0), rgba(255, 255, 255, 0));
  background-image:    -moz-linear-gradient(to right, rgba(255, 255, 255, 0), rgba(255, 255, 255, 0));
  background-image:     -ms-linear-gradient(to right, rgba(255, 255, 255, 0), rgba(255, 255, 255, 0));
  background-image:      -o-linear-gradient(to right, rgba(255, 255, 255, 0), rgba(255, 255, 255, 0));
  background-image:         linear-gradient(to right, rgba(255, 255, 255, 0), rgba(255, 255, 255, 0));
}

.rectangle_a6de30eb-474f-475c-96bb-384a32d7daa6:hover .strw-shape {
  
    opacity: 1;
    background-image: -webkit-;
    background-image:    -moz-;
    background-image:     -ms-;
    background-image:      -o-;
    background-image:         ;
  
}.rectangle_a6de30eb-474f-475c-96bb-384a32d7daa6 { top: 584.23px;left: 463.273px;width: 30px;border: none;height: 29.889px;opacity: 1;overflow: hidden;position: absolute;box-shadow: none;visibility: inherit;background-size: cover;background-repeat: no-repeat;background-position: center;border-radius: 0px 0px 0px 0px; }.rectangle_a6de30eb-474f-475c-96bb-384a32d7daa6 {
            left: -moz-calc(50% - 600px + 463.273px);
            left: -webkit-calc(50% - 600px + 463.273px);
            left: -o-calc(50% - 600px + 463.273px);
            left: calc(50% - 600px + 463.273px)
          }.image_a15a9195-be68-4e52-b3d0-e607d40032dd:before {
  content: '';
  position: absolute;
  top:0;
  left: 0;
  right:0;
  bottom:0;

  background-image: -webkit-;
  background-image:    -moz-;
  background-image:     -ms-;
  background-image:      -o-;
  background-image:         ;
}.image_a15a9195-be68-4e52-b3d0-e607d40032dd { top: 586.23px;left: 467.25699999999995px;width: 28px;height: 29.889px;opacity: 1;overflow: hidden;position: absolute;visibility: inherit;background-size: cover;background-image: none;background-repeat: no-repeat;background-position: center;box-shadow: none;border-radius: 0px 0px 0px 0px; }.image_a15a9195-be68-4e52-b3d0-e607d40032dd {
            left: -moz-calc(50% - 600px + 467.25699999999995px);
            left: -webkit-calc(50% - 600px + 467.25699999999995px);
            left: -o-calc(50% - 600px + 467.25699999999995px);
            left: calc(50% - 600px + 467.25699999999995px)
          }</style>
  
</div><style>.group_634b87a8-190a-4783-a5ab-89a2c719b6cb { top: 0px;left: 0px;width: 100%;height: 0px;opacity: 1;position: absolute;visibility: inherit;background-color: transparent; }.group_f05805d9-d324-4615-b4ba-1596188c2c7c { top: 0px;left: 0px;width: 100%;height: 0px;opacity: 1;position: absolute;visibility: inherit;background-color: transparent; }.group_0099e32e-0230-425a-87e0-aef48d3e962a { top: 0px;left: 0px;width: 100%;height: 0px;opacity: 1;position: absolute;visibility: inherit;background-color: transparent; }.group_622be72c-b9a4-4531-9291-61985618201e { top: 0px;left: 0px;width: 100%;height: 0px;opacity: 1;position: absolute;visibility: inherit;background-color: transparent; }.group_1440a04f-0be9-4cee-ba44-fa3e27338ec6 { top: 0px;left: 0px;width: 100%;height: 0px;opacity: 1;position: absolute;visibility: inherit;background-color: transparent; }.image_d72c6b76-fbef-4206-bedd-4bbd731495d6:before {
  content: '';
  position: absolute;
  top:0;
  left: 0;
  right:0;
  bottom:0;

  background-image: -webkit-;
  background-image:    -moz-;
  background-image:     -ms-;
  background-image:      -o-;
  background-image:         ;
}.image_d72c6b76-fbef-4206-bedd-4bbd731495d6 { top: 135.23px;left: 608.439px;width: 593px;height: 494.165px;opacity: 1;overflow: hidden;position: absolute;visibility: inherit;background-size: cover;background-image: none;background-repeat: no-repeat;background-position: center;box-shadow: none; }.image_d72c6b76-fbef-4206-bedd-4bbd731495d6 {
            left: -moz-calc(50% - 600px + 608.439px);
            left: -webkit-calc(50% - 600px + 608.439px);
            left: -o-calc(50% - 600px + 608.439px);
            left: calc(50% - 600px + 608.439px)
          }.image_5ac3d3f3-8f97-4fd8-a832-68f1f9cd2b16:before {
  content: '';
  position: absolute;
  top:0;
  left: 0;
  right:0;
  bottom:0;

  background-image: -webkit-;
  background-image:    -moz-;
  background-image:     -ms-;
  background-image:      -o-;
  background-image:         ;
}.image_5ac3d3f3-8f97-4fd8-a832-68f1f9cd2b16 { top: 739.23px;left: 198.139px;width: 434px;height: 148.449px;opacity: 1;overflow: hidden;position: absolute;visibility: inherit;background-size: cover;background-image: none;background-repeat: no-repeat;background-position: center;box-shadow: none;border-radius: 0px 0px 0px 0px; }.image_5ac3d3f3-8f97-4fd8-a832-68f1f9cd2b16 {
            left: -moz-calc(50% - 600px + 198.139px);
            left: -webkit-calc(50% - 600px + 198.139px);
            left: -o-calc(50% - 600px + 198.139px);
            left: calc(50% - 600px + 198.139px)
          }.image_3c37802c-dcf0-4ef0-a8e7-a9a225e33976:before {
  content: '';
  position: absolute;
  top:0;
  left: 0;
  right:0;
  bottom:0;

  background-image: -webkit-;
  background-image:    -moz-;
  background-image:     -ms-;
  background-image:      -o-;
  background-image:         ;
}.image_3c37802c-dcf0-4ef0-a8e7-a9a225e33976 { top: 731.23px;left: 648.139px;width: 397.21px;height: 71.7564px;opacity: 1;overflow: hidden;position: absolute;visibility: inherit;background-size: cover;background-image: none;background-repeat: no-repeat;background-position: center;box-shadow: none;border-radius: 0px 0px 0px 0px; }.image_3c37802c-dcf0-4ef0-a8e7-a9a225e33976 {
            left: -moz-calc(50% - 600px + 648.139px);
            left: -webkit-calc(50% - 600px + 648.139px);
            left: -o-calc(50% - 600px + 648.139px);
            left: calc(50% - 600px + 648.139px)
          }.image_75e7aa9f-9331-4b62-be23-a1c72c6aa1e3:before {
  content: '';
  position: absolute;
  top:0;
  left: 0;
  right:0;
  bottom:0;

  background-image: -webkit-;
  background-image:    -moz-;
  background-image:     -ms-;
  background-image:      -o-;
  background-image:         ;
}.image_75e7aa9f-9331-4b62-be23-a1c72c6aa1e3 { top: 760.23px;left: -322.824px;width: 379.963px;height: 84.323px;opacity: 1;overflow: hidden;position: absolute;visibility: inherit;background-size: cover;background-image: none;background-repeat: no-repeat;background-position: center;box-shadow: none;border-radius: 0px 0px 0px 0px; }.image_75e7aa9f-9331-4b62-be23-a1c72c6aa1e3 {
            left: -moz-calc(50% - 600px + -322.824px);
            left: -webkit-calc(50% - 600px + -322.824px);
            left: -o-calc(50% - 600px + -322.824px);
            left: calc(50% - 600px + -322.824px)
          }.image_b5fbb8d7-39e9-437c-b323-42ab9c61824d:before {
  content: '';
  position: absolute;
  top:0;
  left: 0;
  right:0;
  bottom:0;

  background-image: -webkit-;
  background-image:    -moz-;
  background-image:     -ms-;
  background-image:      -o-;
  background-image:         ;
}.image_b5fbb8d7-39e9-437c-b323-42ab9c61824d { top: 755.23px;left: 1102.14px;width: 425.364px;height: 75.1885px;opacity: 1;overflow: hidden;position: absolute;visibility: inherit;background-size: cover;background-image: none;background-repeat: no-repeat;background-position: center;box-shadow: none;border-radius: 0px 0px 0px 0px; }.image_b5fbb8d7-39e9-437c-b323-42ab9c61824d {
            left: -moz-calc(50% - 600px + 1102.14px);
            left: -webkit-calc(50% - 600px + 1102.14px);
            left: -o-calc(50% - 600px + 1102.14px);
            left: calc(50% - 600px + 1102.14px)
          }.group_db3bdcff-1782-409f-9073-c83b16b1ca0c { top: 0px;left: 0px;width: 100%;height: 0px;opacity: 1;position: absolute;visibility: inherit;background-color: transparent; }.group_d6481b03-13d6-4fda-be3b-929a2d5c0127 { top: 0px;left: 0px;width: 100%;height: 0px;opacity: 1;position: absolute;visibility: inherit;background-color: transparent; }.group_99acbf94-3969-4a93-a13c-2ab7b7d57002 { top: 0px;left: 0px;width: 100%;height: 0px;opacity: 1;position: absolute;visibility: inherit;background-color: transparent; }.group_44863d38-1c6f-48ce-88e8-20aa823b6421 { top: 0px;left: 0px;width: 100%;height: 0px;opacity: 1;position: absolute;visibility: inherit;background-color: transparent; }.image_a423caca-47b2-4ae2-8903-3bceb5b0f950:before {
  content: '';
  position: absolute;
  top:0;
  left: 0;
  right:0;
  bottom:0;

  background-image: -webkit-;
  background-image:    -moz-;
  background-image:     -ms-;
  background-image:      -o-;
  background-image:         ;
}.image_a423caca-47b2-4ae2-8903-3bceb5b0f950 { top: 589.23px;left: 203.139px;width: 28px;height: 29.889px;opacity: 1;overflow: hidden;position: absolute;visibility: inherit;background-size: cover;background-image: none;background-repeat: no-repeat;background-position: center;box-shadow: none;border-radius: 0px 0px 0px 0px; }.image_a423caca-47b2-4ae2-8903-3bceb5b0f950 {
            left: -moz-calc(50% - 600px + 203.139px);
            left: -webkit-calc(50% - 600px + 203.139px);
            left: -o-calc(50% - 600px + 203.139px);
            left: calc(50% - 600px + 203.139px)
          }.group_8df90d31-ca6f-424a-b478-20e70baa70b0 { top: 0px;left: 0px;width: 100%;height: 0px;opacity: 1;position: absolute;visibility: inherit;background-color: transparent; }</style>
  
</div><div data-unit="px" data-container="grid" id="f35c3140-80b7-4f53-a4cf-9fb5ecb3c816" data-type="image" class="page-content__component image_f35c3140-80b7-4f53-a4cf-9fb5ecb3c816" style="background-image:url('https://cdn.siter.io/assets/ast_HrMofpgtVDAFeryqhfFXUTSeC/e8ff8da0-2dd2-4f1c-b5c2-c30c7dd2d5ae.webp');" data-bg="image">
  <div class="strw-shape"></div>
  
</div><div data-unit="px" class="page-content__component rectangle_3ab8b264-1327-4e92-b8c5-51ef1d153949" data-container="grid" id="3ab8b264-1327-4e92-b8c5-51ef1d153949" data-type="rectangle">
  <div class="strw-shape"></div>
  
</div><style>.group_9ed0bc87-8f7b-4401-8ff7-4dab05ba6627 { top: 0px;left: 0px;width: 100%;height: 0px;opacity: 1;position: absolute;visibility: inherit;background-color: transparent; }.image_f35c3140-80b7-4f53-a4cf-9fb5ecb3c816:before {
  content: '';
  position: absolute;
  top:0;
  left: 0;
  right:0;
  bottom:0;

  background-image: -webkit-;
  background-image:    -moz-;
  background-image:     -ms-;
  background-image:      -o-;
  background-image:         ;
}.image_f35c3140-80b7-4f53-a4cf-9fb5ecb3c816 { top: 786px;left: 1087px;width: 33.1215px;height: 23.4485px;opacity: 1;overflow: hidden;position: absolute;visibility: inherit;background-size: cover;background-image: none;background-repeat: no-repeat;background-position: center; }.image_f35c3140-80b7-4f53-a4cf-9fb5ecb3c816 {
            left: -moz-calc(50% - 600px + 1087px);
            left: -webkit-calc(50% - 600px + 1087px);
            left: -o-calc(50% - 600px + 1087px);
            left: calc(50% - 600px + 1087px)
          }.rectangle_3ab8b264-1327-4e92-b8c5-51ef1d153949 .strw-shape {
  content: '';
  position: absolute;
  top:0;
  left: 0;
  right:0;
  bottom:0;
  background-image: -webkit-linear-gradient(to right, rgba(255, 255, 255, 1), rgba(255, 255, 255, 1));
  background-image:    -moz-linear-gradient(to right, rgba(255, 255, 255, 1), rgba(255, 255, 255, 1));
  background-image:     -ms-linear-gradient(to right, rgba(255, 255, 255, 1), rgba(255, 255, 255, 1));
  background-image:      -o-linear-gradient(to right, rgba(255, 255, 255, 1), rgba(255, 255, 255, 1));
  background-image:         linear-gradient(to right, rgba(255, 255, 255, 1), rgba(255, 255, 255, 1));
}

.rectangle_3ab8b264-1327-4e92-b8c5-51ef1d153949:hover .strw-shape {
  
    opacity: 1;
    background-image: -webkit-;
    background-image:    -moz-;
    background-image:     -ms-;
    background-image:      -o-;
    background-image:         ;
  
}.rectangle_3ab8b264-1327-4e92-b8c5-51ef1d153949 { top: 1848px;left: 34px;width: 296px;border: none;height: 0px;opacity: 1;overflow: hidden;position: absolute;box-shadow: none;visibility: inherit;background-size: cover;background-repeat: no-repeat;background-position: center; }.rectangle_3ab8b264-1327-4e92-b8c5-51ef1d153949 {
            left: -moz-calc(50% - 600px + 34px);
            left: -webkit-calc(50% - 600px + 34px);
            left: -o-calc(50% - 600px + 34px);
            left: calc(50% - 600px + 34px)
          }</style><style>.page_pg_Hxy1AtxR8qrL1HTaXF6THWM7P { height: 2309.067893939363px; }.page_pg_Hxy1AtxR8qrL1HTaXF6THWM7P:after {
  background-image: -webkit-linear-gradient(to right, rgba(255, 255, 255, 1), rgba(255, 255, 255, 1));
  background-image:    -moz-linear-gradient(to right, rgba(255, 255, 255, 1), rgba(255, 255, 255, 1));
  background-image:     -ms-linear-gradient(to right, rgba(255, 255, 255, 1), rgba(255, 255, 255, 1));
  background-image:      -o-linear-gradient(to right, rgba(255, 255, 255, 1), rgba(255, 255, 255, 1));
  background-image:         linear-gradient(to right, rgba(255, 255, 255, 1), rgba(255, 255, 255, 1));
  background-size: cover;
}

.page_pg_Hxy1AtxR8qrL1HTaXF6THWM7P {
  background-repeat: no-repeat;
  background-position: top center;
  background-size: cover;
}</style></div> <div class="page-content__inner-fixed" id="page-content-fixed" style="transform: scale(1);"></div> </div> <div class="notification-container" style="display: none"> <span> <div class="notification"> <svg onclick="EditorPageWidgets.notifyHide()" width="16" height="16" viewBox="0 0 16 16" fill="none" xmlns="http://www.w3.org/2000/svg" style="position: absolute; top: 20px; right: 22px;"> <g opacity="0.5"> <path d="M15 1L1 15" stroke="#333333"></path> <path d="M1 1L15 15" stroke="#333333"></path> </g> </svg> <div class="notification-message" role="alert"> <h4 class="title"></h4> <div class="message"></div> </div> </div> </span> </div> </div> <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script> <script src="https://www.youtube.com/iframe_api"></script> <script src="https://player.vimeo.com/api/player.js"></script> <script src="https://maps.googleapis.com/maps/api/js?key=AIzaSyDrutUSPfjuwC8b4W9pitclowi3btRQkMo&amp;v=3.exp&amp;libraries=geometry,drawing,places,directions"></script> <link rel="stylesheet" href="https://api.siter.io/assets/magnific-popup-2f7f85183333c84a42262b5f8a4f8251958809e29fa31c65bdee53c4603502cd.css"> <script src="https://api.siter.io/assets/magnific-popup.min-37130bcc3f8b01fe7473f8bb60a9aea35dc77c05eedc37fbd70135363feb6999.js"></script> <script src="https://api.siter.io/assets/swiper.min-d36969d50f8c2fa3a00a68e55fe929e3af3fdd249cf33fd128b6a17a410e2c59.js"></script> <link rel="stylesheet" href="https://api.siter.io/assets/swiper-18be8aa3f032dded246a45a9da3dafdb3934e39e1f1b3b623c1722f3152b2788.css"> <script src="https://api.siter.io/assets/application-ad7d1058a4f8521663fc8298179979c36f417a211a3974b6793461b077d824f1.js"></script> </body></html>
    '''

@app.route('/privacy-policy/')
def policy():
    return """
    <html class="wf-poppins-n8-active wf-poppins-n4-active wf-poppins-n6-active wf-poppins-n7-active wf-inter-n5-active wf-inter-n1-active wf-inter-n6-active wf-inter-n4-active wf-inter-n8-active wf-inter-n2-active wf-inter-n7-active wf-inter-n3-active wf-poppins-n2-active wf-poppins-n1-active wf-poppins-n3-active wf-poppins-n5-active wf-active"><head> <meta charset="utf-8"> <title>privacy policy</title> <meta content="width=1240, initial-scale=0" name="viewport"> <meta name="description" content=""> <meta property="og:type" content="article"> <meta property="og:title" content="privacy policy"> <meta property="og:description" content=""> <meta property="og:image" content="https://s3.us-east-1.amazonaws.com/cdn-siter/41e2e4ab-defc-404d-b92f-77421b81f2c0-url_og_image.png"> <meta property="twitter:card" content="summary_large_image"> <meta property="twitter:title" content="privacy policy"> <meta property="twitter:description" content=""> <meta property="twitter:image" content="https://s3.us-east-1.amazonaws.com/cdn-siter/41e2e4ab-defc-404d-b92f-77421b81f2c0-url_og_image.png"> <script type="text/javascript" id="www-widgetapi-script" src="https://www.youtube.com/s/player/23604418/www-widgetapi.vflset/www-widgetapi.js" async=""></script><script type="text/javascript" id="variables">
      window.devices = {
        mobile: false,
        tablet: false
      }
      window.site_id = 'boostio-1688456519347'
      window.page_id = 'pg_n2prXkLTBBAugZnXyddEPLx3W'
      window.pages = [{"path":"boostio","id":"pg_Hxy1AtxR8qrL1HTaXF6THWM7P","home":true},{"path":"privacy-policy","id":"pg_n2prXkLTBBAugZnXyddEPLx3W","home":false}];
      window.preview = true;
    </script> <link rel="stylesheet" media="screen" href="https://api.siter.io/assets/application-4024ba90e1f34a0be61507b2881bf775b48256845135858801ad3db2ab8f89e2.css"><link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Inter:100,200,300,400,500,600,700,800%7CPoppins:100,200,300,400,500,600,700,800" media="all"> <script type="text/javascript" charset="UTF-8" src="https://maps.googleapis.com/maps-api-v3/api/js/53/8/common.js"></script><script type="text/javascript" charset="UTF-8" src="https://maps.googleapis.com/maps-api-v3/api/js/53/8/util.js"></script></head><body> <div class="siter-page page_pg_n2prXkLTBBAugZnXyddEPLx3W"> <div class="page-content"> <div class="page-content__inner" id="page-content" style="transform: scale(1) translateZ(0px);"><div data-unit="px" class="page-content__component rectangle_5b03ba2f-4cae-4e1e-b19a-cb7603423eb6" data-container="grid" id="5b03ba2f-4cae-4e1e-b19a-cb7603423eb6" data-type="rectangle">
  <div class="strw-shape"></div>
  
</div><div class="page-content__component text_9cf57baa-bf2c-4d69-947d-1df794f7a6a4" data-container="grid" id="9cf57baa-bf2c-4d69-947d-1df794f7a6a4" data-type="text"><div data-wysiwyg="true">privacy policy</div></div><div class="page-content__component text_18eb6772-845f-487e-a512-884cf896e99b" data-container="grid" id="18eb6772-845f-487e-a512-884cf896e99b" data-type="text"><div data-wysiwyg="true">At Boost, we are committed to protecting the privacy and security of your personal information. This Privacy Policy outlines how we collect, use, disclose, and safeguard your information when you use our services. By accessing or using Boost, you consent to the terms outlined in this Privacy Policy.<br>
<span style="-webkit-background-clip:text !important;font-weight:600;">1. Information We Collect</span><br>
Personal Information: We may collect personal information such as your name, email address, contact details, and any other information you voluntarily provide to us.<br>
Usage Information: We may collect information about your Youtube channel<br>
Cookies and Similar Technologies: We use cookies and similar technologies to enhance your experience, gather information about usage patterns, and track website analytics.<br>
<span style="-webkit-background-clip:text !important;font-weight:600;">2. How We Use Your Information</span><br>
Provide and Improve Services: We use your information to provide, maintain, and improve our services, customize your experience, and respond to your inquiries or requests.<br>
Communication: We may use your contact information to send you updates, newsletters, promotional materials, and other communications related to Boost. You can opt-out of these communications at any time.<br>
Analytics and Aggregated Data: We may use anonymized and aggregated data for research, analytics, and reporting purposes.<br>
<span style="-webkit-background-clip:text !important;font-weight:600;">3. How We Share Your Information</span><br>
Service Providers: We may share your information with trusted third-party service providers who assist us in delivering our services, such as hosting providers or analytics tools.<br>
Legal Requirements: We may disclose your information if required by law, regulation, legal process, or governmental request.<br>
Business Transfers: In the event of a merger, acquisition, or sale of assets, your information may be transferred as part of the transaction. We will notify you of any such change and provide options regarding your information.<br>
<span style="-webkit-background-clip:text !important;font-weight:600;">4. Data Security</span><br>
We implement industry-standard security measures to protect your information from unauthorized access, disclosure, or alteration.<br>
However, no method of transmission over the internet or electronic storage is 100% secure. While we strive to protect your information, we cannot guarantee its absolute security.<br>
<span style="-webkit-background-clip:text !important;font-weight:600;">5. Children's Privacy</span><br>
Boost is not intended for individuals under the age of 13. We do not knowingly collect or solicit personal information from children. If you believe we have inadvertently collected personal information from a child, please contact us immediately.<br>
<span style="-webkit-background-clip:text !important;font-weight:600;">6. Your Choices and Rights</span><br>
You have the right to access, update, or delete your personal information. You can do so by contacting us directly.<br>
You can opt-out of receiving promotional communications from us by following the unsubscribe instructions provided in the communication or by contacting us.<br>
<span style="-webkit-background-clip:text !important;font-weight:700;">7. Changes to this Privacy Policy</span><br>
We reserve the right to update or modify this Privacy Policy at any time. The revised policy will be effective upon posting on our website. We encourage you to review this Privacy Policy periodically.<br>
<span style="-webkit-background-clip:text !important;font-weight:700;">8. Contact Us</span><br>
If you have any questions or concerns regarding this Privacy Policy or our data practices, please contact us at codingprojects2018@gmail.com.<br>
Please note that this Privacy Policy applies only to Boost and not to any third-party websites or services linked to or integrated with Boost. We encourage you to review the privacy policies of those third-party platforms.<br>
<span style="background-clip: text !important;"><span style="font-weight: 600;">By using Boost, you signify your acceptance of this Privacy Policy.</span></span></div></div><div class="page-content__component text_5459d84f-a961-4334-af29-a6c63b4ee757" data-container="grid" id="5459d84f-a961-4334-af29-a6c63b4ee757" data-type="text"><div data-wysiwyg="true"><div style="vertical-align: top;" tab-index="3" text-content="true"><div class="page-content__component text_73283844-f3a3-4b2b-aa70-a67ec9d5e1d9" data-container="grid" id="73283844-f3a3-4b2b-aa70-a67ec9d5e1d9" data-type="text"><div data-wysiwyg="true"><a href="/" class="str-link" data-close-click-outside="true" data-id="link-46480253-6364-47e1-8257-717befe41524" data-overlay-color="rgba(0, 0, 0, 0.2)" data-popup-position="center" data-type="page" style="font-family:Poppins;font-weight:700;color:inherit;font-size:inherit;" href="" data-cke-saved-href="" target="_blank">home</a></div></div></a></div></div></div>

</div></div><style>.rectangle_5b03ba2f-4cae-4e1e-b19a-cb7603423eb6 .strw-shape {
  content: '';
  position: absolute;
  top:0;
  left: 0;
  right:0;
  bottom:0;
  background-image: -webkit-linear-gradient(to right, rgba(0, 0, 0, 1), rgba(0, 0, 0, 1));
  background-image:    -moz-linear-gradient(to right, rgba(0, 0, 0, 1), rgba(0, 0, 0, 1));
  background-image:     -ms-linear-gradient(to right, rgba(0, 0, 0, 1), rgba(0, 0, 0, 1));
  background-image:      -o-linear-gradient(to right, rgba(0, 0, 0, 1), rgba(0, 0, 0, 1));
  background-image:         linear-gradient(to right, rgba(0, 0, 0, 1), rgba(0, 0, 0, 1));
}

.rectangle_5b03ba2f-4cae-4e1e-b19a-cb7603423eb6:hover .strw-shape {
  
    opacity: 1;
    background-image: -webkit-;
    background-image:    -moz-;
    background-image:     -ms-;
    background-image:      -o-;
    background-image:         ;
  
}.rectangle_5b03ba2f-4cae-4e1e-b19a-cb7603423eb6 { top: 1px;left: -793.255px;width: 2732.5px;border: none;height: 124.711px;opacity: 1;overflow: hidden;position: absolute;box-shadow: none;visibility: inherit;background-size: cover;background-repeat: no-repeat;background-position: center; }.rectangle_5b03ba2f-4cae-4e1e-b19a-cb7603423eb6 {
            left: -moz-calc(50% - 600px + -793.255px);
            left: -webkit-calc(50% - 600px + -793.255px);
            left: -o-calc(50% - 600px + -793.255px);
            left: calc(50% - 600px + -793.255px)
          }.text_9cf57baa-bf2c-4d69-947d-1df794f7a6a4 [data-wysiwyg="true"] {
  display: table-cell;
  vertical-align: top
}


  


.text_9cf57baa-bf2c-4d69-947d-1df794f7a6a4 {
  
  color: rgba(255, 255, 255, 1);
  
}



.text_9cf57baa-bf2c-4d69-947d-1df794f7a6a4 { top: 33px;left: -38px;width: 425.158px;height: 59px;display: table;opacity: 1;font-size: 50px;position: absolute;text-align: left;font-family: Poppins;font-weight: 900;line-height: 59px;text-shadow: none;visibility: inherit;letter-spacing: 0em; }.text_9cf57baa-bf2c-4d69-947d-1df794f7a6a4 {
            left: -moz-calc(50% - 600px + -38px);
            left: -webkit-calc(50% - 600px + -38px);
            left: -o-calc(50% - 600px + -38px);
            left: calc(50% - 600px + -38px)
          }.text_18eb6772-845f-487e-a512-884cf896e99b [data-wysiwyg="true"] {
  display: table-cell;
  vertical-align: top
}


  


.text_18eb6772-845f-487e-a512-884cf896e99b {
  
  color: rgba(0, 0, 0, 1);
  
}



.text_18eb6772-845f-487e-a512-884cf896e99b { top: 153px;left: -89px;width: 1373.83px;height: 4838px;display: table;opacity: 1;font-size: 24px;position: absolute;text-align: left;font-family: Poppins;font-weight: 400;line-height: 29px;text-shadow: none;visibility: inherit;letter-spacing: 0em; }.text_18eb6772-845f-487e-a512-884cf896e99b {
            left: -moz-calc(50% - 600px + -89px);
            left: -webkit-calc(50% - 600px + -89px);
            left: -o-calc(50% - 600px + -89px);
            left: calc(50% - 600px + -89px)
          }.text_5459d84f-a961-4334-af29-a6c63b4ee757 [data-wysiwyg="true"] {
  display: table-cell;
  vertical-align: top
}


  


.text_5459d84f-a961-4334-af29-a6c63b4ee757 {
  
  color: rgba(255, 255, 255, 1);
  
}



.text_5459d84f-a961-4334-af29-a6c63b4ee757 { top: 55px;left: 1131px;width: 75.0917px;height: 34.0573px;display: table;opacity: 1;font-size: 20px;position: absolute;text-align: left;font-family: Poppins;font-weight: 600;line-height: 24px;text-shadow: none;visibility: inherit;letter-spacing: 0em; }.text_5459d84f-a961-4334-af29-a6c63b4ee757 {
            left: -moz-calc(50% - 600px + 1131px);
            left: -webkit-calc(50% - 600px + 1131px);
            left: -o-calc(50% - 600px + 1131px);
            left: calc(50% - 600px + 1131px)
          }</style><style>.page_pg_n2prXkLTBBAugZnXyddEPLx3W { height: 1524.785144460758px; }.page_pg_n2prXkLTBBAugZnXyddEPLx3W:after {
  background-image: -webkit-linear-gradient(to right, rgba(255, 255, 255, 1), rgba(255, 255, 255, 1));
  background-image:    -moz-linear-gradient(to right, rgba(255, 255, 255, 1), rgba(255, 255, 255, 1));
  background-image:     -ms-linear-gradient(to right, rgba(255, 255, 255, 1), rgba(255, 255, 255, 1));
  background-image:      -o-linear-gradient(to right, rgba(255, 255, 255, 1), rgba(255, 255, 255, 1));
  background-image:         linear-gradient(to right, rgba(255, 255, 255, 1), rgba(255, 255, 255, 1));
  background-size: cover;
}

.page_pg_n2prXkLTBBAugZnXyddEPLx3W {
  background-repeat: no-repeat;
  background-position: top center;
  background-size: cover;
}</style></div> <div class="page-content__inner-fixed" id="page-content-fixed" style="transform: scale(1);"></div> </div> <div class="notification-container" style="display: none"> <span> <div class="notification"> <svg onclick="EditorPageWidgets.notifyHide()" width="16" height="16" viewBox="0 0 16 16" fill="none" xmlns="http://www.w3.org/2000/svg" style="position: absolute; top: 20px; right: 22px;"> <g opacity="0.5"> <path d="M15 1L1 15" stroke="#333333"></path> <path d="M1 1L15 15" stroke="#333333"></path> </g> </svg> <div class="notification-message" role="alert"> <h4 class="title"></h4> <div class="message"></div> </div> </div> </span> </div> </div> <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script> <script src="https://www.youtube.com/iframe_api"></script> <script src="https://player.vimeo.com/api/player.js"></script> <script src="https://maps.googleapis.com/maps/api/js?key=AIzaSyDrutUSPfjuwC8b4W9pitclowi3btRQkMo&amp;v=3.exp&amp;libraries=geometry,drawing,places,directions"></script> <link rel="stylesheet" href="https://api.siter.io/assets/magnific-popup-2f7f85183333c84a42262b5f8a4f8251958809e29fa31c65bdee53c4603502cd.css"> <script src="https://api.siter.io/assets/magnific-popup.min-37130bcc3f8b01fe7473f8bb60a9aea35dc77c05eedc37fbd70135363feb6999.js"></script> <script src="https://api.siter.io/assets/swiper.min-d36969d50f8c2fa3a00a68e55fe929e3af3fdd249cf33fd128b6a17a410e2c59.js"></script> <link rel="stylesheet" href="https://api.siter.io/assets/swiper-18be8aa3f032dded246a45a9da3dafdb3934e39e1f1b3b623c1722f3152b2788.css"> <script src="https://api.siter.io/assets/application-ad7d1058a4f8521663fc8298179979c36f417a211a3974b6793461b077d824f1.js"></script> </body></html>

    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
