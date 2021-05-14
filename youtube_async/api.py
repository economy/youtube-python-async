import httpx


class API:
    _client_id = None
    _client_secret = None
    _api_key = None
    _access_token = None
    _api_base_url = 'https://www.googleapis.com/youtube/v3/'
    _part = 'id,snippet'
    _async_client = httpx.AsyncClient()

    def __init__(self, client_id, client_secret, api_key, access_token=None, api_url=None, timeout=5):
        self._client_id = client_id
        self._client_secret = client_secret
        self._api_key = api_key
        self._access_token = access_token
        self._async_client = httpx.AsyncClient(timeout=timeout)
        if api_url:
            self._api_base_url = api_url

    async def get(self, endpoint, **kwargs):
        if self._access_token:
            kwargs['access_token'] = self._access_token
        else:
            kwargs['key'] = self._api_key

        if 'part' not in kwargs:
            kwargs['part'] = self._part

        return self.response(await self._get(self._api_base_url+endpoint, params=kwargs))

    async def post(self, endpoint, **kwargs):
        if self._access_token:
            kwargs['access_token'] = self._access_token
        else:
            kwargs['key'] = self._api_key

        return self.response(await self._post(self._api_base_url + endpoint, params=kwargs))

    async def get_profile(self):
        return self.response(await self._get(
            'https://www.googleapis.com/oauth2/v1/userinfo',
            {'access_token': self._access_token}
        ))

    async def _get(self, url, params=None, **kwargs):

        try:
            result = await self._async_client.get(url, params=params, **kwargs)
            result.raise_for_status()
            return result
        except httpx.HTTPStatusError as exc:
            print(f"Error response {exc.response.status_code} while requesting {exc.request.url!r}.")

    async def _post(self, url, params=None, **kwargs):

        try:
            result = await self._async_client.post(url, params=params, **kwargs)
            result.raise_for_status()
            return result
        except httpx.HTTPStatusError as exc:
            print(f"Error response {exc.response.status_code} while requesting {exc.request.url!r}.")

    @staticmethod
    def response(response):
        return response.json()
