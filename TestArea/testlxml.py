__author__ = 'limitwh'
# coding=gbk
#import requests
from bs4 import BeautifulSoup
htmlstr='''
<!DOCTYPE HTML>
<html lang="zh-CN">
<head>
    <!-- shouji -->
    <meta http-equiv="Content-Type" content="text/html; charset=gbk" />
    <title>【华为畅享6】【新年货】华为 畅享6 金色 移动联通电信4G手机 双卡双待【行情 报价 价格 评测】-京东</title>
    <meta name="keywords" content="HUAWEI畅享6,华为畅享6,华为畅享6报价,HUAWEI畅享6报价"/>
    <meta name="description" content="【华为畅享6】京东JD.COM提供华为畅享6正品行货，并包括HUAWEI畅享6网购指南，以及华为畅享6图片、畅享6参数、畅享6评论、畅享6心得、畅享6技巧等信息，网购华为畅享6上京东,放心又轻松" />
    <meta name="format-detection" content="telephone=no">
    <meta http-equiv="mobile-agent" content="format=xhtml; url=//item.m.jd.com/product/3888216.html">
    <meta http-equiv="mobile-agent" content="format=html5; url=//item.m.jd.com/product/3888216.html">
    <meta http-equiv="X-UA-Compatible" content="IE=Edge">
    <link rel="canonical" href="//item.jd.com/3888216.html"/>
        <link rel="dns-prefetch" href="//misc.360buyimg.com"/>
    <link rel="dns-prefetch" href="//static.360buyimg.com"/>
    <link rel="dns-prefetch" href="//img10.360buyimg.com"/>
    <link rel="dns-prefetch" href="//img11.360buyimg.com"/>
    <link rel="dns-prefetch" href="//img13.360buyimg.com"/>
    <link rel="dns-prefetch" href="//img12.360buyimg.com"/>
    <link rel="dns-prefetch" href="//img14.360buyimg.com"/>
    <link rel="dns-prefetch" href="//img30.360buyimg.com"/>
    <link rel="dns-prefetch" href="//pi.3.cn"/>
    <link rel="dns-prefetch" href="//ad.3.cn"/>
    <link rel="dns-prefetch" href="//dx.3.cn"/>
    <link rel="dns-prefetch" href="//c.3.cn"/>
    <link rel="dns-prefetch" href="//d.jd.com"/>
    <link rel="dns-prefetch" href="//x.jd.com"/>
    <link rel="dns-prefetch" href="//wl.jd.com"/>
                            <link rel="stylesheet" type="text/css" href="//misc.360buyimg.com/??jdf/1.0.0/unit/ui-base/1.0.0/ui-base.css,jdf/1.0.0/unit/shortcut/2.0.0/shortcut.css,jdf/1.0.0/unit/global-header/1.0.0/global-header.css,jdf/1.0.0/unit/myjd/2.0.0/myjd.css,jdf/1.0.0/unit/nav/2.0.0/nav.css,jdf/1.0.0/unit/shoppingcart/2.0.0/shoppingcart.css,jdf/1.0.0/unit/global-footer/1.0.0/global-footer.css,jdf/1.0.0/unit/service/1.0.0/service.css">
        <style>[style*="2147483647"] div[hui-mod] {display: none !important;}
.sh-brand-wrap-630128 {
font: 14px/1.5 '\5fae\8f6f\96c5\9ed1', Arial, sans-serif;
height: 110px;
overflow:hidden;
position:relative;
}
.sh-brand-wrap-630128 img {
vertical-align: middle;
}
.sh-brand-wrap-630128 .sh-brand {
position: relative;
margin: 0 auto;
width: 990px;
overflow:hidden;
}
.sh-brand-wrap-630128 .sh-brand .shop-name-box {
position: absolute;
top: 50%;
margin-top: -30px;
height: 60px;
left: 190px;
vertical-align: top;
}
.sh-brand-wrap-630128 .sh-brand .shop-name-box .shop-name{
font-size: 18px;
color: #333;
}
.sh-brand-wrap-630128 .sh-brand .shop-logo-box {
position: absolute;
top: 50%;
margin-top: -40px;
}
.sh-brand-wrap-630128 .sh-hot-wrap img {
width: 180px;
height: 60px;
}
.sh-brand-wrap-630128 .sh-brand .hot-link {
display: 'inline-block';
position:absolute;
}
.sh-brand-wrap-630128 .sh-brand .coupons {
position: absolute;
right: 0;
top: 50%;
margin-top: -28px;
}
.sh-brand-wrap-630128 .sh-brand .coupons .coupon {
float: left;
margin-left: 10px;
}
.sh-brand-wrap-630128 .sh-brand .follow-me {
display: inline-block;
*display: inline;
*zoom: 1;
padding-left: 24px;
width: 47px;
height: 23px;
line-height: 23px;
color: #000;
font-size: 12px;
background: url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEcAAABZCAMAAABbssnGAAAA/1BMVEUAAAD///////+xGRqxGRqxGRr////uub2xGRr////uub2xGRr///+xGRr////////uub3uub3uub3////uub2xGRruub3uub3////uub2xGRr////uub2xGRruub3////uub2xGRqxGRqxGRqxGRqxGRr////uub2xGRr////uub3kOTzlQEOzHx/++/vsoqbsmJzoaWz9+Pj78vL03t7y2Njv0dHtyMjqwcHtq6/jrKzNbG3GV1jEUFHmTE+/QEG8Oju1Jie6MjP57+/25ub25eXou7zgpKTblJTpfYHRdHXnX2LIXV3mWFvmU1bBSEnBR0i3KSrWhofVg4O6NDWxIW+2AAAAKHRSTlMAl9DQlkxEREQGBgbw8JtMTNCb1tbWmJa3t7fx8fHv1dXVm5yZmktLhfBmHAAAAn5JREFUWMPtmMdy2zAQhlfFIq3eZVuWi+IkAIu61SVLcu92kvd/logAMcT4tgBPHn2Xf3n5ZmcxWMwQfBKRaJriSNN0NJIAmdwpVeU0B4L9CNUhu+9rDqgeB1yUpbpkPc0vXl+OL0Xg8WbER/zkEndG6WwbT3hPCSDBigfi8fLC4gEvSgA/qxWRWOE9EYiydGWPi/dEIc1yLXvWeE8aeM5kz4zi8fu5/Qw0n7cq/UR5MQo8I6oyH3G3xmt/OGOqQAQSohyu2JkPqQoJgJKob94Jeb9R0pS83UMFrcWiRZXIhXTfQ9s/XJTV3YeCXEnZUuL7WXov6khDnda992LHju+LUbPwnBRqBsjkzyxVzvIgSFYtHapJX3No6XHIRUVLl6Kn+c3rdqctAo83Iz7irm073W04tr0NLGUAgxWPtsfzM4tHvMiAGsulLbHEe2pQYOnIHgfvKcBJKJ5j4NmVPV0Lj9/PxJHamaj0U+BFJ/B0LJX5iLvVcfxumAZ/XoYo20t25m1LBQOgLOrJm22/TZQ0ZW/3BJ+vr5Ya+ZDue6j7B5JFvW6SIMiXlS3lPMgYKjv6uFA1YMeO74sZj2UIjgzJxOImyOydE1XO90CQuiA6XKR8zRHR44iLfhJdmmw2vL6aX4nA482Ij/i+RXtTQqY92rrHeyoAJiv+UI+7OxZ/8SIT4iwHVGKA98QhxrIne3p4TwwyLPuyp4/3ZIDnVPZMCR6/n811oLn+p9JPjBeLVvDXhajMJ+5X874/nDlRIA6mKD8G7Mw/iAomQEXUmyGlw42SpsLul8AdjVyiBNtBTaLLj1D3D6Saet2kgv1cUbZU9r6+Fw2koUEawXvxHzpC3Z34XwtFAAAAAElFTkSuQmCC) 0 0 no-repeat;
}
.sh-brand-wrap-630128 .sh-brand .follow-me:hover {
background-position: 0 -33px;
}
.sh-brand-wrap-630128 .sh-brand .for-light-bg {
color: #fff;
background-position: 0 -66px;
}
.sh-brand-wrap-630128 .sh-brand .m-search {
position: absolute;
right: 0;
top: 50%;
margin-top: -32px;
height: 64px;
}
.sh-brand-wrap-630128 .sh-brand .m-search .m-kw {
margin-right: -6px;
padding-left: 5px;
width: 164px;
height: 32px;
vertical-align: top;
border: 2px solid #000;
}
.sh-brand-wrap-630128 .sh-brand .m-search .m-submit {
padding: 0 15px;
border: 0;
height: 38px;
vertical-align: top;
background-color: #000;
color: #fff;
cursor: pointer;
}
.sh-brand-wrap-630128 .sh-brand .m-search .m-hw {
padding-top: 5px;
font-size: 12px;
}
.sh-brand-wrap-630128 .sh-brand .m-search .m-hw .hw-link {
margin-right: 10px;
color: #666;
}
.sh-brand-wrap-630128 .sh-brand .for-black-bg .m-kw {
border-color: #b1191a;
}
.sh-brand-wrap-630128 .sh-brand .for-black-bg .m-submit {
background-color: #b1191a;
}
.sh-brand-wrap-630128 .sh-brand .for-black-bg .m-hw .hw-link {
color: #fff;
}
.sh-brand-wrap-630128 .userDefinedArea {
 margin: 0 auto;
}

.sh-head-menu-922476 ul,
.sh-head-menu-922476 ol,
.sh-head-menu-922476 dl,
.sh-head-menu-922476 li,
.sh-head-menu-922476 dt,
.sh-head-menu-922476 dd {
margin: 0;
padding: 0;
list-style: none;
}
.sh-head-menu-922476 .sh-hd-container {
background-color: #fff;
}
.sh-head-menu-922476 a {
text-decoration: none;
color: #666666;
}
.sh-head-menu-922476 {
width: 100%;
}
.sh-head-menu-922476 .sh-hd-wrap {
font: 14px/1.5 '\5fae\8f6f\96c5\9ed1', Arial, sans-serif;
position: relative;
margin: 0 auto;
height: 40px;
font-size: 14px;
color: #333;
width: 990px;
}
.sh-head-menu-922476 .menu-list {
width: 100%;
height: 40px;
list-style: none;
}
.sh-head-menu-922476 .mc {
overflow: visible;
}
.sh-head-menu-922476 .menu-list .menu {
float: left;
line-height: 24px;
height: 24px;
padding: 8px 0;
border-radius: 12px;
}
.sh-head-menu-922476 .menu-list .menu:hover .arrow,
.sh-head-menu-922476 .menu-list .menu .hover .arrow {
font-size: 0;
line-height: 0;
height: 0;
width: 0;
border-top: 0;
border-left: 5px dashed transparent;
border-right: 5px dashed transparent;
border-bottom: 5px solid #fff;
}
.sh-head-menu-922476 .menu-list .menu:hover .main-link,
.sh-head-menu-922476 .menu-list .menu .hover .main-link {
color: #fff !important;
background-color: #333;
}
.sh-head-menu-922476 .menu-list .menu .main-link {
position: relative;
z-index: 4;
display: block;
padding: 0 15px;
color: #333;
border-radius: 12px;
}
.sh-head-menu-922476 .menu-list .menu .home-link {
font-weight:bold;
}
.sh-head-menu-922476 .menu-list .menu .arrow {
display: inline-block;
*display: inline;
*zoom: 1;
vertical-align: middle;
margin-left: 10px;
font-size: 0;
line-height: 0;
height: 0;
width: 0;
border-bottom: 0;
border-left: 5px dashed transparent;
border-right: 5px dashed transparent;
border-top: 5px solid #666;
}
.sh-head-menu-922476 .menu-list .menu .sub-menu-wrap {
display: none;
position: absolute;
left: 0;
top: 39px;
right: 0;
z-index: 99;
padding: 20px 40px;
border: 1px solid #bebab0;
background-color: rgba(247, 242, 234, 0.9);
}
.sh-head-menu-922476 .menu-list .menu .sub-menu-wrap .sub-pannel {
float: left;
padding: 0;
_display: inline;
}
.sh-head-menu-922476 .menu-list .menu .sub-menu-wrap .sub-title {
margin-bottom: 13px;
height: 54px;
line-height: 54px;
border-bottom: dashed 1px #c9c9c9;
padding: 0 20px;
}
.sh-head-menu-922476 .menu-list .menu .sub-menu-wrap .sub-list {
padding: 0 20px;
}
.sh-head-menu-922476 .menu-list .menu .sub-menu-wrap .sub-title .sub-tit-link {
font-size: 14px;
font-weight: bold;
color: #333;
line-height: 24px;
display: inline-block;
height: 24px;
padding: 0 10px;
margin-left: -10px;
border-radius: 12px;
min-width: 74px;
}
.sh-head-menu-922476 .menu-list .menu .sub-menu-wrap .sub-title .sub-tit-link:hover {
border: solid 1px #e4393c;
color: #e4393c;
}
.sh-head-menu-922476 .menu-list .menu .sub-menu-wrap .leaf {
font-size: 12px;
height: 26px;
line-height: 26px;
}
.sh-head-menu-922476 .menu-list .menu .sub-menu-wrap .leaf .leaf-link:hover {
color: #c81623;
}
.sh-head-menu-922476 .menu-list .menu .sub-menu-wrap .all-goods-wrap {
clear: both;
padding-left: 20px;
}
.sh-head-menu-922476 .menu-list .menu .sub-menu-wrap .all-goods-wrap .all-goods-link {
font-weight: bold;
padding-left: 20px;
border: solid 1px #666;
border-radius: 12px;
height: 24px;
line-height: 24px;
padding: 0 10px;
}
.sh-head-menu-922476 .menu-list .menu:hover .sub-menu-wrap {
display: block;
}
.sh-head-menu-922476 .menu-list .menu .all-goods-link-wrap {
clear: both;
padding: 23px 20px 0;
}
.sh-head-menu-922476 .menu-list .menu .all-goods-link {
display: inline-block;
border: solid 1px #666;
height: 24px;
line-height: 24px;
border-radius: 12px;
padding: 0 10px;
margin-left: -10px;
font-weight:bold;
color: #000;
}
.sh-head-menu-922476 .s-form {
position: absolute;
top: 8px;
right: 0;
}
.sh-head-menu-922476 .s-form .s-inp {
padding: 0 0 0 10px;
width: 130px;
line-height: 22px;
height: 22px;
background-color: #ffffff;
color: #c9c9c9;
vertical-align: top;
outline: none;
border: solid 1px #e1e1e1;
border-top-left-radius: 11px;
border-bottom-left-radius: 11px;
}
.sh-head-menu-922476 .s-form .s-submit {
margin-left: -5px;
padding: 0 10px;
border: 0;
height: 24px;
width: 46px;
cursor: pointer;
border-top-right-radius: 11px;
border-bottom-right-radius: 11px;
background:#333 url("//img13.360buyimg.com/cms/jfs/t3121/284/4170076300/1201/43e1ad98/583543d4Nc7e0c1a4.png") no-repeat center;
}</style>
                        <link rel="stylesheet" type="text/css" href="//static.360buyimg.com/item/default/1.0.37/components/??/common/common.css,/main/main.css,/address/address.css,/prom/prom.css,/colorsize/colorsize.css,/buytype/buytype.css,/track/track.css,/suits/suits.css,/baitiao/baitiao.css,/o2o/o2o.css,/summary/summary.css,/buybtn/buybtn.css,/crumb/crumb.css,/fittings/fittings.css,/detail/detail.css,/contact/contact.css,/popbox/popbox.css,/preview/preview.css,/info/info.css,/imcenter/imcenter.css,/jdservice/jdservice.css,/popupCar/popupCar.css,/poprent/poprent.css" />
        <script charset="gbk">
        var pageConfig = {
                compatible: true,
                product: {
                    modules: [
                        'address',
                        'prom',
                        'colorsize',
                        'buytype',
                        'baitiao',
                        'summary',
                        'o2o',
                        'buybtn',
                        'track',
                        'suits',
                        'crumb',
                        'fittings',
                        'detail',
                        'contact',
                        'popbox',
                        'preview',
                        'info',
                        'imcenter',
                        'jdservice',
                        'commitments',
                        'gift',
                        'popupCar'        ],
                imageAndVideoJson: {},
                ostime: 1519220366.737,
        skuid: 3888216,
        name: '\u3010\u65b0\u5e74\u8d27\u3011\u534e\u4e3a\u0020\u7545\u4eab\u0036\u0020\u91d1\u8272\u0020\u79fb\u52a8\u8054\u901a\u7535\u4fe1\u0034\u0047\u624b\u673a\u0020\u53cc\u5361\u53cc\u5f85',
            skuidkey:'FEB76B7887D03EDFBFD91BD01567B3BB',
            href: '//item.jd.com/3888216.html',
                koEndOffset : 8434000,koEndTime:1519228800000,
                        src: 'jfs/t3637/275/652996370/280419/2a134044/58105e15N75fb0595.jpg',
                imageList: ["jfs/t3637/275/652996370/280419/2a134044/58105e15N75fb0595.jpg","jfs/t3697/87/647818434/172938/25a798fe/58105e19N58917f62.jpg","jfs/t3364/209/682238813/177412/e0a59882/58105e1cNfab816f2.jpg","jfs/t3346/108/621106249/149901/27cda576/58105e1fN440cf37a.jpg","jfs/t3568/33/645616471/141345/6613a544/58105e22Ncf939ce4.jpg","jfs/t3451/292/636496916/239681/37f48c17/58105e34Naab1186c.jpg","jfs/t3427/233/660473690/178101/ac72933d/58105e38N5fee2bf5.jpg","jfs/t3766/68/687577971/180767/1d7762f3/58105e3bN2c1c857e.jpg"],
                cat: [9987,653,655],
        forceAdUpdate: '8277',
            brand: 8557,
        pType: 1,
        isClosePCShow: false,
         pTag:424106,                                         isPop:false,
        venderId:1000004259,
        shopId:'1000004259',
                commentVersion:'64357',         specialAttrs:["isFlashPurchase-0","isSupportCard","IsSXQJ","nationallySetWare-5","packType","IsNewGoods","isCanUseDQ-1","YushouStepType-0","isCanUseJQ-1"],
        recommend : [0,1,2,3,4,5,6,7,8,9],
            easyBuyUrl:"//easybuy.jd.com/skuDetail/newSubmitEasybuyOrder.action",
            qualityLife: "//c.3.cn/qualification/info?skuId=3888216&pid=3888216&catId=655",
        phoneNetwork:['移动4G/联通4G/电信4G','移动4G','联通4G','电信4G'],        colorSize: [{"版本":"全网通","skuId":3458011,"颜色":"灰色"},{"版本":"移动定制版","skuId":4577199,"颜色":"金色"},{"版本":"移动定制版","skuId":5305784,"颜色":"白色"},{"版本":"全网通","skuId":3888216,"颜色":"金色"}],        warestatus: 1,                         desc: '//cd.jd.com/description/channel?skuId=3888216&mainSkuId=3888216&cdn=2',
        cmsNavigation: [{"address":"//shouji.jd.com/","corner":"","name":"手机首页","order":1},{"address":"//sale.jd.com/act/WX2fhkEvletpdM.html","corner":"","name":"新品频道","order":2},{"address":"//sale.jd.com/act/oMHT5c7gAznJ.html","corner":"","name":"游戏手机","order":3},{"address":"//phone.jd.com/","corner":"","name":"正品好店","order":4},{"address":"//wt.jd.com/","corner":"","name":"网上营业厅","order":5},{"address":"//group.jd.com/site/20000151/20000091.htm","corner":"","name":"手机社区","order":6}],        /*cmsSuit: table: 0x41eebd70,*/
        cmsAd: [{"content":"10元抢1GB流量","link":"http://sale.jd.com/act/mRZ4HLxoOews3.html","areas":"1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,23,24,25,26,27,28,29,30,31,32,42,43,84"},{"content":"0元享200M流量","link":"http://item.jd.com/2932671.html","areas":"22"}],         /* cmsExpand: table: 0x41ece310,*/
                twoColumn: true,                isFeeType: true,                                        isBookMvd4Baby: false,        addComments:true,
                foot: '//dx.3.cn/footer?type=common_config2',
                         huanfuInfo:{"beginDate":1513785600000,"tagClassify":1,"endDate":1513871999000,"name":"自营商详换肤222","tagUrl":""} ,          shangjiazizhi: false        }
        };
                                try {
                        function is_sort_black_list() {
              var jump_sort_list = {"6881":3,"1195":3,"10011":3,"6980":3,"12360":3};
              if(jump_sort_list['9987'] == 1 || jump_sort_list['653']==2 || jump_sort_list['655']==3) {
                return false;
              }
              return false;
            }

            function jump_mobile() {
              if(is_sort_black_list()) {
                return;
              }

              var userAgent = navigator.userAgent || "";
              userAgent = userAgent.toUpperCase();
                            if(userAgent == "" || userAgent.indexOf("PAD") > -1) {
                  return;
              }

                            if(window.location.hash == '#m') {
                var exp = new Date();
                exp.setTime(exp.getTime() + 30 * 24 * 60 * 60 * 1000);
                document.cookie = "pcm=1;expires=" + exp.toGMTString() + ";path=/;domain=jd.com";
                                window.showtouchurl = true;
                return;
              }

                            if (/MOBILE/.test(userAgent) && /(MICROMESSENGER|QQ\/)/.test(userAgent)) {
                  var paramIndex = location.href.indexOf("?");
                  window.location.href = "//item.m.jd.com/product/3888216.html"+(paramIndex>0?location.href.substring(paramIndex,location.href.length):'');
                  return;
              }

                            var jump = true;
              var cook = document.cookie.match(/(^| )pcm=([^;]*)(;|$)/);
              if(cook && cook.length > 2 && unescape(cook[2]) == "1") {
                jump = false;
              }
              var mobilePhoneList = ["IOS","IPHONE","ANDROID","WINDOWS PHONE"];
              for(var i=0, len=mobilePhoneList.length; i<len; i++) {
                if(userAgent.indexOf(mobilePhoneList[i]) > -1) {
                  if(jump) {
                    var paramIndex = location.href.indexOf("?");
                    window.location.href = "//item.m.jd.com/product/3888216.html"+(paramIndex>0?location.href.substring(paramIndex,location.href.length):'');
                  } else {
                                        window.showtouchurl = true;
                  }
                  break;
                }
              }
            }
            jump_mobile();
        } catch(e) {}
        var __FE_Monitor_Config = { sid: 'item', browsers: [ 'chrome' ] };
    </script>
    <script src="//misc.360buyimg.com/??jdf/lib/jquery-1.6.4.js,jdf/1.0.0/unit/base/1.0.0/base.js,jdf/1.0.0/ui/ui/1.0.0/ui.js"></script>

    <script>
        seajs.config({
            paths: {
                'MISC' : '//misc.360buyimg.com',
                'MOD_ROOT' : '//static.360buyimg.com/item/default/1.0.37/components',
                'PLG_ROOT' : '//static.360buyimg.com/item/default/1.0.37/components/common/plugins',
                'JDF_UI'   : '//misc.360buyimg.com/jdf/1.0.0/ui',
                'JDF_UNIT' : '//misc.360buyimg.com/jdf/1.0.0/unit'
            }
        });
    </script>
    <script src="//static.360buyimg.com/devfe/devfe-monitor/1.0.0/js/log_client.js" crossorigin></script>

</head>
<body version="140120" class="cat-1-9987 cat-2-653 cat-3-655 item-3888216 JD JD-1">
<div id="shortcut-2014">
    <div class="w">
        <ul class="fl" clstag="shangpin|keycount|topitemnormal|a01">
            <li class="dorpdown" id="ttbar-mycity"></li>
        </ul>
        <ul class="fr">
            <li class="fore1" id="ttbar-login" clstag="shangpin|keycount|topitemnormal|a02">
                <a target="_blank" href="javascript:login();" class="link-login">你好，请登录</a>
                &nbsp;&nbsp;
                <a href="javascript:regist();" class="link-regist style-red">免费注册</a>
            </li>
            <li class="spacer"></li>
            <li class="fore2"  clstag="shangpin|keycount|topitemnormal|a03">
                <div class="dt">
                    <a target="_blank" href="//order.jd.com/center/list.action">我的订单</a>
                </div>
            </li>
            <li class="spacer"></li>
            <li class="fore3 dorpdown" id="ttbar-myjd" clstag="shangpin|keycount|topitemnormal|b04">
                <div class="dt cw-icon">
                    <i class="ci-right"><s>◇</s></i>
                    <a target="_blank" href="//home.jd.com/">我的京东</a>
                </div>
                <div class="dd dorpdown-layer"></div>
            </li>
            <li class="spacer"></li>
            <li class="fore4" clstag="shangpin|keycount|topitemnormal|a04">
                <div class="dt">
                    <a target="_blank" href="//vip.jd.com/">京东会员</a>
                </div>
            </li>
            <li class="spacer"></li>
            <li class="fore5"  clstag="shangpin|keycount|topitemnormal|a05">
                <div class="dt">
                    <a target="_blank" href="//b.jd.com/">企业采购</a>
                </div>
            </li>
            <li class="spacer"></li>
            <li class="fore6 dorpdown" id="ttbar-apps" clstag="shangpin|keycount|topitemnormal|a06">
                <div class="dt cw-icon">
                    <i class="ci-left"></i>
                    <i class="ci-right"><s>◇</s></i>
                    <a target="_blank" href="//app.jd.com/">手机京东</a>
                </div>
            </li>
            <li class="spacer"></li>
            <li class="fore7 dorpdown" id="ttbar-atte" clstag="shangpin|keycount|topitemnormal|a09">
                <div class="dt cw-icon">
                    <i class="ci-right"><s>◇</s></i>关注京东
                </div>
            </li>
            <li class="spacer"></li>
            <li class="fore8 dorpdown" id="ttbar-serv" clstag="shangpin|keycount|topitemnormal|a07">
                <div class="dt cw-icon">
                    <i class="ci-right"><s>◇</s></i>客户服务
                </div>
                <div class="dd dorpdown-layer"></div>
            </li>
            <li class="spacer"></li>
            <li class="fore9 dorpdown" id="ttbar-navs" clstag="shangpin|keycount|topitemnormal|a08">
                <div class="dt cw-icon">
                    <i class="ci-right"><s>◇</s></i>网站导航
                </div>
                <div class="dd dorpdown-layer"></div>
            </li>
        </ul>
        <span class="clr"></span>
    </div>
</div><!-- #shortcut-2014 --><style type="text/css">
    #search-2014 .button {
        width: auto;
        padding: 0 8px;
        font:12px simsun;
        overflow:visible;
    }
    #search-2014 .button01 {
        background: #474e5c;
    }
    #search-2014 .text {
        width: 340px;
    }
    #search-2014 .form {
        width: 480px;
    }
    #shelper {
        width: 349px;
    }
    .root61 #search-2014, .root61 #search-2014 .form {
        _width: 560px;
    }
</style>

<div class="w">
    <div id="logo-2014">
        <a href="//www.jd.com/" class="logo" clstag="shangpin|keycount|topitemnormal|d01">京东</a>
        <div class="extra">
            <div id="channel"></div>
            <div id="categorys-mini">
                <div class="cw-icon">
                    <h2><a href="//www.jd.com/allSort.aspx" clstag="shangpin|keycount|topitemnormal|d02">全部分类<i class="ci-right"><s>◇</s></i></a></h2>
                </div>
                <div id="categorys-mini-main">
                    <span class="loading"></span>
                </div>
            </div>
        </div>
    </div>

    <div id="search-2014" >
        <ul id="shelper" class="hide"></ul>
        <div class="form">
            <input type="text" onkeydown="javascript:if(event.keyCode==13) search('key');" autocomplete="off" id="key" accesskey="s" class="text" />
            <button onclick="search('key');return false;" class="button cw-icon" clstag="shangpin|keycount|topitemnormal|d03">搜全站</button>
            <button type="button" class="button button01" clstag="shangpin|keycount|topitemnormal|d04">搜本店</button>
        </div>
    </div>
    <div id="settleup-2014" class="dorpdown">
        <div class="cw-icon">
            <i class="ci-left"></i>
            <i class="ci-right">&gt;</i>
            <a target="_blank" href="//cart.jd.com/cart.action" clstag="shangpin|keycount|topitemnormal|d05">我的购物车</a>
        </div>
        <div class="dorpdown-layer">
            <div class="spacer"></div>
            <div id="settleup-content">
                <span class="loading"></span>
            </div>
        </div>
    </div>
    <div id="hotwords"></div>
    <span class="clr"></span>
    <script>
                (function() {
            $('.button01').click(function() {
                url = '//mall.jd.com/advance_search-' + 466323 + '-' + pageConfig.product.venderId + '-' + pageConfig.product.shopId + '-0-0-0-1-1-24.html';
                location.href = url + '?keyword=' + encodeURIComponent(encodeURIComponent(jQuery.trim($('#key').val())));
            });
            $(function() {
                $("#navmore").hover(function() {
                    $(this).addClass("hover")
                }, function() {
                    $(this).removeClass("hover")
                });
            });
        })();
        seajs.use(['jdf/1.0.0/unit/globalInit/2.0.0/globalInit.js','jdf/1.0.0/unit/category/2.0.0/category.js'],function(globalInit,category){
            globalInit();
            category({type:'mini', mainId:'#categorys-mini', el:'#categorys-mini-main'});
        });
        seajs.use('MOD_ROOT/common/vendor/jshop-lib.min');

        (function(cfg) {
            function setPlaceholder(val) {
                $('#key').val(val)
                .bind('focus',function(){
                    if (this.value==val){ this.value='';this.style.color='#333' }
                })
                .bind('blur',function(){
                    if (this.value==''){ this.value=val;this.style.color='#999' }
                });
            }
            function render(r) {
                if (!r || !r.length) return;
                var html = '';
                var el = document.getElementById('hotwords')

                for (var i = 0; i < r.length; i++) {
                    var item = r[i];

                    if (i === 0) {
                        setPlaceholder(item.name)
                    } else {
                        html += '<a target="_blank" data-id="'+ item.id +'" href="'+ item.url_info +'">'+ item.name +'</a>'
                    }
                }

                if (el) el.innerHTML = html
            }
            $.ajax({
                url: '//cds.3.cn/hotwords/get',
                data: { cate: cfg.cat.join(',') },
                dataType: 'jsonp',
                success: render
            })
        })(pageConfig.product);
    </script>
</div><div id="shop-head" clstag="shangpin|keycount|product|dianputou"><div class="layout-area J-layout-area" >
		<div class="layout layout-auto J-layout" name="通栏布局（100%）" id="94714659" prototypeId="20" area="" layout_name="insertLayout" >
			<div class="layout-one" name="main">
				



<div onclick="log('shop_03','mall_03','1000004259','19268','630128')" class="fn-clear sh-brand-wrap-630128" instanceId="94714660" module-name="new_shop_signs" style="margin-bottom:0px;;margin-bottom: 0px" origin="0">
	<div class="mc" style=";">
	 	
<div class="j-module sh-brand-wrap" module-function="autoCenter" module-param="{}">
    <div class="userDefinedArea" style="width:990px;" data-title="">
        <div style="height:110px;background:url(//img10.360buyimg.com/imgzone/jfs/t19150/281/138532201/36785/f68e167c/5a604639N9f4c3b16.jpg) no-repeat top center;">
	<div style="width:990px;height:110px;margin:0 auto;position:relative;">
		<div class="j-module" module-function="saleAttent" module-param="{attentType:'vender'}">
			<a href="javascript:;" class="e-attention" data-id="1000004259" data-state="0" data-type="0" style="width:353px;height:93px;display:block;position:absolute;top:14px;left:5px;font-size:0;">关注店铺</a><a href="//item.jd.com/5826236.html" data-state="0" data-type="0" style="width:303px;height:101px;display:block;position:absolute;top:6px;left:686px;"></a> 
		</div>
	</div>
</div>
    </div>
</div>

<script type="text/javascript">
    function importHotZoneData() {
        $.each($('.hot-link'), function(index, item) {
            var pxArray = $(item).attr('px').split(',');
            $(item).css({
                left: pxArray[0] + 'px',
                top: pxArray[1]+ 'px',
                width: pxArray[2] - 2+ 'px',
                height: pxArray[3] - 2+ 'px'
            });
        });
    }
    importHotZoneData();
    function addAttentHtml(){
        var attentHtml = '<div class="j-attent-dialog-wrap">'
                +'<div class="attent-dialog-mask"></div>'
                +'<div class="attent-dialog">'
                +   '<div class="attent-mt">'
                +       '<span class="attent-close"  title="关闭">关闭</span>'
                +       '<span class="attent-title">提示</span>'
                +   '</div>'
                +   '<div class="attent-mc">'
                +       '<div class="attent-con">'
                +           '<span class="attent-msg"></span>'
                +           '<span class="attent-other"></span>'
                +       '</div>'
                +   '</div>'
                +'</div>'
                +'</div><div class="j-attent-tip-wrap attent-tip-wrap"><i></i></div>';

        var jAttWrap = $(".j-attent-dialog-wrap");

        if(jAttWrap.length === 0){
            jAttWrap = $(attentHtml).appendTo("body");
        }
    }
    addAttentHtml();
    function _seacrh_hot_keyword(obj){
        var base_url = "//mall.jd.com/view_search" +  "-466323" + "-1000004259" + "-1000004259"   + "-0-1-0-0-1-1-24.html";
        var keyword = $(obj).html();
        if(keyword){
            keyword = encodeURIComponent(keyword);
            keyword = encodeURIComponent(keyword);
        }else{
            keyword="";
        }
        var url = base_url + "?keyword="+keyword+"&isGlobalSearch=1";
        window.open(url);
    }

    function shop_signs_search(obj){
        var base_url = "//mall.jd.com/view_search" +  "-466323" + "-1000004259" + "-1000004259"   + "-0-1-0-0-1-1-24.html";
        var keyword = $(obj).prev().val();
        if(keyword){
            keyword = encodeURIComponent(keyword);
            keyword = encodeURIComponent(keyword);
        }else{
            keyword="";
        }
        var url = base_url + "?keyword="+keyword+"&isGlobalSearch=1";
        window.open(url);
    }

    $('.m-kw').keydown(function(e){
        if(e.keyCode==13){
            var base_url = "//mall.jd.com/view_search" +  "-466323" + "-1000004259" + "-1000004259"   + "-0-1-0-0-1-1-24.html";
            var keyword = $(this).val();
            if(keyword){
                keyword = encodeURIComponent(keyword);
                keyword = encodeURIComponent(keyword);
            }else{
                keyword="";
            }
            var url = base_url + "?keyword="+keyword+"&isGlobalSearch=1";
            window.open(url);
            return false;
        }
    });

    function _shop_attention(){
        jQuery('#shop-signs-attention').unbind('click');
        jQuery('#shop-signs-attention').click(function() {
            S_ifollow.follow(this);
            var url = "//follow-soa.jd.com/vender/follow";
            url+="?venderId=" +"1000004259";
            jQuery.ajax({
                url:url,
                type : 'GET',
                dataType : 'jsonp',
                //jsonp: 'jsonpCallback',
                success:function (data){
                    S_ifollow.requestSuccess(data);
                },
                error:function(){

                }
            });
        });
    }
    _shop_attention();
</script>

	</div>
</div>




<div onclick="log('shop_03','mall_03','1000004259','18169','922476')" class="fn-clear sh-head-menu-922476" instanceId="94714661" module-name="shop_link" style="margin-bottom:0px;;margin-bottom: 0px" origin="0">
	<div class="mc" style=" no-repeat center center;">
	 	<div style="height: 40px;overflow: hidden;">
    <div class="j-module" module-function="autoCenter" module-param="{}">
        <div class="userDefinedArea" style="width:px" data-title="">
            <div style="dispaly:none;">
</div>
        </div>
    </div>
</div>

	</div>
</div>

			</div>
		</div>
	</div></div><!--#shop-head-->
<script>
    (function(cfg) {
        var $nav1 = $('#navitems-group1');
        var $nav2 = $('#navitems-group2');
        var html = '<li class="fore1" id="nav-home"> <a href="//www.jd.com/">首页</a> </li>';

        if (cfg.cmsNavigation && cfg.cmsNavigation.length && $nav1.length) {
            $nav2.html('');
            var corner_class = "";
            var corner_i="";
            for (var i = 0; i < cfg.cmsNavigation.length; i++) {
                var nav = cfg.cmsNavigation[i];
                if(nav.corner&&nav.corner!=""){
                    corner_class = "new-tab";
                    corner_i="<i class='icon-new'>"+nav.corner+"<span></span></i>";
                }else{
                    corner_class="";
                    corner_i="";
                }
                var j = i + 3;
                if(j.toString().length == 1) {
                    j = "0" + j;
                }
                html += '<li class="fore'+ i +' '+corner_class+'" clstag="shangpin|keycount|topitemnormal|c' + j + '">'+corner_i+'<a href="'+ nav.address +'" target="_blank">'+ nav.name +'</a> </li>';
            }

            $nav1.html(html);
        }
    })(pageConfig.product);
</script>

<div class="crumb-wrap" id="crumb-wrap">
    <div class="w">
        <div class="crumb fl clearfix">
                        <div class="item first"><a href='//shouji.jd.com' clstag="shangpin|keycount|product|mbNav-1">手机</a></div>
            <div class="item sep">&gt;</div>
            <div class="item"><a href='//shouji.jd.com' clstag="shangpin|keycount|product|mbNav-2">手机通讯</a></div>
            <div class="item sep">&gt;</div>
            <div class="item"><a href='//list.jd.com/list.html?cat=9987,653,655' clstag="shangpin|keycount|product|mbNav-3">手机</a></div>
            <div class="item sep">&gt;</div>
                                    <div class="item">
                                <div class="J-crumb-br crumb-br EDropdown">
                    <div class="inner border">
                        <div class="head" data-drop="head">
                            <a href='//list.jd.com/list.html?cat=9987,653,655&ev=exbrand_8557' clstag="shangpin|keycount|product|mbNav-4">华为（HUAWEI）</a>
                            <span class="arrow arr-close"></span>
                        </div>
                        <div class="content hide" data-drop="content">
                                                        <ul class="br-reco plist-1 lh clearfix" clstag="shangpin|keycount|product|mbTJ-1"></ul>
                                                        <ul class="br-list" clstag="shangpin|keycount|product|mbTJ-2">
                                                                                                <li><a href="//list.jd.com/list.html?cat=9987,653,655&ev=exbrand_8557" target='_blank' title="华为（HUAWEI）">华为（HUAWEI）</a></li>
                                                                <li><a href="//list.jd.com/list.html?cat=9987,653,655&ev=exbrand_18374" target='_blank' title="小米（MI）">小米（MI）</a></li>
                                                                <li><a href="//list.jd.com/list.html?cat=9987,653,655&ev=exbrand_14026" target='_blank' title="Apple">Apple</a></li>
                                                                <li><a href="//list.jd.com/list.html?cat=9987,653,655&ev=exbrand_12669" target='_blank' title="魅族（MEIZU）">魅族（MEIZU）</a></li>
                                                                <li><a href="//list.jd.com/list.html?cat=9987,653,655&ev=exbrand_13539" target='_blank' title="诺基亚（NOKIA）">诺基亚（NOKIA）</a></li>
                                                                <li><a href="//list.jd.com/list.html?cat=9987,653,655&ev=exbrand_91515" target='_blank' title="锤子（smartisan）">锤子（smartisan）</a></li>
                                                                <li><a href="//list.jd.com/list.html?cat=9987,653,655&ev=exbrand_27306" target='_blank' title="360">360</a></li>
                                                                <li><a href="//list.jd.com/list.html?cat=9987,653,655&ev=exbrand_63032" target='_blank' title="一加">一加</a></li>
                                                                <li><a href="//list.jd.com/list.html?cat=9987,653,655&ev=exbrand_25591" target='_blank' title="vivo">vivo</a></li>
                                                                                                <li><a href="//list.jd.com/list.html?cat=9987,653,655" target='_blank' title="更多">更多>></a></li>
                                                                                            </ul>
                        </div>
                    </div>
                </div>
                            </div>
            <div class="item sep">&gt;</div>
                        <div class="item ellipsis" title="华为畅享6">华为畅享6</div>
        </div><!-- .crumb -->

        <div class="contact fr clearfix">
                            <div class="name goodshop EDropdown">
                    <em class="u-jd">
                        <span>JD</span>自营
                    </em>
                </div>
                        <div class="J-hove-wrap EDropdown fr">
                                                <div class="item">
                    <div class="name">
                                                <a href="//huawei.jd.com" target="_blank" title="华为京东自营官方旗舰店" clstag="shangpin|keycount|product|dianpuname1">华为京东自营官方旗舰店</a>
                                            </div>
                </div>
                                <div class="item hide J-im-item">
                    <div class="J-im-btn" clstag="shangpin|keycount|product|dongdong_1"></div>
                </div>
                <div class="item hide J-jimi-item">
                    <div class="J-jimi-btn" clstag="shangpin|keycount|product|jimi_1"></div>
                </div>
                                <div class="item">
                    <div class="follow J-follow-shop" data-vid="1000004259" clstag="shangpin|keycount|product|guanzhu">
                        <i class="sprite-follow"></i><span>关注店铺</span>
                    </div>
                </div>
                                <div class="contact-layer ">
                    <div class="content " data-drop="content">
                        <div class="score-body">
                                                        <div class="pop-shop-im">
                                <div class="hide J-contact-text">客服</div>
                                <div class="hide J-im-item">
                                    <div class="J-im-btn clearfix"></div>
                                </div>
                                <div class="hide J-jimi-item">
                                    <div class="J-jimi-btn clearfix"></div>
                                </div>

                                                            </div>
                            <div class="pop-shop-qr-code J-contact-qrcode clearfix">
                                <div class="qr-code hide J-wd-qrcode">
                                    <img src="//misc.360buyimg.com/lib/img/e/blank.gif" width="78" height="78" alt="关注微店"/>
                                    <p>关注微店</p>
                                </div>
                                <div class="qr-code J-m-qrcode" data-url="https://cd.jd.com/qrcode?skuId=3888216&location=3&isWeChatStock=2">
                                    <div class="J-m-wrap"></div>
                                    <p>手机下单</p>
                                </div>
                            </div>
                            <div class="btns">
                                                                <a href="//huawei.jd.com" target="_blank" class="btn-def enter-shop J-enter-shop" clstag="shangpin|keycount|product|jindian1">
                                    <i class="sprite-enter"></i><span>进店逛逛</span>
                                </a>
                                <span class="separator">|</span>
                                <a href="#none" class="btn-def follow-shop J-follow-shop" data-vid="1000004259" clstag="shangpin|keycount|product|guanzhu1">
                                    <i class="sprite-follow"></i><span>关注店铺</span>
                                </a>
                                                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div><!-- .contact -->

        <div class="clr"></div>
    </div>
</div>

<div class="w">
    <div class="product-intro clearfix">
        <div class="preview-wrap">
            <div class="preview" id="preview">
                                <div id="spec-n1" class="jqzoom main-img" data-big="1" clstag="shangpin|keycount|product|mainpic_1">
                    <ul class="preview-btn J-preview-btn">
                                                                                            </ul>
                    <img id="spec-img" width="450" data-origin="//img11.360buyimg.com/n1/s450x450_jfs/t3637/275/652996370/280419/2a134044/58105e15N75fb0595.jpg" alt="【新年货】华为 畅享6 金色 移动联通电信4G手机 双卡双待">
                                        <i></i>
                                                            <div id="belt"></div>
                </div>
                                            <script>
                (function(doc, cfg) {
                    var img = doc.getElementById('spec-img');
                    var src = img.getAttribute('data-origin');
                    var nsz = 300;

                    if ((!cfg.wideVersion || !cfg.compatible) && !cfg.product.ctCloth) {
                        img.setAttribute('width', nsz);
                        /*img.setAttribute('height', nsz);*/
                        img.setAttribute('src', src.replace('s450x450', 's'+ nsz +'x' + nsz));
                    } else {
                        img.setAttribute('src', src);
                    }

                    if(cfg.product.ctCloth) {
                        if (!cfg.wideVersion || !cfg.compatible) {
                            img.setAttribute('width', nsz);
                        }
                    }
                })(document, pageConfig);
            </script>
            <div class="spec-list" clstag="shangpin|keycount|product|lunbotu_1">
                <a id="spec-forward" href="javascript:;" class="arrow-prev"><i class="sprite-arrow-prev"></i></a>
                <a id="spec-backward" href="javascript:;" class="arrow-next"><i class="sprite-arrow-next"></i></a>
                <div id="spec-list" class="spec-items">
                    <ul class="lh">
                                                                                                                                                <li  class='img-hover'><img alt='【新年货】华为 畅享6 金色 移动联通电信4G手机 双卡双待' src='//img11.360buyimg.com/n5/s54x54_jfs/t3637/275/652996370/280419/2a134044/58105e15N75fb0595.jpg' data-url='jfs/t3637/275/652996370/280419/2a134044/58105e15N75fb0595.jpg' data-img='1' width='54' height='54'></li>
                                                <li ><img alt='【新年货】华为 畅享6 金色 移动联通电信4G手机 双卡双待' src='//img11.360buyimg.com/n5/s54x54_jfs/t3697/87/647818434/172938/25a798fe/58105e19N58917f62.jpg' data-url='jfs/t3697/87/647818434/172938/25a798fe/58105e19N58917f62.jpg' data-img='1' width='54' height='54'></li>
                                                <li ><img alt='【新年货】华为 畅享6 金色 移动联通电信4G手机 双卡双待' src='//img11.360buyimg.com/n5/s54x54_jfs/t3364/209/682238813/177412/e0a59882/58105e1cNfab816f2.jpg' data-url='jfs/t3364/209/682238813/177412/e0a59882/58105e1cNfab816f2.jpg' data-img='1' width='54' height='54'></li>
                                                <li ><img alt='【新年货】华为 畅享6 金色 移动联通电信4G手机 双卡双待' src='//img11.360buyimg.com/n5/s54x54_jfs/t3346/108/621106249/149901/27cda576/58105e1fN440cf37a.jpg' data-url='jfs/t3346/108/621106249/149901/27cda576/58105e1fN440cf37a.jpg' data-img='1' width='54' height='54'></li>
                                                <li ><img alt='【新年货】华为 畅享6 金色 移动联通电信4G手机 双卡双待' src='//img11.360buyimg.com/n5/s54x54_jfs/t3568/33/645616471/141345/6613a544/58105e22Ncf939ce4.jpg' data-url='jfs/t3568/33/645616471/141345/6613a544/58105e22Ncf939ce4.jpg' data-img='1' width='54' height='54'></li>
                                                <li ><img alt='【新年货】华为 畅享6 金色 移动联通电信4G手机 双卡双待' src='//img11.360buyimg.com/n5/s54x54_jfs/t3451/292/636496916/239681/37f48c17/58105e34Naab1186c.jpg' data-url='jfs/t3451/292/636496916/239681/37f48c17/58105e34Naab1186c.jpg' data-img='1' width='54' height='54'></li>
                                                <li ><img alt='【新年货】华为 畅享6 金色 移动联通电信4G手机 双卡双待' src='//img11.360buyimg.com/n5/s54x54_jfs/t3427/233/660473690/178101/ac72933d/58105e38N5fee2bf5.jpg' data-url='jfs/t3427/233/660473690/178101/ac72933d/58105e38N5fee2bf5.jpg' data-img='1' width='54' height='54'></li>
                                                <li ><img alt='【新年货】华为 畅享6 金色 移动联通电信4G手机 双卡双待' src='//img11.360buyimg.com/n5/s54x54_jfs/t3766/68/687577971/180767/1d7762f3/58105e3bN2c1c857e.jpg' data-url='jfs/t3766/68/687577971/180767/1d7762f3/58105e3bN2c1c857e.jpg' data-img='1' width='54' height='54'></li>
                                                                    </ul>
                </div>
            </div>
            <div class="preview-info">
                <div class="left-btns">
                    <a class="follow J-follow" data-id="3888216" href="#none" clstag="shangpin|keycount|product|guanzhushangpin_1">
                        <i class="sprite-follow-sku"></i><em>关注</em>
                    </a>
                    <a class="share J-share" href="#none" clstag="shangpin|keycount|product|share_1">
                        <i class="sprite-share"></i><em>分享</em>
                    </a>
                                                            <a class="compare J-compare J_contrast" id="comp_3888216" data-sku="3888216" href="#none" clstag="shangpin|keycount|product|jiaruduibi">
                        <i class="sprite-compare"></i><em>对比</em>
                    </a>
                                    </div>
                <div class="right-btns">
                    <a class="report-btn" href="//jubao.jd.com/index.html?skuId=3888216" target="_blank" clstag="shangpin|keycount|product|jubao">举报</a>
                </div>
            </div>

                            </div>
            </div>
            <div class="itemInfo-wrap">
                <div class="sku-name">
                                        【新年货】华为 畅享6 金色 移动联通电信4G手机 双卡双待                </div>
                        <div class="news">
            <div class="item hide" id="p-ad" clstag="shangpin|keycount|product|slogana" data-hook="hide"></div>
            <div class="item hide" id="p-ad-phone" clstag="shangpin|keycount|product|sloganb" data-hook="hide"></div>
        </div>

                                <div class="activity-banner  J-seckill" id="banner-miaosha" style="display:none">
            <div class="activity-type">
                <i class=""></i><strong>京东秒杀</strong>
            </div>
            <div class="activity-message">
            </div>
        </div>
                <div class="summary summary-first">
            <div class="summary-price-wrap">
                                    <div class="summary-price J-summary-price">
                                                <div class="dt">秒 杀 价 </div>
                        <div class="dd">
                            <span class="p-price"><span>￥</span><span class="price J-p-3888216"></span></span>
                                                        <span class="pricing">[<del id="page_origin_price">￥699</del>]</span>
                                                                                    <a class="notice J-notify-sale" data-type="1" data-sku="3888216" href="#none" clstag="shangpin|keycount|product|jiangjia_1">降价通知</a>
                                                                                    <!-- 高端品 限时特惠start，这段代码中的样式，是需要改的，请前端同学定义样式。还有用js代码，完成对应的需求 -->
                            <span class="J-xsth-sale" style="display: none;">
                                    <a href="#none" class="J-xsth-panel" clstag="shangpin|keycount|product|xianshitehui">限时特惠<s class="s-arrow">></s></a>
                                    <i class="sprite-question"></i>
                                </span>
                            <!-- 高端品 限时特惠end -->

                                                                                    
                                                                                                                                            <div class="plus-price J-plus-price hide" style="display: none;">
                                    <span class="p-price-plus">
                                        <span class="price J-p-p-3888216"></span>
                                    </span>
                                <img src="//img10.360buyimg.com/da/jfs/t5731/317/890792506/848/391b9a15/59224a28N48552ed2.png" alt="plus" class="plus-icon">
                                <span class="text"><strong>PLUS会员</strong>专享价</span>
                                <a clstag="shangpin|keycount|product|whatisplus" href="//plus.jd.com/index" target="_blank">银牌及以上用户开通PLUS可享限时特惠 >></a>
                            </div>
                                                                                    <div class="user-price J-user-price hide" style="display: none;">
                                    <span class="p-price-user">
                                        <span class="price J-p-s-3888216"></span>
                                    </span>
                                <img src="//img14.360buyimg.com/devfe/jfs/t5728/113/4603623007/244/a159e46d/59535259N6eed475d.png" alt="sam's" class="sam-icon">

                                <span class="text">您购买此商品可享受专属价</span>

                                <i class="sprite-question"></i>
                            </div>
                                                    </div>
                    </div>

                    <!-- 分期用分区价格展示需求 start -->
                                        <!-- 分期用分区价格展示需求 end -->

                                        <div class="summary-info J-summary-info clearfix">
                        <div id="comment-count" class="comment-count item fl" clstag="shangpin|keycount|product|pingjiabtn_1">
                            <p class="comment">累计评价</p>
                            <a class="count J-comm-3888216" href="#comment">0</a>
                        </div>
                                                                    </div>
                                                                                                                        <div id="summary-quan" class="li p-choose hide" clstag="shangpin|keycount|product|lingquan"></div>
                                        <div id="J-summary-top" class="summary-top" clstag="shangpin|keycount|product|cuxiao">
                        <div id="summary-promotion" class="summary-promotion" data-hook="hide">
                            <div class="dt">促&#x3000;&#x3000;销</div>
                            <div class="dd J-prom-wrap p-promotions-wrap">
                                <div class="p-promotions">
                                    <ins id="prom-mbuy" data-url="https://cd.jd.com/qrcode?skuId=3888216&location=3&isWeChatStock=2"></ins>
                                    <ins id="prom-car-gift"></ins>
                                    <ins id="prom-gift" clstag="shangpin|keycount|product|zengpin_1"></ins>
                                    <ins id="prom-fujian" clstag="shangpin|keycount|product|fujian_1"></ins>
                                    <ins id="prom"></ins>
                                    <ins id="prom-one"></ins>
                                    <ins id="prom-phone"></ins>
                                    <ins id="prom-phone-jjg"></ins>
                                    <ins id="prom-tips"></ins>
                                    <ins id="prom-quan"></ins>
                                    <div class="J-prom-more view-all-promotions" data-hook="hide">
                                        <span class="prom-sum">展开促销</span>
                                        <a href="#none" class="view-link"><i class="sprite-arr-close"></i></a>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <div class="summary p-choose-wrap">
                                                       <div id="summary-support" class="li hide">
                    <div class="dt">增值业务</div>
                    <div class="dd">
                        <ul class="choose-support lh">
                        </ul>
                    </div>
                </div>
                <div class="summary-stock" clstag="shangpin|keycount|product|quyuxuanze_1" >
                    <div class="dt">配 送 至</div>
                    <div class="dd">
                        <div class="store clearfix">
                            <div id="stock-address" class="stock-address EDropdown" data-role="drop">
                                <div class="inner">
                                    <div data-drop="head" class="head">
                                        <span class="text" data-res>请选择</span>
                                        <span class="arrow arr-close"></span>
                                    </div>
                                    <div data-drop="content" class="content hide">
                                        <!--<div class="close" data-close>x</div>-->
                                        <dl class="address-used hide">
                                            <dt data-drop="head"><strong>常用地址</strong><span class="arrow"></span></dt>
                                            <dd class="stock-address-list J-common-address hide" clstag="shangpin|keycount|product|morendizhi_1"></dd>
                                        </dl>
                                        <div class="line hide"></div>
                                        <dl class="address-select clicked">
                                            <dt data-drop="head"><strong>选择新地址</strong><span class="arrow"></span></dt>
                                            <dd class="stock-address-list hide">
                                                <div class="address-tab J-address-tab ETab">
                                                    <ul class="tab">
                                                        <li data-tab="trigger" class="current" clstag="shangpin|keycount|product|yijidizhi">请选择</li>
                                                        <li data-tab="trigger" clstag="shangpin|keycount|product|erjidizhi">请选择</li>
                                                        <li data-tab="trigger" clstag="shangpin|keycount|product|sanjidizhi">请选择</li>
                                                        <li data-tab="trigger" style="display:none" clstag="shangpin|keycount|product|sijidizhi">请选择</li>
                                                    </ul>
                                                    <div class="tab-con">
                                                        <div data-tab="item" data-level="0" clstag="shangpin|keycount|product|yijidizhi_1">请选择</div>
                                                        <div data-tab="item" data-level="1" class="hide" clstag="shangpin|keycount|product|erjidizhi_1">请选择</div>
                                                        <div data-tab="item" data-level="2" class="hide" clstag="shangpin|keycount|product|sanjidizhi_1">请选择</div>
                                                        <div data-tab="item" data-level="3" class="hide" clstag="shangpin|keycount|product|sijidizhi_1">请选择</div>
                                                    </div>
                                                </div>
                                            </dd>
                                        </dl>
                                    </div>
                                </div>
                            </div>
                            <div id="store-prompt" class="store-prompt"></div>
                            <div class="J-promise-icon promise-icon fl promise-icon-more" clstag="shangpin|keycount|product|promisefw_1">
                                <div class="title fl">支持</div>
                                <div class="icon-list fl">
                                    <ul></ul>
                                    <span class="clr"></span>
                                </div>
                            </div>
                            <div class="J-dcashDesc dcashDesc fl"></div>
                        </div>
                    </div>
                </div>
                                                <div id="summary-supply" class="li" style="display:none">
                    <div class="dt">&#x3000;&#x3000;</div>
                    <div class="dd">
                        <div id="summary-service" class="summary-service"  clstag="shangpin|keycount|product|fuwu_1"></div>
                    </div>
                </div>
                                                <div id="summary-weight" class="li" style="display:none">
                    <div class="dt">重&#x3000;&#x3000;量</div>
                    <div class="dd"></div>
                </div>

                                <div class="summary-line"></div>
                                                                                                                                        <div id="choose-attrs">
                                                                                <div id="choose-attr-1" class="li p-choose" data-type="颜色" data-idx="0">
                        <div class="dt">选择颜色</div>
                        <div class="dd">
                                                        <div class="item  selected  " data-sku="4577199" data-value="金色">
                                <b></b>
                                                                <a href="#none" clstag="shangpin|keycount|product|yanse-金色">
                                                                                                            <img data-img="1" src="//img14.360buyimg.com/n9/s40x40_jfs/t5935/263/7096608000/1366888/e8860080/59793d46N50bf5336.jpg" width="40" height="40" alt="金色"><i>金色</i>
                                                                                                        </a>
                                                            </div>
                                                        <div class="item  " data-sku="5305784" data-value="白色">
                                <b></b>
                                                                <a href="#none" clstag="shangpin|keycount|product|yanse-白色">
                                                                                                            <img data-img="1" src="//img14.360buyimg.com/n9/s40x40_jfs/t6850/289/737192940/861204/cb476eed/59794799N17e25bb4.jpg" width="40" height="40" alt="白色"><i>白色</i>
                                                                                                        </a>
                                                            </div>
                                                        <div class="item  " data-sku="3458011" data-value="灰色">
                                <b></b>
                                                                <a href="#none" clstag="shangpin|keycount|product|yanse-灰色">
                                                                                                            <img data-img="1" src="//img11.360buyimg.com/n9/s40x40_jfs/t3805/305/404016366/303918/8231e4d6/58105e5eN0c217e5e.jpg" width="40" height="40" alt="灰色"><i>灰色</i>
                                                                                                        </a>
                                                            </div>
                                                    </div>
                    </div>
                                                                                                    <div id="choose-attr-2" class="li p-choose" data-type="版本" data-idx="1">
                        <div class="dt">选择版本</div>
                        <div class="dd">
                                                        <div class="item  selected  " data-sku="3458011" data-value="全网通">
                                <b></b>
                                                                <a href="#none" clstag="shangpin|keycount|product|yanse-全网通">
                                                                        全网通                                                                    </a>
                                                            </div>
                                                        <div class="item  " data-sku="4577199" data-value="移动定制版">
                                <b></b>
                                                                <a href="#none" clstag="shangpin|keycount|product|yanse-移动定制版">
                                                                        移动定制版                                                                    </a>
                                                            </div>
                                                    </div>
                    </div>
                                                                                <div id="choose-results" class="li" style="display:none"><div class="dt">已选择</div><div class="dd"></div></div>
                                    </div>

                                                
                                                                                                <div id="choose-luodipei" class="choose-luodipei li" style="display:none">
                    <div class="dt">送装服务</div>
                    <div class="dd"></div>
                </div>
                                <div id="choose-type" class="li" data-hook="hide" style="display:none;">
                    <div class="dt">购买方式</div>
                    <div class="dd clearfix"> </div>
                </div>
                <div id="choose-type-hy" class="li" data-hook="hide" style="display:none;">
                    <div class="dt">优惠类型</div>
                    <div class="dd clearfix"> </div>
                </div>
                <div id="choose-type-suit" class="li" data-hook="hide" style="display:none;">
                    <div class="dt">优惠套餐</div>
                    <div class="dd clearfix">
                        <div class="item J-suit-trigger" clstag="shangpin|keycount|product|taocanleixing">
                            <i class="sprite-selected"></i>
                            <a href="#none" title="选择套餐与资费">选择套餐与资费</a>
                        </div>
                        <div class="fl" style="padding-top:5px;">
                            <span class="J-suit-tips hide">请选择套餐内容</span>
                            <span class="J-suit-resel J-suit-trigger hl_blue hide" href="#none">重选</span>
                        </div>
                    </div>
                </div>
                <div id="btype-tip" data-hook="hide" style="display:none;">&#x3000;您选择的地区暂不支持合约机销售！</div>
                                                                <div id="choose-suits" class="li choose-suits" style="display:none">
                    <div class="dt">套&#x3000;&#x3000;装</div>
                    <div class="dd clearfix"></div>
                </div>
                                <div id="choose-gift" class="choose-gift li"  style="display: none;">
                    <div class="dt">搭配赠品</div>
                    <div class="dd clearfix">
                        <div class="gift J-gift" clstag="shangpin|keycount|product|dapeizengpin">
                            <i class="sprite-gift J-popup"></i><span class="gift-tips">选择搭配赠品(共<em>0</em>个)</span>
                        </div>
                        <!--choosed-->
                        <div class="J-gift-selected hide">
                            <div class="gift choosed J-gift-choosed"></div>
                            <a href="#none" class="gift-modify J-popup" clstag="shangpin|keycount|product|zengpin-genggai">更改</a>
                        </div>
                    </div>
                </div>

                                                <div id="choose-service" class="li" data-hook="hide" style="display:none;">
                    <div class="dt" data-yb="new_yb_server"></div>
                    <div class="dd"></div>
                </div>
                                                                                <div id="choose-baitiao" class="li choose-baitiao" style="display:none"></div>
                                <div id="choose-jincai" class="li choose-jincai" style="display:none">
                    <div class="dt">企业金采</div>
                    <div class="dd">
                        <div class="jincai-list J-jincai-list">
                            <div class="item">
                                <a href="#none">先采购，后付款</a>
                            </div>
                            <div class="bt-info-tips">
                                <a class="J-bt-tips question icon fl" href="#none">　</a>
                            </div>
                        </div>
                    </div>
                </div>
                                                                                                                  <div class="summary-line"></div>
                                <div id="choose-btns" class="choose-btns clearfix" >
                                        <div class="choose-amount "  clstag="shangpin|keycount|product|goumaishuliang_1">
                    <div class="wrap-input">
                        <input class="text buy-num" onkeyup="setAmount.modify('#buy-num');" id="buy-num" value="1"  data-max="200"/>
                        <a class="btn-reduce" onclick="setAmount.reduce('#buy-num')" href="#none">-</a>
                        <a class="btn-add" onclick="setAmount.add('#buy-num')" href="#none">+</a>
                    </div>
                </div>
                <!--<a id="choose-btn-gift" class="btn-special1 btn-lg" style="display:none;" href="//cart.gift.jd.com/cart/addGiftToCart.action?pid=3888216&pcount=1&ptype=1" class="btn-gift" clstag="shangpin|keycount|product|选作礼物购买_1"><b></b>选作礼物购买</a>-->

                                                                                                <a href="#none" id="btn-heyue" class="btn-special1 btn-lg" style="display:none;" clstag="shangpin|keycount|product|选择号码和套餐_1">选择号码和套餐</a>
                                                                                <a href="//cart.jd.com/gate.action?pid=3888216&pcount=1&ptype=1" id="InitCartUrl" class="btn-special1 btn-lg "  clstag="shangpin|keycount|product|加入购物车_1">加入购物车</a>
                                                                                <a href="#none" id="btn-baitiao" class="btn-special2 btn-lg" style="display:none;" clstag="shangpin|keycount|product|dabaitiaobutton_9987_653_655">打白条</a>
                <a href="//jc.jd.com" target="_blank" id="btn-jincai" class="btn-special2 btn-lg" style="display: none;" clstag="shangpin|keycount|product|jincai_1">使用金采</a>

                                    <a href="#none" id="btn-onkeybuy" class="btn-special2 btn-lg" style="display:none;" clstag="shangpin|keycount|product|easybuy_1">一键购</a>
                                                
                                <a href="#none" id="btn-notify" class="J-notify-stock btn-special3 btn-lg notify-stock" style="display:none;" data-type="2" data-sku="3888216" clstag="shangpin|keycount|product|daohuo_1">到货通知</a>
                                                                                            </div>
                        <div id="local-tips" class="summary-tips hide">
                <div class="dt">本地活动</div>
                <div class="dd">
                    <ol class="tips-list clearfix"></ol>
                </div>
            </div>
                                                <div id="summary-tips" class="summary-tips" clstag="shangpin|keycount|product|wenxintishi_1" style="display: none">
                <div class="dt">温馨提示</div>
                <div class="dd">
                    <ol class="tips-list clearfix">
                    </ol>
                </div>
            </div>
                                            </div>
            </div>
        </div>
</div>


<div class="w">
    <div class="m m-content hide" id="similar">
        <div class="mt">
            <h3 class="fl">为你推荐</h3>
            <div class="extra">
                <div class="page-num"></div>
            </div>
        </div>
        <div class="mc">
            <a href="#none" class="arrow-prev disabled"><i class="sprite-arrow-prev"></i></a>
            <div class="list clearfix"></div>
            <a href="#none" class="arrow-next disabled"><i class="sprite-arrow-next"></i></a>
        </div>
    </div>
</div>



<div class="w">
    <div id="fittings" class="fittings ETab hide">
        <div class="tab-main large">
            <ul>
                <li data-tab="trigger" class="current" data-name="人气配件" onclick='log("gz_item", "gz_detail","02","tjpj_pjfl_人气配件","","main")'>人气配件</li>
            </ul>
            <div class="extra"></div>
        </div>
        <div class="tab-con J_fitting_con clearfix">
            <div class="master">
                <div class="p-list">
                    <div class="p-img">
                        <a href="//jd.com/" target="_blank">
                            <img data-img="1" src="//img14.360buyimg.com/n4/jfs/t3637/275/652996370/280419/2a134044/58105e15N75fb0595.jpg" width="100" height="100" alt="【新年货】华为 畅享6 金色 移动联通电信4G手机 双卡双待"/>
                        </a>
                    </div>
                    <div class="p-name">
                        <a href="//item.jd.com/3888216.html" target="_blank">【新年货】华为 畅享6 金色 移动联通电信4G手机 双卡双待</a>
                    </div>
                    <div class="p-price hide">
                        <input type="checkbox" data-sku="3888216" id="inp-acc-master" checked/>
                        <label for="inp-acc-master"><strong class="J-p-3888216">￥</strong></label>
                    </div>
                    <i class="plus">+</i>
                </div>
            </div>
            <div class="suits">
                <div class="switchable-wrap" data-tab="item">
                    <div class="btns">
                        <a href="javascript:void(0)" target="_self" class="prev-btn"></a>
                        <a href="javascript:void(0)" target="_self" class="next-btn"></a>
                    </div>
                    <div class="lh-wrap">
                        <ul class="lh clearfix"></ul>
                    </div>
                </div>
            </div>

            <div class="infos">
                <div class="selected">已选择<em class="J-selected-cnt">0</em>个配件</div>
                <div class="p-price">
                    <span>组合价</span>
                    <strong class="J_cal_jp">￥暂无报价</strong>
                </div>
                <div class="btn">
                    <a href="#none" class="btn-primary J-btn" target="_blank" onclick='log("gz_item", "gz_detail","02","tjpj_ycgm_ljgm", pageConfig.getAccSelectedSkus(),"main")'>立即购买</a>
                </div>
                                                <a href="//kong.jd.com/index?sku=3888216&cid=655" target="_blank" class="acc-buy-center" onclick='log("gz_item", "gz_detail","02","tjpj_gdpj","","main")'>配件选购中心</a>
                                <i class="equal">=</i>
            </div>
        </div>
    </div>
</div>
<div class="w">
           <div id="shopRecSuit" class="ETab hide" >
        <div class="tab-main large">
            <ul>
                <li data-tab="trigger" class="J-shopRec-trigger shopRec-trigger current hide" data-name="店长推荐">店长推荐</li>
            </ul>
        </div>
        <div class="tab-con clearfix">
            <div class="J-shopRec-content shopRec-content hide" data-tab="item" clstag="shangpin|keycount|product|dianzhangtuijian_2">
                            </div>
        </div>
    </div>
    </div>

<div class="w">
    <div class="aside">
                                <div class="m m-aside popbox" id="popbox">
            <div class="popbox-inner" data-fixed="pro-detail-hd-fixed">
    <div class="mt">
        <h3>
                        <a href="//huawei.jd.com" target="_blank" title="华为京东自营官方旗舰店" clstag="shangpin|keycount|product|dianpuname2_华为京东自营官方旗舰店">华为京东自营官方旗舰店</a>
                                </h3>
                <div class="im-wrap clearfix">
            <a class="J-popbox-im im" title="联系供应商" data-code="1" data-name="联系供应商" data-seller="联系供应商" data-domain="chat.jd.com" clstag="shangpin|keycount|product|dongdong2_1"><i
                    class="sprite-im"></i></a>
        </div>
                        <span class="arrow"></span>
            </div>
        <div class="mc">
        <div class="pop-score-summary">
            <div class="btns">
                <a href="//huawei.jd.com" target="_blank" class="btn-def enter-shop J-enter-shop" clstag="shangpin|keycount|product|jindian2">
                    <i class="sprite-enter"></i>
                    <span>进店逛逛</span>
                </a>
                <a href="#none" class="btn-def follow-shop J-follow-shop" data-vid="1000004259" clstag="shangpin|keycount|product|guanzhu2">
                    <i class="sprite-follow"> </i>
                    <span>关注店铺</span>
                </a>
            </div>
        </div>
    </div>
    </div>
        </div>
                                                <div class="m m-aside" id="seek" clstag="shangpin|keycount|product|fanxiangdaogou_1">
            <div class="mt">
                <h3>关于手机，你可能在找</h3>
            </div>
            <div class="mc">
                <ul class="tag-list">
                                                            <li>
                                                <a href='//search.jd.com/Search?keyword=%E5%8D%8E%E4%B8%BA%EF%BC%88HUAWEI%EF%BC%89%20%E5%AE%89%E5%8D%93%EF%BC%88Android%EF%BC%89&enc=utf-8&cid3=655' target='_blank'>安卓（Android）</a>
                                            </li>
                                                            <li>
                                                <a href='//search.jd.com/Search?keyword=%E5%8D%8E%E4%B8%BA%EF%BC%88HUAWEI%EF%BC%89%205.0-4.6%E8%8B%B1%E5%AF%B8&enc=utf-8&cid3=655' target='_blank'>5.0-4.6英寸</a>
                                            </li>
                                                            <li>
                                                <a href='//search.jd.com/Search?keyword=%E5%8D%8E%E4%B8%BA%EF%BC%88HUAWEI%EF%BC%89%20%E8%81%94%E9%80%9A4G&enc=utf-8&cid3=655' target='_blank'>联通4G</a>
                                            </li>
                                                            <li>
                                                <a href='//search.jd.com/Search?keyword=%E5%8D%8E%E4%B8%BA%EF%BC%88HUAWEI%EF%BC%89%20%E7%94%B5%E4%BF%A14G&enc=utf-8&cid3=655' target='_blank'>电信4G</a>
                                            </li>
                                                            <li>
                                                <a href='//search.jd.com/Search?keyword=%E5%8D%8E%E4%B8%BA%EF%BC%88HUAWEI%EF%BC%89%20%E7%A7%BB%E5%8A%A84G%2F%E8%81%94%E9%80%9A4G%2F%E7%94%B5%E4%BF%A14G&enc=utf-8&cid3=655' target='_blank'>移动4G/联通4G/电信4G</a>
                                            </li>
                                                            <li>
                                                <a href='//search.jd.com/Search?keyword=%E5%8D%8E%E4%B8%BA%EF%BC%88HUAWEI%EF%BC%89%20%E7%A7%BB%E5%8A%A84G&enc=utf-8&cid3=655' target='_blank'>移动4G</a>
                                            </li>
                                                            <li>
                                                <a href='//search.jd.com/Search?keyword=%E5%8D%8E%E4%B8%BA%EF%BC%88HUAWEI%EF%BC%89%203GB&enc=utf-8&cid3=655' target='_blank'>3GB</a>
                                            </li>
                                                            <li>
                                                <a href='//search.jd.com/Search?keyword=%E5%8D%8E%E4%B8%BA%EF%BC%88HUAWEI%EF%BC%89%20%E5%85%AB%E6%A0%B8&enc=utf-8&cid3=655' target='_blank'>八核</a>
                                            </li>
                                    </ul>
            </div>
        </div>
                        <div class="m m-aside hide" id="view-buy" clstag="shangpin|keycount|product|darenxuangou_1"></div>

                        <div class="m m-aside" id="view-view" clstag="shangpin|keycount|product|seemore_1"></div>
                                        <div class="m m-aside" id="rank">
            <div class="mt">
                <h3>手机热销榜</h3>
            </div>
            <div class="mc no-padding">
                <div class="ETab">
                    <div class="tab-main medium">
                        <ul>
                            <li data-tab="trigger" class="current">同价位</li>
                            <li data-tab="trigger">同品牌</li>
                            <li data-tab="trigger">总排行</li>
                        </ul>
                    </div>
                    <div class="tab-con">
                        <div data-tab="item">
                                                        <ul class="plist-1" clstag="shangpin|keycount|product|rexiaobang_price_655">
                                                                <li class="fore1" data-sku="5835261">
                                    <div class="p-img"><a href="//item.jd.com/5835261.html" target="_blank"><img data-img="1" height="85" width="85"  data-lazyload="//img11.360buyimg.com/n5/s85x85_jfs/t15775/364/150916311/324587/3b5a727/5a28b5a1N8a5c095f.jpg"/></a></div>
                                    <div class="p-name"><a href="//item.jd.com/5835261.html" target="_blank" title='小米红米5 Plus'>小米红米5 Plus</a></div>
                                    <div class="p-price"><strong class="J-p-5835261"></strong></div>
                                    <div class="p-num">1</div>
                                </li>
                                                                <li class="fore2" data-sku="4787565">
                                    <div class="p-img"><a href="//item.jd.com/4787565.html" target="_blank"><img data-img="1" height="85" width="85"  data-lazyload="//img10.360buyimg.com/n5/s85x85_jfs/t7366/351/1158159113/342659/850e3d95/599adf11Nc6ec37b7.jpg"/></a></div>
                                    <div class="p-name"><a href="//item.jd.com/4787565.html" target="_blank" title='小米红米Note5A'>小米红米Note5A</a></div>
                                    <div class="p-price"><strong class="J-p-4787565"></strong></div>
                                    <div class="p-num">2</div>
                                </li>
                                                                <li class="fore3" data-sku="3755813">
                                    <div class="p-img"><a href="//item.jd.com/3755813.html" target="_blank"><img data-img="1" height="85" width="85"  data-lazyload="//img13.360buyimg.com/n5/s85x85_jfs/t3688/211/2249892071/336862/d776c56e/584f5935N31fa3fd4.jpg"/></a></div>
                                    <div class="p-name"><a href="//item.jd.com/3755813.html" target="_blank" title='华为畅享6S'>华为畅享6S</a></div>
                                    <div class="p-price"><strong class="J-p-3755813"></strong></div>
                                    <div class="p-num">3</div>
                                </li>
                                                                <li class="fore4" data-sku="5835285">
                                    <div class="p-img"><a href="//item.jd.com/5835285.html" target="_blank"><img data-img="1" height="85" width="85"  data-lazyload="//img10.360buyimg.com/n5/s85x85_jfs/t15907/320/109431190/305235/572b49b4/5a28b4cdNc5c0694e.jpg"/></a></div>
                                    <div class="p-name"><a href="//item.jd.com/5835285.html" target="_blank" title='小米红米5'>小米红米5</a></div>
                                    <div class="p-price"><strong class="J-p-5835285"></strong></div>
                                    <div class="p-num">4</div>
                                </li>
                                                                <li class="fore5" data-sku="3893499">
                                    <div class="p-img"><a href="//item.jd.com/3893499.html" target="_blank"><img data-img="1" height="85" width="85"  data-lazyload="//img14.360buyimg.com/n5/s85x85_jfs/t6205/223/1653756309/269723/b3c43437/5955c79bN016acbc3.jpg"/></a></div>
                                    <div class="p-name"><a href="//item.jd.com/3893499.html" target="_blank" title='华为 畅享7'>华为 畅享7</a></div>
                                    <div class="p-price"><strong class="J-p-3893499"></strong></div>
                                    <div class="p-num">5</div>
                                </li>
                                                                <li class="fore6" data-sku="3846673">
                                    <div class="p-img"><a href="//item.jd.com/3846673.html" target="_blank"><img data-img="1" height="85" width="85"  data-lazyload="//img13.360buyimg.com/n5/s85x85_jfs/t6553/346/1473938601/145939/f7796bfa/59521206N527bb108.jpg"/></a></div>
                                    <div class="p-name"><a href="//item.jd.com/3846673.html" target="_blank" title='小米红米Note4X'>小米红米Note4X</a></div>
                                    <div class="p-price"><strong class="J-p-3846673"></strong></div>
                                    <div class="p-num">6</div>
                                </li>
                                                                <li class="fore7" data-sku="5143886">
                                    <div class="p-img"><a href="//item.jd.com/5143886.html" target="_blank"><img data-img="1" height="85" width="85"  data-lazyload="//img11.360buyimg.com/n5/s85x85_jfs/t5878/302/2473394232/308597/1319a39/59312053N69739c6c.jpg"/></a></div>
                                    <div class="p-name"><a href="//item.jd.com/5143886.html" target="_blank" title='华为荣耀畅玩6A'>华为荣耀畅玩6A</a></div>
                                    <div class="p-price"><strong class="J-p-5143886"></strong></div>
                                    <div class="p-num">7</div>
                                </li>
                                                            </ul>
                                                    </div>
                        <div data-tab="item" class="hide">
                                                        <ul class="plist-1" clstag="shangpin|keycount|product|rexiaobang_brand_655">
                                                                <li class="fore1" data-sku="5295423">
                                    <div class="p-img"><a href="//item.jd.com/5295423.html" target="_blank"><img data-img="1" height="85" width="85"  data-lazyload="//img13.360buyimg.com/n5/s85x85_jfs/t10159/363/1183140024/256693/980afae7/59ddcd8cN50a50637.jpg"/></a></div>
                                    <div class="p-name"><a href="//item.jd.com/5295423.html" target="_blank" title='华为荣耀7X'>华为荣耀7X</a></div>
                                    <div class="p-price"><strong class="J-p-5295423"></strong></div>
                                    <div class="p-num">1</div>
                                </li>
                                                                <li class="fore2" data-sku="5005725">
                                    <div class="p-img"><a href="//item.jd.com/5005725.html" target="_blank"><img data-img="1" height="85" width="85"  data-lazyload="//img10.360buyimg.com/n5/s85x85_jfs/t11626/86/689371235/67431/a2514630/59f5eef1N99542494.jpg"/></a></div>
                                    <div class="p-name"><a href="//item.jd.com/5005725.html" target="_blank" title='华为荣耀V9 play'>华为荣耀V9 play</a></div>
                                    <div class="p-price"><strong class="J-p-5005725"></strong></div>
                                    <div class="p-num">2</div>
                                </li>
                                                                <li class="fore3" data-sku="6008133">
                                    <div class="p-img"><a href="//item.jd.com/6008133.html" target="_blank"><img data-img="1" height="85" width="85"  data-lazyload="//img13.360buyimg.com/n5/s85x85_jfs/t12607/160/2542824776/353795/da2168a0/5a434302Nb0cd1c6c.jpg"/></a></div>
                                    <div class="p-name"><a href="//item.jd.com/6008133.html" target="_blank" title='华为荣耀9青春版'>华为荣耀9青春版</a></div>
                                    <div class="p-price"><strong class="J-p-6008133"></strong></div>
                                    <div class="p-num">3</div>
                                </li>
                                                                <li class="fore4" data-sku="5821455">
                                    <div class="p-img"><a href="//item.jd.com/5821455.html" target="_blank"><img data-img="1" height="85" width="85"  data-lazyload="//img10.360buyimg.com/n5/s85x85_jfs/t13084/76/1267962766/310543/df0a46d8/5a1d1d8aN30671ab7.jpg"/></a></div>
                                    <div class="p-name"><a href="//item.jd.com/5821455.html" target="_blank" title='华为荣耀V10'>华为荣耀V10</a></div>
                                    <div class="p-price"><strong class="J-p-5821455"></strong></div>
                                    <div class="p-num">4</div>
                                </li>
                                                                <li class="fore5" data-sku="4241985">
                                    <div class="p-img"><a href="//item.jd.com/4241985.html" target="_blank"><img data-img="1" height="85" width="85"  data-lazyload="//img10.360buyimg.com/n5/s85x85_jfs/t6328/246/364913906/80331/7a647145/593e4f61N73cf7cb5.jpg"/></a></div>
                                    <div class="p-name"><a href="//item.jd.com/4241985.html" target="_blank" title='华为荣耀9'>华为荣耀9</a></div>
                                    <div class="p-price"><strong class="J-p-4241985"></strong></div>
                                    <div class="p-num">5</div>
                                </li>
                                                                <li class="fore6" data-sku="3652063">
                                    <div class="p-img"><a href="//item.jd.com/3652063.html" target="_blank"><img data-img="1" height="85" width="85"  data-lazyload="//img13.360buyimg.com/n5/s85x85_jfs/t3502/149/1442706783/302122/91048536/5825a5a6Nde8ecb75.jpg"/></a></div>
                                    <div class="p-name"><a href="//item.jd.com/3652063.html" target="_blank" title='华为荣耀畅玩6X'>华为荣耀畅玩6X</a></div>
                                    <div class="p-price"><strong class="J-p-3652063"></strong></div>
                                    <div class="p-num">6</div>
                                </li>
                                                                <li class="fore7" data-sku="5284203">
                                    <div class="p-img"><a href="//item.jd.com/5284203.html" target="_blank"><img data-img="1" height="85" width="85"  data-lazyload="//img13.360buyimg.com/n5/s85x85_jfs/t10414/363/1280355182/335902/18c2b152/59ded64fNfdb4e9da.jpg"/></a></div>
                                    <div class="p-name"><a href="//item.jd.com/5284203.html" target="_blank" title='华为Mate 10'>华为Mate 10</a></div>
                                    <div class="p-price"><strong class="J-p-5284203"></strong></div>
                                    <div class="p-num">7</div>
                                </li>
                                                            </ul>
                                                    </div>
                        <div data-tab="item" class="hide">
                                                        <ul class="plist-1" clstag="shangpin|keycount|product|rexiaobang_all_655">
                                                                <li class="fore1" data-sku="5835261">
                                    <div class="p-img"><a href="//item.jd.com/5835261.html" target="_blank"><img data-img="1" height="85" width="85"  data-lazyload="//img11.360buyimg.com/n5/s85x85_jfs/t15775/364/150916311/324587/3b5a727/5a28b5a1N8a5c095f.jpg"/></a></div>
                                    <div class="p-name"><a href="//item.jd.com/5835261.html" target="_blank" title='小米红米5 Plus'>小米红米5 Plus</a></div>
                                    <div class="p-price"><strong class="J-p-5835261"></strong></div>
                                    <div class="p-num">1</div>
                                </li>
                                                                <li class="fore2" data-sku="6008133">
                                    <div class="p-img"><a href="//item.jd.com/6008133.html" target="_blank"><img data-img="1" height="85" width="85"  data-lazyload="//img13.360buyimg.com/n5/s85x85_jfs/t12607/160/2542824776/353795/da2168a0/5a434302Nb0cd1c6c.jpg"/></a></div>
                                    <div class="p-name"><a href="//item.jd.com/6008133.html" target="_blank" title='华为荣耀9青春版'>华为荣耀9青春版</a></div>
                                    <div class="p-price"><strong class="J-p-6008133"></strong></div>
                                    <div class="p-num">2</div>
                                </li>
                                                                <li class="fore3" data-sku="4230903">
                                    <div class="p-img"><a href="//item.jd.com/4230903.html" target="_blank"><img data-img="1" height="85" width="85"  data-lazyload="//img13.360buyimg.com/n5/s85x85_jfs/t7810/207/4346108049/288516/48ea4d34/5a0524e7N1e10fca3.jpg"/></a></div>
                                    <div class="p-name"><a href="//item.jd.com/4230903.html" target="_blank" title='小米小米Note3'>小米小米Note3</a></div>
                                    <div class="p-price"><strong class="J-p-4230903"></strong></div>
                                    <div class="p-num">3</div>
                                </li>
                                                                <li class="fore4" data-sku="4230887">
                                    <div class="p-img"><a href="//item.jd.com/4230887.html" target="_blank"><img data-img="1" height="85" width="85"  data-lazyload="//img12.360buyimg.com/n5/s85x85_jfs/t9646/2/1649720481/166080/e96a680b/59e45be1Nec376639.jpg"/></a></div>
                                    <div class="p-name"><a href="//item.jd.com/4230887.html" target="_blank" title='小米红米5A'>小米红米5A</a></div>
                                    <div class="p-price"><strong class="J-p-4230887"></strong></div>
                                    <div class="p-num">4</div>
                                </li>
                                                                <li class="fore5" data-sku="4787565">
                                    <div class="p-img"><a href="//item.jd.com/4787565.html" target="_blank"><img data-img="1" height="85" width="85"  data-lazyload="//img10.360buyimg.com/n5/s85x85_jfs/t7366/351/1158159113/342659/850e3d95/599adf11Nc6ec37b7.jpg"/></a></div>
                                    <div class="p-name"><a href="//item.jd.com/4787565.html" target="_blank" title='小米红米Note5A'>小米红米Note5A</a></div>
                                    <div class="p-price"><strong class="J-p-4787565"></strong></div>
                                    <div class="p-num">5</div>
                                </li>
                                                                <li class="fore6" data-sku="5716981">
                                    <div class="p-img"><a href="//item.jd.com/5716981.html" target="_blank"><img data-img="1" height="85" width="85"  data-lazyload="//img11.360buyimg.com/n5/s85x85_jfs/t12730/306/1517709913/155178/f5e7e927/5a22acfaNf7222715.jpg"/></a></div>
                                    <div class="p-name"><a href="//item.jd.com/5716981.html" target="_blank" title='一加5T'>一加5T</a></div>
                                    <div class="p-price"><strong class="J-p-5716981"></strong></div>
                                    <div class="p-num">6</div>
                                </li>
                                                                <li class="fore7" data-sku="5295423">
                                    <div class="p-img"><a href="//item.jd.com/5295423.html" target="_blank"><img data-img="1" height="85" width="85"  data-lazyload="//img13.360buyimg.com/n5/s85x85_jfs/t10159/363/1183140024/256693/980afae7/59ddcd8cN50a50637.jpg"/></a></div>
                                    <div class="p-name"><a href="//item.jd.com/5295423.html" target="_blank" title='华为荣耀7X'>华为荣耀7X</a></div>
                                    <div class="p-price"><strong class="J-p-5295423"></strong></div>
                                    <div class="p-num">7</div>
                                </li>
                                                            </ul>
                                                    </div>
                    </div>
                </div>
            </div>
        </div>
                                                                <div id="miaozhen7886" class="m m-aside" clstag="shangpin|keycount|product|ad_1"></div>
        <div id="miaozhen10767" class="m m-aside" clstag="shangpin|keycount|product|ad_1"></div>
                                <div id="ad_market_1" class="m m-aside"></div>
            </div>
    <div class="detail">
                        <div class="ETab" id="detail">
            <div class="tab-main large" data-fixed="pro-detail-hd-fixed">
                <ul>
                    <li data-tab="trigger" data-anchor="#detail" class="current" clstag="shangpin|keycount|product|shangpinjieshao_1">商品介绍</li>
                                        <li data-tab="trigger" data-anchor="#detail" clstag="shangpin|keycount|product|pcanshutab">规格与包装</li>
                                                            <li data-tab="trigger" data-anchor="#detail" clstag="shangpin|keycount|product|ershouzhijian" style="display:none">质检报告</li>
                                                            <li data-tab="trigger" data-anchor="#detail" clstag="shangpin|keycount|product|psaleservice">售后保障</li>
                                                            <li data-tab="trigger" data-offset="38" data-anchor="#comment" clstag="shangpin|keycount|product|shangpinpingjia_1">商品评价<s></s></li>
                                                            <li data-tab="trigger" data-offset="38" data-anchor="#club" clstag="shangpin|keycount|product|shequ">
                        手机社区                    </li>
                                                            <li style="display:none" data-tab="trigger" data-offset="38" data-anchor="#try-holder" clstag="shangpin|keycount|product|try-entry">京东试用<sup>new<b>◤</b></sup></li>
                </ul>
                <div class="extra">
                                        <div class="item addcart-mini">
                        <div class="J-addcart-mini EDropdown">
                            <div class="inner">
                                <div class="head" data-drop="head">
                                                                        <a id="InitCartUrl-mini" class="btn-primary" href="//cart.jd.com/gate.action?pid=3888216&pcount=1&ptype=1" clstag="shangpin|keycount|product|gouwuchexuanfu_1">加入购物车</a>
                                                                    </div>
                                <div class="content hide" data-drop="content">
                                    <div class="mini-product-info">
                                        <div class="p-img fl">
                                            <img src="//img11.360buyimg.com/n4/jfs/t3637/275/652996370/280419/2a134044/58105e15N75fb0595.jpg" data-img="1" width="100" height="100" />
                                        </div>
                                        <div class="p-info lh">
                                            <div class="p-name">【新年货】华为 畅享6 金色 移动联通电信4G手机 双卡双待</div>
                                            <div class="p-price">
                                                <strong class="J-p-3888216"></strong> <span>X <span class="J-buy-num"></span></span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                                                        </div>
            </div>
            <div class="tab-con">
                <div data-tab="item">
                    <div class="p-parameter">
                                                <ul class="parameter1 p-parameter-list">
                              <li class='fore0'>
  <i class='i-phone'></i>
  <div class='detail'>
          <p title='1280×720（HD）'>分辨率：1280×720（HD）</p>  </div>
  </li>
  <li class='fore1'>
  <i class='i-camera'></i>
  <div class='detail'>
     <p title='1300万像素'>后置摄像头：1300万像素</p>     <p title='500万像素'>前置摄像头：500万像素</p>  </div>
  </li>
  <li class='fore2'>
  <i class='i-cpu'></i>
  <div class='detail'>
     <p title='八核'>核&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;数：八核</p>     <p title='最高1.5Ghz'>频&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;率：最高1.5Ghz</p>  </div>
  </li>
                         </ul>
                                                                        <ul id="parameter-brand" class="p-parameter-list">
                            <li title='华为（HUAWEI）'>品牌： <a href='//list.jd.com/list.html?cat=9987,653,655&ev=exbrand_8557' clstag='shangpin|keycount|product|pinpai_1' target='_blank'>华为（HUAWEI）</a>
                                <!--a href="#none" class="follow-brand btn-def" clstag='shangpin|keycount|product|guanzhupinpai'><b>&hearts;</b>关注 -->
                            </li>
                        </ul>
                                                <ul class="parameter2 p-parameter-list">
                                <li title='华为畅享6'>商品名称：华为畅享6</li>
    <li title='3888216'>商品编号：3888216</li>
                         <li title='145.00g'>商品毛重：145.00g</li>
            <li title='中国大陆'>商品产地：中国大陆</li>
                                    <li title='安卓（Android）'>系统：安卓（Android）</li>
                  <li title='薄（7mm-8.5mm）'>机身厚度：薄（7mm-8.5mm）</li>
                  <li title='500万-799万'>前置摄像头像素：500万-799万</li>
                  <li title='3GB'>运行内存：3GB</li>
                  <li title='1200万-1999万'>后置摄像头像素：1200万-1999万</li>
                  <li title='4000mAh-5999mAh'>电池容量：4000mAh-5999mAh</li>
                  <li title='16GB'>机身内存：16GB</li>
                  <li title='金色系'>机身颜色：金色系</li>
                                          </ul>
                                                <p class="more-par">
                            <a href="#product-detail" class="J-more-param">更多参数<s class="txt-arr">&gt;&gt;</s></a>
                        </p>
                                            </div>
                    <div id="quality-life" class="quality-life" style="display:none" clstag="shangpin|keycount|product|pinzhishenghuo">
                        <div class="q-logo">
                            <img src="//img20.360buyimg.com/da/jfs/t2077/314/2192172483/11044/f861504a/56ca6792N64e5eafc.png" alt="品质生活"/>
                        </div>
                        <ul class="quality-icon">
                                                                                                                                            <li class="J-ql-iframe ql-ico-1" data-type="1" data-text="质量承诺" style="display:none" data-title="质量承诺" clstag="shangpin|keycount|product|zhijianchengnuo">
                                <a href="#none"><i></i><span>质量承诺</span></a>
                            </li>
                            <li class="ql-ico-5" data-type="5" data-text="耐久性标签" style="display:none" clstag="shangpin|keycount|product|naijiuxingbiaoqian">
                                <a href="#none"><i></i><span>耐久性标签</span></a>
                            </li>
                            <li class="ql-ico-3" data-type="3" data-text="吊牌" style="display:none" clstag="shangpin|keycount|product|diaopai">
                                <a href="#none"><i></i><span>吊牌</span></a>
                            </li>
                            <li class="ql-ico-4" data-type="4" data-text="质检报告" style="display:none" clstag="shangpin|keycount|product|zhijianbaogao">
                                <a href="#none"><i></i><span>质检报告</span></a>
                            </li>
                            <li class="ql-ico-2" data-type="2" data-text="CCC证书" style="display:none" clstag="shangpin|keycount|product|3czhengshu">
                                <a href="#none"><i></i><span>CCC证书</span></a>
                            </li>
                                                        <li class="fresh-ico-1" data-text="实时温控" data-type="v1" style="display:none" clstag="shangpin|keycount|product|shishiwenkong">
                                <a href="#none"><i></i><span class="J-fresh-wd fresh-wd"></span><span>实时温控</span></a>
                            </li>
                            <li class="fresh-ico-2" data-text="检验报告" data-type="v2" style="display:none" clstag="shangpin|keycount|product|jiancebaogao">
                                <a href="#none"><i></i><span>检验报告</span></a>
                            </li>
                        </ul>
                    </div>
                    <div id="suyuan-video"></div>
                                        <div id="J-detail-banner"></div>                                                            <div class="detail-content clearfix" data-name="z-have-detail-nav">
                        <div class="detail-content-wrap">
                                                                                    
                            <div class="detail-content-item">
                                                                                                <div id="activity_header" clstag="shangpin|keycount|product|activityheader"><div style="text-align: center;"><img data-lazyload="//img20.360buyimg.com/cms/jfs/t17059/306/465669821/159770/55c29e4c/5a8024c7Ne72409f1.jpg" width="750" height="352" usemap="#Mapabcdfd1" border="0" alt="" /><map name="Mapabcdfd1" id="Mapabcdfd1">  <area shape="rect" coords="6,3,373,158" href="https://shouji.jd.com/" target="_blank" />  <area shape="rect" coords="381,7,745,157" href="https://sale.jd.com/act/akwtUDFIVxumG48.html" target="_blank" />  <area shape="rect" coords="5,168,184,352" href="https://sale.jd.com/act/k1Apil0bIJQv4uS.html" target="_blank" />  <area shape="rect" coords="190,170,376,349" href="https://sale.jd.com/act/WX2fhkEvletpdM.html" target="_blank" />  <area shape="rect" coords="383,174,558,346" href="https://sale.jd.com/act/dGJ6jb7h3BDpwu.html" target="_blank" />  <area shape="rect" coords="565,166,738,344" href="https://sale.jd.com/act/oMHT5c7gAznJ.html" target="_blank" /></map></div></div>
                                                                                                <div id="J-detail-content">
                                    <div class="loading-style1"><b></b>商品介绍加载中...</div>                                </div><!-- #J-detail-content -->
                                                                                                <div id="activity_footer" clstag="shangpin|keycount|product|activityfooter"></div>
                                                            </div>
                        </div>
                                                <div id="J-detail-nav" class="detail-content-nav">
                            <ul id="J-detail-content-tab" class="detail-content-tab"></ul>
                                                                                </div>
                    </div>
                                                            <div class="clb"></div>
                </div>
                                                <div data-tab="item" class="hide">
                                        <div class="Ptable">
            <div class="Ptable-item">
        <h3>主体</h3>
        <dl>
                                                        <dt>型号</dt>
                  <dd class="Ptable-tips">
                    <a href="#none"><i class="Ptable-sprite-question"></i></a>
                    <div class="tips">
                      <div class="Ptable-sprite-arrow"></div>
                      <div class="content">
                        <p>对外宣传型号</p>
                      </div>
                    </div>
                  </dd>
                  <dd>畅享6</dd>
                                                                                    <dt>入网型号</dt>
                  <dd class="Ptable-tips">
                    <a href="#none"><i class="Ptable-sprite-question"></i></a>
                    <div class="tips">
                      <div class="Ptable-sprite-arrow"></div>
                      <div class="content">
                        <p>工业代号或者入网型号</p>
                      </div>
                    </div>
                  </dd>
                  <dd>以官网信息为准</dd>
                                                                                    <dt>上市年份</dt><dd>2016年</dd>
                                                                                    <dt>上市月份</dt><dd>11月</dd>
                                              </dl>
      </div>
                <div class="Ptable-item">
        <h3>基本信息</h3>
        <dl>
                                                        <dt>机身颜色</dt><dd>金色</dd>
                                                                                    <dt>机身长度（mm）</dt><dd>143.2mm</dd>
                                                                                    <dt>机身宽度（mm）</dt><dd>70.4mm</dd>
                                                                                    <dt>机身厚度（mm）</dt><dd>7.9mm</dd>
                                                                                    <dt>机身重量（g）</dt><dd>约145g（含电池）</dd>
                                                                                    <dt>运营商标志或内容</dt>
                  <dd class="Ptable-tips">
                    <a href="#none"><i class="Ptable-sprite-question"></i></a>
                    <div class="tips">
                      <div class="Ptable-sprite-arrow"></div>
                      <div class="content">
                        <p>定制机往往会有运营商的元素在手机的某些位置，该属性会介绍这些元素出现的位置。</p>
                      </div>
                    </div>
                  </dd>
                  <dd>无</dd>
                                                                                    <dt>机身材质分类</dt><dd>塑胶后盖</dd>
                                              </dl>
      </div>
                <div class="Ptable-item">
        <h3>操作系统</h3>
        <dl>
                                                        <dt>操作系统</dt><dd>Android</dd>
                                              </dl>
      </div>
                <div class="Ptable-item">
        <h3>主芯片</h3>
        <dl>
                                                        <dt>CPU品牌</dt><dd>联发科（MTK）</dd>
                                                                                    <dt>CPU频率</dt><dd>最高1.5Ghz</dd>
                                                                                    <dt>CPU核数</dt><dd>八核</dd>
                                                                                    <dt>CPU型号</dt><dd>mt6750</dd>
                                              </dl>
      </div>
                <div class="Ptable-item">
        <h3>网络支持</h3>
        <dl>
                                                        <dt>双卡机类型</dt><dd>双卡双待单通</dd>
                                                                                    <dt>最大支持SIM卡数量</dt><dd>2个</dd>
                                                                                    <dt>SIM卡类型</dt>
                  <dd class="Ptable-tips">
                    <a href="#none"><i class="Ptable-sprite-question"></i></a>
                    <div class="tips">
                      <div class="Ptable-sprite-arrow"></div>
                      <div class="content">
                        <p>sim卡的规格，大卡、小卡或者nano卡。如果副卡有不同可在下方副卡规格中填写或显示</p>
                      </div>
                    </div>
                  </dd>
                  <dd>其他</dd>
                                                                                    <dt>4G网络</dt>
                  <dd class="Ptable-tips">
                    <a href="#none"><i class="Ptable-sprite-question"></i></a>
                    <div class="tips">
                      <div class="Ptable-sprite-arrow"></div>
                      <div class="content">
                        <p>单卡手机或者主卡的4G网络在这里填写，副卡的网络在副sim卡4G网络中填写。</p>
                      </div>
                    </div>
                  </dd>
                  <dd>4G：移动（TD-LTE)；4G：联通(FDD-LTE)；4G：电信(FDD-LTE)；4G：联通(TD-LTE)</dd>
                                                                                    <dt>3G/2G网络</dt><dd>3G：移动(TD-SCDMA)；3G：联通(WCDMA)；3G：电信(CDMA2000)；2G：移动联通(GSM)+电信(CDMA)</dd>
                                                                                    <dt>副SIM卡3G/2G网络</dt><dd>不支持主副卡同时使用电信卡</dd>
                                                                                    <dt>网络频率（2G/3G）</dt><dd>2G：GSM 900/1800/1900</dd>
                                                                                    <dt>其他</dt><dd>不能同时支持两张电信卡* 各个地区的网络和频段可能有所不同，具体取决于当地运营商以及您所在的位置</dd>
                                              </dl>
      </div>
                <div class="Ptable-item">
        <h3>存储</h3>
        <dl>
                                                        <dt>ROM</dt>
                  <dd class="Ptable-tips">
                    <a href="#none"><i class="Ptable-sprite-question"></i></a>
                    <div class="tips">
                      <div class="Ptable-sprite-arrow"></div>
                      <div class="content">
                        <p>机身的存储空间</p>
                      </div>
                    </div>
                  </dd>
                  <dd>16GB</dd>
                                                                                    <dt>RAM</dt>
                  <dd class="Ptable-tips">
                    <a href="#none"><i class="Ptable-sprite-question"></i></a>
                    <div class="tips">
                      <div class="Ptable-sprite-arrow"></div>
                      <div class="content">
                        <p>机型的运行内存，决定机身的运行速度。</p>
                      </div>
                    </div>
                  </dd>
                  <dd>3GB</dd>
                                                                                    <dt>存储卡</dt><dd>支持MicroSD（TF）</dd>
                                              </dl>
      </div>
                <div class="Ptable-item">
        <h3>屏幕</h3>
        <dl>
                                                        <dt>主屏幕尺寸（英寸）</dt><dd>5.0英寸</dd>
                                                                                    <dt>分辨率</dt><dd>1280×720（HD）</dd>
                                                                                    <dt>屏幕材质类型</dt><dd>AMOLED</dd>
                                              </dl>
      </div>
                <div class="Ptable-item">
        <h3>前置摄像头</h3>
        <dl>
                                                        <dt>前置摄像头</dt><dd>500万像素</dd>
                                                                                    <dt>前摄光圈大小</dt><dd>f/2.2</dd>
                                              </dl>
      </div>
                <div class="Ptable-item">
        <h3>后置摄像头</h3>
        <dl>
                                                        <dt>摄像头数量</dt>
                  <dd class="Ptable-tips">
                    <a href="#none"><i class="Ptable-sprite-question"></i></a>
                    <div class="tips">
                      <div class="Ptable-sprite-arrow"></div>
                      <div class="content">
                        <p>指的是后置摄像头的数量，不是所有摄像头的数量</p>
                      </div>
                    </div>
                  </dd>
                  <dd>1个</dd>
                                                                                    <dt>后置摄像头</dt><dd>1300万像素</dd>
                                              </dl>
      </div>
                <div class="Ptable-item">
        <h3>电池信息</h3>
        <dl>
                                                        <dt>电池容量（mAh）</dt><dd>4100（典型值）</dd>
                                                                                    <dt>电池是否可拆卸</dt>
                  <dd class="Ptable-tips">
                    <a href="#none"><i class="Ptable-sprite-question"></i></a>
                    <div class="tips">
                      <div class="Ptable-sprite-arrow"></div>
                      <div class="content">
                        <p>不可拆卸电池手机更加节省内部空间，密封性更好，请勿在没有专业人士的帮助下自行拆卸。</p>
                      </div>
                    </div>
                  </dd>
                  <dd>否</dd>
                                                                                    <dt>充电器</dt><dd>5V/2A</dd>
                                              </dl>
      </div>
                <div class="Ptable-item">
        <h3>数据接口</h3>
        <dl>
                                                        <dt>数据传输接口</dt><dd>蓝牙；WiFi热点；OTG接口</dd>
                                                                                    <dt>NFC/NFC模式</dt><dd>不支持</dd>
                                                                                    <dt>耳机接口类型</dt><dd>3.5mm</dd>
                                                                                    <dt>充电接口类型</dt><dd>Micro USB</dd>
                                              </dl>
      </div>
                <div class="Ptable-item">
        <h3>手机特性</h3>
        <dl>
                                                        <dt>指纹识别</dt><dd>支持</dd>
                                                                                    <dt>GPS</dt><dd>支持</dd>
                                                                                    <dt>陀螺仪</dt><dd>不支持</dd>
                                              </dl>
      </div>
                <div class="Ptable-item">
        <h3>辅助功能</h3>
        <dl>
                                                        <dt>常用功能</dt><dd>录音</dd>
                                              </dl>
      </div>
      </div>
                                        <div class="package-list">
                        <h3>包装清单</h3>
                        <p>手机（含电池）X1、充电器X1、USB线X1、TPU保护套X1、快速指南X1、售后服务手册X1</p>
                    </div>
                </div>
                                                                <div data-tab="item" class="hide">
                    <!--质检报告-->
                </div>
                                                <div data-tab="item" class="hide">
                    <!--售后保障 家用电器展示一个图文的字段 -->
                </div>
                                                <div data-tab="item" class="hide">
                    <!--商品评价-->
                </div>
                                                <div data-tab="item" class="hide">
                    <!--手机社区 or 达人测评-->
                </div>
                                                <div data-tab="item" class="hide"></div>
            </div>
        </div>

                        <div class="m m-content guarantee" id="guarantee">
                                    <div class="mt">
                       <h3>售后保障</h3>
                    </div>
                                                <div class="mc">
                    <div class="item-detail item-detail-copyright">
                                                <div class="serve-agree-bd">
    <dl>
                                                                <dt>
            <i class="goods"></i>
            <strong>厂家服务</strong>
        </dt>
        <dd>
                                                本产品全国联保，享受三包服务，质保期为：一年质保<br/>
                                                                                                            如因质量问题或故障，凭厂商维修中心或特约维修点的质量检测证明，享受7日内退货，15日内换货，15日以上在质保期内享受免费保修等三包服务！<br />(注:如厂家在商品介绍中有售后保障的说明,则此商品按照厂家说明执行售后保障服务。)
                                                                                    您可以查询本品牌在各地售后服务中心的联系方式，<a target='_blank' href='http://www.huawei.com/cn/'>请点击这儿查询......</a><br/><br/>
            品牌官方网站：<a target='_blank' href='http://www.huawei.com/cn/'>http://www.huawei.com/cn/</a><br/>
                                    售后服务电话：400-830-8300                                </dd>

                <dt>
            <i class="goods"></i>
            <strong>京东承诺</strong>
        </dt>
        <dd>
                            京东平台卖家销售并发货的商品，由平台卖家提供发票和相应的售后服务。请您放心购买！<br />
                                        注：因厂家会在没有任何提前通知的情况下更改产品包装、产地或者一些附件，本司不能确保客户收到的货物与商城图片、产地、附件说明完全一致。只能确保为原厂正货！并且保证与当时市场上同样主流新品一致。若本商城没有及时更新，请大家谅解！
        </dd>

                <dt>
            <i class="goods"></i><strong>
             正品行货             </strong>
        </dt>
                        <dd>京东商城向您保证所售商品均为正品行货，京东自营商品开具机打发票或电子发票。</dd>
                                <dt><i class="unprofor"></i><strong>全国联保</strong></dt>
        <dd>
            凭质保证书及京东商城发票，可享受全国联保服务（奢侈品、钟表除外；奢侈品、钟表由京东联系保修，享受法定三包售后服务），与您亲临商场选购的商品享受相同的质量保证。京东商城还为您提供具有竞争力的商品价格和<a href='//help.jd.com/help/question-892.html' target='_blank'>运费政策</a>，请您放心购买！
            <br/><br/>注：因厂家会在没有任何提前通知的情况下更改产品包装、产地或者一些附件，本司不能确保客户收到的货物与商城图片、产地、附件说明完全一致。只能确保为原厂正货！并且保证与当时市场上同样主流新品一致。若本商城没有及时更新，请大家谅解！
        </dd>
                            </dl>
</div>
                                                <div id="state">
                            <strong>权利声明：</strong><br />京东上的所有商品信息、客户评价、商品咨询、网友讨论等内容，是京东重要的经营资源，未经许可，禁止非法转载使用。
                            <p><b>注：</b>本站商品信息均来自于合作方，其真实性、准确性和合法性由信息拥有者（合作方）负责。本站不提供任何保证，并不承担任何法律责任。</p>
                                                        <br />
                            <strong>价格说明：</strong><br />
                            <p><b>京东价：</b>京东价为商品的销售价，是您最终决定是否购买商品的依据。</p>
                            <p><b>划线价：</b>商品展示的划横线价格为参考价，该价格可能是品牌专柜标价、商品吊牌价或由品牌供应商提供的正品零售价（如厂商指导价、建议零售价等）或该商品在京东平台上曾经展示过的销售价；由于地区、时间的差异性和市场行情波动，品牌专柜标价、商品吊牌价等可能会与您购物时展示的不一致，该价格仅供您参考。</p>
                            <p><b>折扣：</b>如无特殊说明，折扣指销售商在原价、或划线价（如品牌专柜标价、商品吊牌价、厂商指导价、厂商建议零售价）等某一价格基础上计算出的优惠比例或优惠金额；如有疑问，您可在购买前联系销售商进行咨询。</p>
                            <p><b>异常问题：</b>商品促销信息以商品详情页“促销”栏中的信息为准；商品的具体售价以订单结算页价格为准；如您发现活动商品售价或促销信息有异常，建议购买前先联系销售商咨询。</p>

                                            </div>
                </div>
            </div>

<div style='display:none' >
        <a href='https://www.jd.com/phb/zhishi/de076d35c8ba1f69.html'>6种温和去角质法  重获青春的肌肤滑嫩</a>
        <a href='https://www.jd.com/phb/zhishi/340a4bdcbde17158.html'>手机的网络数据</a>
        <a href='https://www.jd.com/phb/zhishi/5780903dbc09194e.html'>iPhone6访问限制如何开启</a>
        <a href='https://www.jd.com/phb/zhishi/f0054ab551ff45d7.html'>2个小技巧教你如何拍出可爱的猫咪</a>
        <a href='https://www.jd.com/phb/zhishi/9009095a8e889762.html'>联通合约计划售后指南</a>
        <a href='https://www.jd.com/phb/zhishi/091aaa39d13c3448.html'>苹果暗示iPhone 6将于9月下旬发布</a>
        <a href='https://www.jd.com/phb/zhishi/419b5d94ff78bfc0.html'>iPhone5S触控屏面板曝光</a>
        <a href='https://www.jd.com/phb/zhishi/b689d904a0479403.html'>miui系统中的一些实用小技巧</a>
        <a href='https://www.jd.com/phb/zhishi/9d26c13a62c01080.html'>朵唯应用——伊乐园</a>
        <a href='https://www.jd.com/phb/zhishi/bf4581857553021f.html'>上班族的七条饮食小妙招</a>
    </div>
<!-- 主站品牌页 , 口碑、排行榜 SEO开始 -->
<div id='CBP_CRK' style='display:none'>
        <!-- 主站品牌页 开始 -->
            <a href='https://www.jd.com/pinpai/16407.html'>松下（Panasonic）</a>
        <a href='https://www.jd.com/pinpai/9420.html'>金立（Gionee）</a>
        <a href='https://www.jd.com/pinpai/107636.html'>新品牌测试（newpinpai）</a>
        <a href='https://www.jd.com/pinpai/16506.html'>索爱（soaiy）</a>
        <a href='https://www.jd.com/pinpai/209978.html'>海派贵族（Haipai Noble）</a>
        <a href='https://www.jd.com/pinpai/16975.html'>天语（K-Touch）</a>
        <a href='https://www.jd.com/pinpai/212863.html'>东北丰（DBEIF）</a>
        <a href='https://www.jd.com/pinpai/278268.html'>YISON</a>
        <a href='https://www.jd.com/pinpai/25591.html'>vivo</a>
        <a href='https://www.jd.com/pinpai/255352.html'>htc</a>
        <a href='https://www.jd.com/pinpai/655-18095.html'>夏新（Amoi）</a>
        <a href='https://www.jd.com/pinpai/655-32919.html'>彼丽（BEELY）</a>
        <a href='https://www.jd.com/pinpai/655-246053.html'>锐族</a>
        <a href='https://www.jd.com/pinpai/655-247963.html'>易博士</a>
        <a href='https://www.jd.com/pinpai/655-223316.html'>unruly</a>
        <a href='https://www.jd.com/pinpai/655-45757.html'>欧奇（ouki）</a>
        <a href='https://www.jd.com/pinpai/655-13477.html'>纽曼（Newsmy）</a>
        <a href='https://www.jd.com/pinpai/655-179528.html'>VETAS</a>
        <a href='https://www.jd.com/pinpai/655-103488.html'>陕西电信</a>
        <a href='https://www.jd.com/pinpai/655-16407.html'>松下（Panasonic）</a>
            <!-- 主站品牌页 结束 -->
    
        <!-- 排行榜 开始 -->
            <a href='//club.jd.com/rank/655/e69c8de58aa1e68081e5baa6e5a5bd_2.html'>服务态度好</a>
        <a href='//club.jd.com/rank/655/e59381e8b4a8e580bce5be97e4bfa1e8b596_2.html'>品质值得信赖</a>
        <a href='//club.jd.com/rank/655/e789a9e6b581e9809fe5baa6e5bfab_2.html'>物流速度快</a>
        <a href='//club.jd.com/rank/655/e6ada3e59381e4bf9de99a9c_2.html'>正品保障</a>
        <a href='//club.jd.com/rank/655/e789a9e7be8ee4bbb7e5bb89_2.html'>物美价廉</a>
        <a href='//club.jd.com/rank/655/e680a7e4bbb7e6af94e8be83e9ab98_2.html'>性价比较高</a>
        <a href='//club.jd.com/rank/655.html'>好评度</a>
            <!-- 排行榜 结束 -->
    
        <!-- 口碑 开始 -->
            <a href='//club.jd.com/koubei/e7baa2e7b1b36e6f7465e6898be69cba.html'>红米note手机</a>
        <a href='//club.jd.com/koubei/e58886e5b18fe6898be69cba.html'>分屏手机</a>
        <a href='//club.jd.com/koubei/e4b889e998b2e6898be69cba.html'>三防手机</a>
        <a href='//club.jd.com/koubei/e7baa2e7b1b33373e6898be69cba.html'>红米3s手机</a>
        <a href='//club.jd.com/koubei/e4b8ade59bbde7a7bbe58aa8e6898be69cba.html'>中国移动手机</a>
        <a href='//club.jd.com/koubei/e8b685e89684e6898be69cba.html'>超薄手机</a>
        <a href='//club.jd.com/koubei/38383438e6898be69cba.html'>8848手机</a>
        <a href='//club.jd.com/koubei/e4b889e6989f6139e6898be69cba.html'>三星a9手机</a>
        <a href='//club.jd.com/koubei/e68b8de785a7e6898be69cba.html'>拍照手机</a>
        <a href='//club.jd.com/koubei/e58f8ce69184e5838fe5a4b4e6898be69cba.html'>双摄像头手机</a>
            <!-- 口碑 结束 -->
    </div>
<!-- 主站品牌页 , 口碑、排行榜 SEO结束 -->

<div id="footmark" class="w footmark"></div>
<div id="GLOBAL_FOOTER"></div>
<script>
        seajs.use('MOD_ROOT/main/main.js', function (App) {
        App.init(pageConfig.product);
    });


                function totouchbate() {
  var exp = new Date();
  exp.setTime(exp.getTime() + 30 * 24 * 60 * 60 * 1000);
  document.cookie = "pcm=2;expires=" + exp.toGMTString() + ";path=/;domain=jd.com";
    window.location.href="//item.m.jd.com/product/3888216.html";
}
if(window.showtouchurl) {
  $("#GLOBAL_FOOTER").after("<div class='ac' style='padding-bottom:30px;'>你的浏览器更适合浏览触屏版&nbsp;&nbsp;&nbsp;&nbsp;<a href='#none' style='text-decoration:underline;' onclick='totouchbate()'>京东触屏版</a></div>");
} else {
  $("#GLOBAL_FOOTER").css("padding-bottom", "30px");
}
</script>
<script type="text/javascript">
    $(".Ptable-tips").mouseover(function(){
        $(this).find(".tips").show();
    });
    $(".Ptable-tips").mouseout(function(){
        $(this).find(".tips").hide();
    });
</script>


<img src="//jcm.jd.com/pre" width="0" height="0" style="display:none"/>
<script>
seajs.use('//wl.jd.com/wl.js');
(function(){
    var bp = document.createElement('script');
    var curProtocol = window.location.protocol.split(':')[0];
    if (curProtocol === 'https') {
        bp.src = 'https://zz.bdstatic.com/linksubmit/push.js';
    }
    else {
        bp.src = 'http://push.zhanzhang.baidu.com/push.js';
    }
    var s = document.getElementsByTagName("script")[0];
    s.parentNode.insertBefore(bp, s);
})();

dataLayer = [{
    'google_tag_params': {
        ecomm_prodid:pageConfig.product.skuid,
        ecomm_pagetype:"item",
        ecomm_pname:pageConfig.product.name,
        ecomm_pcat:['9987|653|655'],
        ecomm_pvalues:['9987|653|655'],
        ecomm_totalvalue:null,
        ecomm_pbrand:8557    }
}]
</script>
<noscript>iframe(src='//www.googletagmanager.com/ns.html?id=GTM-T947SH', height='0', width='0', style='display: none; visibility: hidden;')</noscript>
<script>
(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start': new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src= '//www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);})(window,document,'script','dataLayer','GTM-T947SH');
</script><div id="J-global-toolbar"></div>
<script>
/*
(function(cfg) {
    cfg.toolbarParam = {
        bars: {
            history: {
                enabled: false
            }
        }
    }
})(pageConfig);
    ;(function(cfg) {
        var sid = cfg.cat[2] === 832 ? '737542' : '992349';
        var phoneNetwork = cfg.phoneNetwork
            ? cfg.phoneNetwork.join(',')
            : '';

        var hallEnable = cfg.cat[2] === 655;
        var hallUrl = {
            url: '//ctc.jd.com/hall/index?',
            param: {
                sku: cfg.skuid,
                cat: cfg.cat.join(','),
                mode: phoneNetwork
            }
        };

        var ad_entry = { enabled: false };
        var isDecCat = cfg.cat[0] == 1620 || cfg.cat[0] == 9847 
                        || cfg.cat[0] == 9855 || cfg.cat[0] == 6196
                        
        if (isDecCat) {
            ad_entry = {
                enabled: true,
                id: "0_0_7209",
                startTime: +new Date(2017, 3, 1, 0, 0, 1) / 1000,
                endTime: +new Date(2017, 4, 3, 0, 0, 0) / 1000
            }
        }

        var isEleCat = cfg.cat[0] === 737
        if (isEleCat) {
            ad_entry = {
                enabled: true,
                id: "0_0_7860",
                startTime: +new Date(2017, 3, 11, 0, 0, 1) / 1000,
                endTime: +new Date(2017, 4, 8, 0, 0, 0) / 1000
            }
        }

        seajs.use(['//static.360buyimg.com/devfe/toolbar/1.0.0/js/main'], function(toolbar) {
            pageConfig.toolbar = new toolbar({
                pType: 'item',
                bars: {
                    hall: {
                        index: 0.5,
                        title: '营业厅',
                        login: true,
                        enabled: hallEnable,
                        iframe: hallUrl.url + $.param(hallUrl.param)
                    },
                    cart: {
                        enabled: true
                    },
                    coupon: {
                        index: 1.5,
                        enabled: true,
                        title: '优惠券',
                        login: true,
                        iframe: '//cd.jd.com/coupons?' + $.param({
                            skuId: cfg.skuid,
                            cat: cfg.cat.join(','),
                            venderId: cfg.venderId
                        })
                    },
                    jimi: {
                        iframe: '//jimi.jd.com/index.action?productId='+ cfg.skuid +'&source=jdhome'
                    }
                },
                links: {
                    feedback: {
                        href: '//surveys.jd.com/index.php?r=survey/index/sid/323814/newtest/Y/lang/zh-Hans'
                    },
                    top:{ anchor:"#" }
                },
                ad: ad_entry
            });
        });
    })(pageConfig.product)
*/
</script>        

</body>
</html>
'''

soup = BeautifulSoup(htmlstr,"lxml")
divtitle = soup.find_all(name='div',attrs={"class":"item ellipsis"})
print(divtitle[0].text)
#tree = etree.parse(UrlStr)
#r = tree.XPath("/html/body/div[11]/div[2]/div[1]/div[2]/div[1]/div[1]/ul[3]/li[1]")
#print(len(r))