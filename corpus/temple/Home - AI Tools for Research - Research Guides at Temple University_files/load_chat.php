(function() { var options = {"id":16781,"hash":"e2f5d90134f990a82aaef204913ac871","siteUrl":"https:\/\/answers.library.temple.edu","width":"100%","height":"350px","color_backg":"#FFFFFF","color_border":"#CCCCCC"}; var cascadeServer = "https:\/\/chat-us.libanswers.com"; var referer = ""; var refererTitle = ""; const embedWidget={config:{},online:!1,loaded:!1,chatContainer:null,referer:"",refererTitle:"",insertWidgetCSS:function(){const id=`#${this.chatContainer.id}`,css=`/* LibChat Widget CSS */\n        ${id} .lci_chat_load { width: ${this.config.width}; height: ${this.config.height}; background-color: ${this.config.color_backg}; border: 1px solid ${this.config.color_border}; box-sizing: content-box; }\n        ${id} iframe { width: 100%; height: ${this.config.height}; background-color: ${this.config.color_backg}; border: 0px; box-sizing: border-box; }`,head=document.head||document.getElementsByTagName("head")[0],style=document.createElement("style");style.styleSheet?style.styleSheet.cssText=css:style.appendChild(document.createTextNode(css)),head.appendChild(style)},buildIFrame:function(){""===this.referer&&(this.referer=window.location.href),""===this.refererTitle&&window.document.title&&(this.refererTitle=window.document.title);let authId=0;window.springSpace&&window.springSpace.la&&window.springSpace.la.Page&&window.springSpace.la.Page.auth_id&&(authId=window.springSpace.la.Page.auth_id);const widgetUrl=`${this.config.siteUrl}/chat/widget/${this.config.hash}?referer=${encodeURIComponent(this.referer)}&referer_title=${encodeURIComponent(this.refererTitle)}&auth_id=${authId}`,iframeContainer=document.createElement("div");iframeContainer.classList.add("lci_chat_load");const iframe=document.createElement("iframe");iframe.setAttribute("id",`iframe_${this.config.hash}`),iframe.setAttribute("name",`iframe_${this.config.hash}`),iframe.setAttribute("src",widgetUrl),iframe.setAttribute("title","Chat Widget"),iframe.setAttribute("scrolling","no"),iframe.innerHTML="Content is loading...",iframeContainer.appendChild(iframe),this.chatContainer.appendChild(iframeContainer),this.chatContainer.setAttribute("role","region"),this.chatContainer.setAttribute("aria-label","Chat Widget")},start:function(){!0!==this.loaded&&(this.loaded=!0,this.chatContainer=document.querySelector(`#libchat_${this.config.hash}, #libchat_inline_widget, #libchat_d2oi_widget`),null===this.chatContainer||this.chatContainer.querySelector(`#iframe_${this.config.hash}`)||(this.insertWidgetCSS(),this.buildIFrame()))}};embedWidget.config=options,embedWidget.referer=referer,embedWidget.refererTitle=refererTitle,"complete"===document.readyState||"interactive"===document.readyState?embedWidget.start():(document.addEventListener("DOMContentLoaded",embedWidget.start.bind(embedWidget),!1),window.addEventListener("load",embedWidget.start.bind(embedWidget),!1));})();