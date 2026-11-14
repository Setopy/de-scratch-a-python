// Service worker for the "De Scratch a Python" site (setopy.github.io/de-scratch-a-python).
// Keeps the page, icons and the PDF on the device so the book opens offline.
// Bump VERSION whenever the page or the PDF changes, so installed apps pick up the new files.
const VERSION = 'v2-2026-11-14';
const CACHE = 'de-scratch-a-python-' + VERSION;
const CORE = [
  './',
  './index.html',
  './manifest.webmanifest',
  './icons/icon-192.png',
  './icons/icon-512.png',
  './icons/icon-maskable-512.png',
  './icons/apple-touch-icon.png',
  './icons/favicon-48.png',
];
const PDF = './de-scratch-a-python.pdf';

self.addEventListener('install', (event) => {
  event.waitUntil((async () => {
    const cache = await caches.open(CACHE);
    await cache.addAll(CORE);
    // The PDF is large (about 1.5 MB); fetch it too, but don't fail the install if it can't.
    try { await cache.add(PDF); } catch (e) { /* fetched later on first open */ }
    await self.skipWaiting();
  })());
});

self.addEventListener('activate', (event) => {
  event.waitUntil((async () => {
    const keys = await caches.keys();
    await Promise.all(keys.filter((k) => k.startsWith('de-scratch-a-python-') && k !== CACHE)
      .map((k) => caches.delete(k)));
    await self.clients.claim();
  })());
});

self.addEventListener('fetch', (event) => {
  const req = event.request;
  if (req.method !== 'GET') return;
  const url = new URL(req.url);
  if (url.origin !== self.location.origin) return; // Colab, GitHub: always go to the network

  // Pages: network first, so updates show up; fall back to the saved copy offline.
  if (req.mode === 'navigate') {
    event.respondWith((async () => {
      try {
        const fresh = await fetch(req);
        const cache = await caches.open(CACHE);
        cache.put('./index.html', fresh.clone());
        return fresh;
      } catch (e) {
        return (await caches.match('./index.html')) || (await caches.match('./')) || Response.error();
      }
    })());
    return;
  }

  // Everything else in /es/ (icons, manifest, PDF): saved copy first, then the network.
  event.respondWith((async () => {
    const cached = await caches.match(req, { ignoreSearch: true });
    if (cached) return cached;
    const fresh = await fetch(req);
    if (fresh.ok && url.pathname.startsWith(new URL('./', self.location).pathname)) {
      const cache = await caches.open(CACHE);
      cache.put(req, fresh.clone());
    }
    return fresh;
  })());
});
