const CACHE_NAME = 'agamoon-v1';

// Fichiers à mettre en cache pour le mode hors-ligne
const FILES_TO_CACHE = [
    '/code/accueil.html',
    '/code/accueil.css',
    '/LogoWebSite.png',
    '/img/photo-1657637760839-772d81f3e334.jpg',
    '/img/moon-29.gif',
    '/img/Luna2.jpg',
    '/img/Luna9.jpg',
    '/img/Apollo11.jpg',
    '/img/Apollo17.jpg',
    '/img/artemis-3.jpg',
    '/img/Chandrayaan-3.jpg',
    "/img/Chang'e 4.jpg",
    '/img/8Phases/lune-libration-phases.gif',
    '/img/8Phases/phase-nouvelle-lune.jpg',
    '/img/8Phases/premier-croissant.jpg',
    '/img/8Phases/phase-premier-quartier.jpg',
    '/img/8Phases/phase-gibbeuse-croissante.jpg',
    '/img/8Phases/phase-pleine-lune.jpg',
    '/img/8Phases/phase-gibbeuse-decroissante.jpg',
    '/img/8Phases/phase-dernier-quartier.jpg',
    '/img/8Phases/dernier-croissant.jpg',
    '/img/Transparent/earth.png',
    '/img/Transparent/Jupiter.png',
    '/img/Transparent/Mars.webp',
    '/img/Transparent/Mercure.webp',
    '/img/Transparent/MoonTransparent.png',
    '/img/Transparent/Neptune.webp',
    '/img/Transparent/Pluton.webp',
    '/img/Transparent/Saturn_from_Hubble.png',
    '/img/Transparent/Uranus.png',
    '/img/Transparent/Venus-PNG-Background.png',
];

// Installation : on met tout en cache
self.addEventListener('install', (event) => {
    event.waitUntil(
        caches.open(CACHE_NAME).then((cache) => {
            console.log('[SW] Mise en cache des fichiers...');
            return cache.addAll(FILES_TO_CACHE);
        })
    );
    self.skipWaiting();
});

// Activation : on supprime les anciens caches
self.addEventListener('activate', (event) => {
    event.waitUntil(
        caches.keys().then((keyList) =>
            Promise.all(
                keyList.map((key) => {
                    if (key !== CACHE_NAME) {
                        console.log('[SW] Suppression ancien cache :', key);
                        return caches.delete(key);
                    }
                })
            )
        )
    );
    self.clients.claim();
});

// Fetch : cache d'abord, réseau ensuite (offline-first)
self.addEventListener('fetch', (event) => {
    event.respondWith(
        caches.match(event.request).then((response) => {
            if (response) {
                return response; // Servi depuis le cache
            }
            return fetch(event.request).then((networkResponse) => {
                // On met aussi en cache les nouvelles ressources
                return caches.open(CACHE_NAME).then((cache) => {
                    cache.put(event.request, networkResponse.clone());
                    return networkResponse;
                });
            }).catch(() => {
                // Hors-ligne et pas en cache : page de fallback
                if (event.request.destination === 'document') {
                    return caches.match('/code/accueil.html');
                }
            });
        })
    );
});
