Install:
pip install pyrogram tgcrypto pillow python-dotenv tkinterdnd2

Optional (Windows only):
pip install winloop

NOTE ON UPLOAD SPEED
====================
- upload_concurrency in config.json now actually works: Pyrogram's
  Client must be given max_concurrent_transmissions=UPLOAD_CONCURRENCY,
  otherwise all uploads run one-by-one regardless of the setting.
- The single biggest factor is Telegram's SERVER-SIDE throttle for
  non-Premium user accounts (~1-3 MB/s per session). No code change can
  bypass that. Telegram Premium (or a bot account) raises this limit
  substantially.
- A dropped connection mid-upload restarts that file from 0% (Pyrogram
  has no resume). A stable network avoids wasted re-uploads.

Skeshav's personal	-596817933
Skeshav's Library	-1001270052926
Skeshav Books	-4036917143
Secret times	-1001750420393
Skeshava's photoes	-4277211198
Skeshav's Repository	-548929403
