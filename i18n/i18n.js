/**
 * i18n.js — Bilingual translation engine (LV/EN)
 * Loads translations from JSON files and applies them to data-i18n elements.
 * Supports: data-i18n, data-i18n-attr, data-i18n-html attributes
 * Language preference stored in localStorage, also supports ?lang=en URL param
 */
(function(){
  'use strict';

  var DEFAULT_LANG = 'lv';
  var SUPPORTED = ['lv','en'];
  var STORAGE_KEY = 'cncfrezes_lang';
  var BASE_PATH = '/i18n/';

  // Detect initial language
  function detectLang(){
    // URL param takes priority
    var p = new URLSearchParams(window.location.search).get('lang');
    if(p && SUPPORTED.indexOf(p) !== -1) return p;
    // localStorage
    try {
      var s = localStorage.getItem(STORAGE_KEY);
      if(s && SUPPORTED.indexOf(s) !== -1) return s;
    } catch(e){}
    // browser preference
    var nav = (navigator.language || navigator.userLanguage || '').split('-')[0];
    if(nav === 'lv') return 'lv';
    return DEFAULT_LANG;
  }

  var currentLang = detectLang();
  var translations = {}; // { lv: {...}, en: {...} }
  var loadedLangs = {};
  var onReadyCallbacks = [];

  // Load a language JSON file
  function loadLang(lang, callback){
    if(loadedLangs[lang]){ callback(); return; }
    var xhr = new XMLHttpRequest();
    xhr.open('GET', BASE_PATH + lang + '.json', true);
    xhr.onload = function(){
      if(xhr.status >= 200 && xhr.status < 400){
        try {
          translations[lang] = JSON.parse(xhr.responseText);
          loadedLangs[lang] = true;
          callback();
        } catch(e){ console.error('i18n: JSON parse error for ' + lang, e); }
      }
    };
    xhr.onerror = function(){ console.error('i18n: Failed to load ' + lang); };
    xhr.send();
  }

  // Get a translation key's value (supports dot notation like "home.hero_badge")
  function t(key, lang){
    lang = lang || currentLang;
    var parts = key.split('.');
    var obj = translations[lang];
    if(!obj) return key;
    for(var i=0; i<parts.length; i++){
      if(obj[parts[i]] === undefined) return key;
      obj = obj[parts[i]];
    }
    return obj;
  }

  // Apply translations to DOM
  function applyTranslations(lang){
    currentLang = lang;
    document.documentElement.lang = lang;

    // Update data-i18n elements (text content)
    var els = document.querySelectorAll('[data-i18n]');
    for(var i=0; i<els.length; i++){
      var el = els[i];
      var key = el.getAttribute('data-i18n');
      var val = t(key, lang);
      if(typeof val === 'string') el.textContent = val;
    }

    // Update data-i18n-html elements (inner HTML)
    var htmlEls = document.querySelectorAll('[data-i18n-html]');
    for(var j=0; j<htmlEls.length; j++){
      var hel = htmlEls[j];
      var hkey = hel.getAttribute('data-i18n-html');
      var hval = t(hkey, lang);
      if(typeof hval === 'string') hel.innerHTML = hval;
    }

    // Update data-i18n-attr elements (attributes like placeholder, title, aria-label)
    var attrEls = document.querySelectorAll('[data-i18n-attr]');
    for(var k=0; k<attrEls.length; k++){
      var ael = attrEls[k];
      var spec = ael.getAttribute('data-i18n-attr');
      var parts2 = spec.split(',');
      for(var m=0; m<parts2.length; m++){
        var kv = parts2[m].split(':');
        var attrName = kv[0].trim();
        var attrKey = kv[1].trim();
        var aval = t(attrKey, lang);
        if(typeof aval === 'string') ael.setAttribute(attrName, aval);
      }
    }

    // Update <title> and <meta name="description">
    var titleKey = document.documentElement.getAttribute('data-i18n-title');
    if(titleKey){
      var tv = t(titleKey, lang);
      if(typeof tv === 'string') document.title = tv;
    }
    var descKey = document.documentElement.getAttribute('data-i18n-desc');
    if(descKey){
      var dv = t(descKey, lang);
      if(typeof dv === 'string'){
        var metaDesc = document.querySelector('meta[name="description"]');
        if(metaDesc) metaDesc.setAttribute('content', dv);
      }
    }

    // Update year in copyright
    var yearEl = document.getElementById('year');
    if(yearEl) yearEl.textContent = new Date().getFullYear();

    // Update language switcher active state
    var switchers = document.querySelectorAll('.lang-switcher a');
    for(var n=0; n<switchers.length; n++){
      var s = switchers[n];
      var sl = s.getAttribute('data-lang');
      if(sl === lang){
        s.classList.add('active');
        s.setAttribute('aria-current','true');
      } else {
        s.classList.remove('active');
        s.removeAttribute('aria-current');
      }
    }

    // Save preference
    try { localStorage.setItem(STORAGE_KEY, lang); } catch(e){}
    // Update hreflang
    updateHreflang(lang);
  }

  // Update hreflang links in <head>
  function updateHreflang(lang){
    var existing = document.querySelector('link[hreflang="' + lang + '"]');
    var currentUrl = window.location.href.split('?')[0];
    // Remove old lang param, add new
    var sep = currentUrl.indexOf('?') === -1 ? '?' : '&';
    // Keep it clean — just set canonical appropriately
    var canonical = document.querySelector('link[rel="canonical"]');
    if(canonical){
      var href = canonical.getAttribute('href');
      // Remove existing lang param
      href = href.replace(/[?&]lang=(lv|en)/,'');
      if(lang !== DEFAULT_LANG){
        href += (href.indexOf('?')===-1?'?':'&') + 'lang=' + lang;
      }
      canonical.setAttribute('href', href);
    }
  }

  // Set language
  function setLang(lang){
    if(SUPPORTED.indexOf(lang) === -1) return;
    if(lang === currentLang && loadedLangs[lang]) return;

    function apply(){
      applyTranslations(lang);
      // Fire callbacks
      for(var i=0; i<onReadyCallbacks.length; i++) onReadyCallbacks[i](lang);
    }

    if(loadedLangs[lang]){
      apply();
    } else {
      loadLang(lang, apply);
    }
  }

  // Build language switcher
  function buildSwitcher(){
    var containers = document.querySelectorAll('.lang-switcher');
    for(var i=0; i<containers.length; i++){
      var c = containers[i];
      c.setAttribute('role','group');
      c.setAttribute('aria-label','Language selector');
      var links = c.querySelectorAll('a');
      for(var j=0; j<links.length; j++){
        var link = links[j];
        link.setAttribute('role','button');
        link.setAttribute('href','#');
        link.addEventListener('click', function(e){
          e.preventDefault();
          setLang(this.getAttribute('data-lang'));
        });
      }
    }
  }

  // Initialize
  function init(){
    buildSwitcher();
    // Load default language first, then apply
    loadLang(DEFAULT_LANG, function(){
      applyTranslations(DEFAULT_LANG);
      if(currentLang !== DEFAULT_LANG){
        setLang(currentLang);
      }
    });
  }

  // Expose API
  window.i18n = {
    t: t,
    setLang: setLang,
    getLang: function(){ return currentLang; },
    onReady: function(cb){ onReadyCallbacks.push(cb); }
  };

  // Run on DOM ready
  if(document.readyState === 'loading'){
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
