// DuarteCinema Pro - High Performance PWA Service Worker
const CACHE_NAME = 'duartecinema-v1.0.0';
const STATIC_ASSETS = [
  './cinema.html',
  './manifest.json',
  './assets/icon_cinema.png',
  './assets/brand_avatar.jpg'
];

// Install: Cache core application shell
self.addEventListener('install', (event) => {
  self.skipWaiting();
  event.waitUntil(
    caches.open(CACHE_NAME).then((cache) => {
      return cache.addAll(STATIC_ASSETS).catch((err) => {
        console.warn('[DuarteCinema SW] Pre-cache warning:', err);
      });
    })
  );
});

// Activate: Clean up old caches and take control immediately
self.addEventListener('activate', (event) => {
  event.waitUntil(
    caches.keys().then((keys) => {
      return Promise.all(
        keys.map((key) => {
          if (key !== CACHE_NAME) {
            console.log('[DuarteCinema SW] Removing outdated cache:', key);
            return caches.delete(key);
          }
        })
      );
    }).then(() => self.clients.claim())
  );
});

// Fetch: Network First strategy with Cache Fallback for shell
self.addEventListener('fetch', (event) => {
  const req = event.request;

  // Only handle GET requests
  if (req.method !== 'GET') return;

  const url = new URL(req.url);

  // Bypass third-party streaming embeds and TMDB API from SW interception
  if (
    url.hostname.includes('themoviedb.org') ||
    url.hostname.includes('videasy.net') ||
    url.hostname.includes('vidsrc') ||
    url.hostname.includes('playlatin') ||
    url.hostname.includes('smashystream') ||
    url.hostname.includes('zeno.fm')
  ) {
    return;
  }

  // Network First for HTML, Fallback to Cache
  if (req.headers.get('accept') && req.headers.get('accept').includes('text/html')) {
    event.respondWith(
      fetch(req)
        .then((response) => {
          if (response && response.status === 200) {
            const copy = response.clone();
            caches.open(CACHE_NAME).then((cache) => cache.put(req, copy));
          }
          return response;
        })
        .catch(() => caches.match(req).then((cached) => cached || caches.match('./cinema.html')))
    );
    return;
  }

  // Cache First for static images & assets
  event.respondWith(
    caches.match(req).then((cached) => {
      if (cached) return cached;
      return fetch(req).then((networkRes) => {
        if (networkRes && networkRes.status === 200 && (url.pathname.includes('/assets/') || url.pathname.endsWith('.png') || url.pathname.endsWith('.jpg'))) {
          const clone = networkRes.clone();
          caches.open(CACHE_NAME).then((cache) => cache.put(req, clone));
        }
        return networkRes;
      });
    })
  );
});
