(function () {
  var header = document.querySelector('.site-header');
  var btn = document.querySelector('.menu-btn');
  var links = document.getElementById('nav-links');

  function onScroll() { header.classList.toggle('scrolled', window.scrollY > 8); }
  onScroll();
  window.addEventListener('scroll', onScroll, { passive: true });

  function setMenu(open) {
    btn.setAttribute('aria-expanded', String(open));
    btn.setAttribute('aria-label', open ? 'Close menu' : 'Open menu');
    links.classList.toggle('open', open);
  }
  btn.addEventListener('click', function () { setMenu(btn.getAttribute('aria-expanded') !== 'true'); });
  links.addEventListener('click', function (e) { if (e.target.closest('a')) setMenu(false); });
  document.addEventListener('keydown', function (e) { if (e.key === 'Escape') setMenu(false); });

  // Scroll reveal
  var items = document.querySelectorAll('.reveal');
  if ('IntersectionObserver' in window) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (en.isIntersecting) { en.target.classList.add('in'); io.unobserve(en.target); }
      });
    }, { threshold: 0.12, rootMargin: '0px 0px -40px 0px' });
    items.forEach(function (el) { io.observe(el); });
  } else {
    items.forEach(function (el) { el.classList.add('in'); });
  }

  // "What's your feeling today?" (children page)
  var feelings = {
    worried: {
      title: 'Feeling worried',
      intro: 'Worry is your brain trying to keep you safe. Here are some ways to help it settle:',
      tips: ['Take 5 slow "smell the flower, blow out the candle" breaths.', 'Name 3 things you can see and 2 things you can hear.', 'Tell a trusted grown-up what your worry is saying.']
    },
    frustrated: {
      title: 'Feeling frustrated',
      intro: 'Frustration shows up when something feels hard or unfair. You can give it space without letting it drive:',
      tips: ['Squeeze your hands into tight fists for 5 seconds, then let go.', 'Take a short break and come back when your body feels calmer.', 'Ask: "What do I need right now?" Help, a break, or a hug?']
    },
    excited: {
      title: 'Feeling excited',
      intro: 'Excitement is a lot of energy! It can help to give it somewhere to go:',
      tips: ['Do 10 jumping jacks or a silly dance.', 'Tell someone what you are excited about.', 'Take 3 slow breaths so your body can enjoy it.']
    },
    sad: {
      title: 'Feeling sad',
      intro: 'Sad feelings are okay. They need to be noticed and cared for:',
      tips: ['Give yourself a hug, or ask for one.', 'Draw or write about how you feel.', 'Do one small thing that helps you feel a little cozier.']
    },
    calm: {
      title: 'Feeling calm',
      intro: 'Nice! Calm is a skill you can practice and keep for later:',
      tips: ['Notice where you feel calm in your body.', 'Remember what helped you get here.', 'Share your calm: tell someone what works for you.']
    }
  };
  var out = document.getElementById('feel-out');
  var btns = document.querySelectorAll('.feel');
  btns.forEach(function (b) {
    b.addEventListener('click', function () {
      var f = feelings[b.dataset.feel];
      btns.forEach(function (x) { x.setAttribute('aria-pressed', String(x === b)); });
      out.innerHTML = '<h3>' + f.title + '</h3><p>' + f.intro + '</p><ul>' +
        f.tips.map(function (t) { return '<li>' + t + '</li>'; }).join('') + '</ul>';
    });
  });

  // Inquiry form: opens the visitor's email app with a pre-filled message.
  // TODO (launch): replace with a secure/HIPAA-appropriate form service if one is adopted.
  var form = document.getElementById('inquiry');
  if (form) {
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var d = new FormData(form);
      var body = 'Name: ' + d.get('name') +
        '\nEmail: ' + d.get('email') +
        '\nPhone: ' + (d.get('phone') || '—') +
        '\nLooking for: ' + d.get('who') +
        '\nPreferred contact: ' + d.get('method') +
        '\n\nMessage:\n' + (d.get('message') || '—');
      var url = 'mailto:therapywithsazzy@gmail.com?subject=' +
        encodeURIComponent('Website inquiry — ' + d.get('who')) + '&body=' + encodeURIComponent(body);
      window.location.href = url;
      document.getElementById('form-status').textContent =
        'Your email app should now open with your message ready to send. If it does not, email therapywithsazzy@gmail.com directly.';
    });
  }
})();
