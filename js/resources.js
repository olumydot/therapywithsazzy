(function () {
  var root = document.getElementById('rc-center');
  if (!root || !window.CATALOG) return;
  var AUD = [['all', 'Everyone', '#0F2A4A'], ['children', 'Children', '#E8806A'], ['teens', 'Teens', '#2E9C95'], ['adults', 'Adults', '#4F6FB5'], ['parents', 'Parents', '#E0A93B'], ['trauma', 'Trauma & Healing', '#7B6AAE']];
  var TOP = [['all', 'All topics'], ['emotional-regulation', 'Emotional regulation'], ['anxiety', 'Anxiety & worries'], ['confidence', 'Confidence & self-esteem'], ['anger', 'Anger management'], ['stress', 'Stress & burnout'], ['relationships', 'Relationships & boundaries'], ['parenting', 'Parenting strategies'], ['trauma', 'Trauma & healing']];
  var COLORS = { children: ['#E8806A', '#fde9e3'], parents: ['#E0A93B', '#fbf0d4'], teens: ['#2E9C95', '#dff1ee'], adults: ['#4F6FB5', '#e4eaf6'], trauma: ['#7B6AAE', '#ebe7f5'] };
  var NAME = { children: 'children', parents: 'parents', teens: 'teens', adults: 'adults', trauma: 'trauma and healing' };
  var st = { aud: 'all', topic: 'all', q: '', start: false };

  var tabs = document.getElementById('rc-tabs'), chips = document.getElementById('rc-chips'),
    grid = document.getElementById('rc-grid'), title = document.getElementById('rc-title'), count = document.getElementById('rc-count'),
    q = document.getElementById('rc-q'), start = document.getElementById('rc-start');

  function esc(s) { return String(s).replace(/[&<>"]/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]; }); }

  function buttons(list, key, cur, cls) {
    return list.map(function (x) {
      var dot = x[2] ? '<span class="dot" style="--c:' + x[2] + '"></span>' : '';
      return '<button type="button" class="' + cls + '" data-v="' + x[0] + '" aria-pressed="' + (cur === x[0]) + '">' + dot + esc(x[1]) + '</button>';
    }).join('');
  }

  function card(e) {
    var c = COLORS[e.a] || ['#2E9C95', '#dff1ee'];
    return '<article class="rc-card" style="--a:' + c[0] + ';--s:' + c[1] + '">' +
      '<a class="rc-thumb" href="/resources/' + e.s + '.pdf" target="_blank" rel="noopener" aria-label="Preview ' + esc(e.t) + '">' + (e.st ? '<span class="star">★ Start here</span>' : '') +
      '<img loading="lazy" src="/resources/thumbs/' + e.s + '.jpg" alt="Preview of ' + esc(e.t) + '"></a>' +
      '<div class="rc-body"><div class="rc-tags"><span>' + esc(e.k) + '</span><span>' + esc(e.g) + '</span></div>' +
      '<h3>' + esc(e.t) + '</h3><p>' + esc(e.d) + '</p>' +
      '<div class="rc-actions"><a class="btn btn-primary" href="/resources/' + e.s + '.pdf" download>Download</a><a class="btn btn-ghost" href="/resources/' + e.s + '.pdf" target="_blank" rel="noopener">Preview</a></div></div></article>';
  }

  function render() {
    tabs.innerHTML = buttons(AUD, 'aud', st.aud, 'tab');
    chips.innerHTML = buttons(TOP, 'topic', st.topic, 'chip-btn');
    var needle = st.q.trim().toLowerCase();
    var list = window.CATALOG.filter(function (e) {
      if (st.aud !== 'all' && e.a !== st.aud) return false;
      if (st.topic !== 'all' && e.tp.indexOf(st.topic) < 0) return false;
      if (st.start && !e.st) return false;
      if (needle && (e.t + ' ' + e.d + ' ' + e.k).toLowerCase().indexOf(needle) < 0) return false;
      return true;
    });
    var topicName = (TOP.filter(function (t) { return t[0] === st.topic; })[0] || [])[1];
    title.textContent = 'Your resource collection';
    count.textContent = (st.aud === 'all' ? 'Recommended materials for everyone' : 'Recommended materials for ' + NAME[st.aud]) +
      (st.topic !== 'all' ? ', focusing on ' + topicName.toLowerCase() : '') + (st.start ? ' (foundation set)' : '') + ': ' + list.length + (list.length === 1 ? ' resource' : ' resources');
    grid.innerHTML = list.length ? list.map(card).join('') : '<p class="rc-empty">No matches yet. Try a different topic or clear the search.</p>';
  }

  tabs.addEventListener('click', function (e) { var b = e.target.closest('button'); if (b) { st.aud = b.dataset.v; render(); } });
  chips.addEventListener('click', function (e) { var b = e.target.closest('button'); if (b) { st.topic = b.dataset.v; render(); } });
  q.addEventListener('input', function () { st.q = q.value; render(); });
  start.addEventListener('change', function () { st.start = start.checked; render(); });
  document.querySelectorAll('[data-pick-start]').forEach(function (a) { a.addEventListener('click', function () { st.start = true; start.checked = true; st.aud = 'all'; st.topic = 'all'; render(); }); });
  render();
})();
