const CACHE_NAME = 'agamoon-v9';
const OFFLINE_URL = 'https://agashae.space/';

self.addEventListener('install', event => {
    event.waitUntil(
        caches.open(CACHE_NAME).then(cache => {
            return cache.addAll([
                OFFLINE_URL,
                'https://agashae.space/style.css',
                'https://agashae.space/manifest.json',
                'https://agashae.space/img/LogoWebSite.png'
            ]);
        })
    );
    self.skipWaiting();
});

self.addEventListener('activate', event => {
    event.waitUntil(
        caches.keys().then(keys => {
            return Promise.all(
                keys.filter(key => key !== CACHE_NAME)
                    .map(key => caches.delete(key))
            );
        })
    );
    self.clients.claim();
});

self.addEventListener('fetch', event => {
    event.respondWith(
        caches.match(event.request)
            .then(response => response || fetch(event.request))
            .catch(() => {
                return caches.match(OFFLINE_URL);
            })
    );
});