# Minimal URL Shortener 

## Configuration
Each of these properties could be set by env variables

`API_PREFIX` - Endpoint prefix - Default: api/

`SHORTENER` - Current URL Shortener strategy - Default: url_manager.services.shorteners.Char8Shortener

`SHORTENER_CACHE_NAME` - Cache name used for store short_name: url pairs - Default: default

`SHORTENER_CACHE_TTL` - Cache TTL - Default: 3600


## Endpoints

1. List all short names defined in database: `GET /api/short-url/`
  ```json
[
    {
      "short_name": "as1234",
      "url": "https://www.google.com",
      "created_at": "2026-05-12 00:00:00",
      "short_url": "http://testserver/api/go/as1234/"
    }
]
```
2. Get specified short name: `GET /api/short-url/<short_name>/`
  ```json
    {
      "short_name": "as1234",
      "url": "https://www.google.com",
      "created_at": "2026-05-12 00:00:00",
      "short_url": "http://testserver/api/go/as1234/"
    }

```

3. Add new URL `POST /api/short-url/`
```json

    {
      "url": "https://test.com/long-address"
    }
```

4. Remove URL `DELETE /api/short-url/<short_name>/`

5. Redirect to specified short URL `GET /api/go/<short_name>/`
