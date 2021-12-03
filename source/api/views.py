import requests
from rest_framework import status, mixins
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from api.serializers import AuthSerializer

accsess_token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImp0aSI6IjJiYjM1NGE3ZDIxYjM1MDYwZDkwY2YyZmIzNTFmMThhNWRjYzBjYzg1MWNmOWM3MTc1OWUxOWUyYTM1NGQ4ZDMxM2MwMGE0YzJkMGU3YmI1In0.eyJhdWQiOiI1YzNlNmM1Yi04OWQ4LTQ0NzItOWRmMC00YzZlMjMwNWEzYzgiLCJqdGkiOiIyYmIzNTRhN2QyMWIzNTA2MGQ5MGNmMmZiMzUxZjE4YTVkY2MwY2M4NTFjZjljNzE3NTllMTllMmEzNTRkOGQzMTNjMDBhNGMyZDBlN2JiNSIsImlhdCI6MTYzODQzODUwNSwibmJmIjoxNjM4NDM4NTA1LCJleHAiOjE2Mzg1MjQ5MDUsInN1YiI6Ijc2ODI3MTYiLCJhY2NvdW50X2lkIjoyOTg1MDEwNiwic2NvcGVzIjpbInB1c2hfbm90aWZpY2F0aW9ucyIsImNybSIsIm5vdGlmaWNhdGlvbnMiXX0.fBQnChjWMaBPgXwfmOnfSHPd3SGVTiuo_yhOJah4t6l7DaHGKPEUIvlFI4Mbxixn_4vVpGWIQeW9zYuLe8m2KLDL-nfY7mBCfREVDnSQyQALBbfcTWA3Woicxzc-0w5UTb3nUGwOeO-1ZX2j0-C0rJoKNEyELeGDXSB3HISKnOBRM3uko03x0a733mIN-anpr7nyl01gGXesCaWnjtOLwR3QL2ohhZ0zTkjwkvmFiqG8zqynqeCjaSx35PyqMec2tLeTaT0ieSLtuuzKOK-ERasBE0acfz8N24FV3mVTH1iWJbtXdtR6UcPpSvA6IHBvnLVdgSTozO1HIC4Ltsww5g'

class AuthViewSet(mixins.CreateModelMixin, mixins.ListModelMixin, GenericViewSet):
    serializer_class = AuthSerializer

    def create(self, request, *args, **kwargs):
        data = {
            "client_id": '5c3e6c5b-89d8-4472-9df0-4c6e2305a3c8',
            "client_secret": 'zT7QFYR6NUn6ZKcl2yzKubdQFCwlnSphI5l9bBSZnxvCC9CHjMwMmzLs66pjPkfd',
            "code": 'def5020067ac04ec6d23fb162b713a6b6ae1d62a18a644c2511c00b6d62dd5a433ba31c95a951c069c2380001cde3e17dafd433ac6a1bcb4b7659058f1bdb6676bb7f2a0618b49c583c65540d741d5a9d40ae0bb4b1e808bb99d929b68e0a47664c4c5b5ff048b3524f064c138918b4141e00865a6f86d4958ad108cd83ec0b2228a57980c3e6c025684392264471a5f9bfcc547a335091cea5cc2b8cba3f6f60608026241aa5e65191c6803c4a47c82e17547eb7c47ffdb9d2b0f8cd080eb8e578f0eb0fa98eda02551828e9e0ee0fe0f5173847e11e9ad9bc71f13212b40565d6019ba74eaf4d6f9b260b5afc1e2cefd90b1795784e3cc4ec5b88091e4811534ca2102feb23f84ddc022be15e70d60f48b2cfbb21f214ab3f53f86101050cdae2e8aae7da3035e01e9b86ae6a5595eccda7bf9a62cf3a4572a26d0bd2fe4d56c0a74276c3029ae9ad68908f103925171b0f32f5ce7baea0a0967ae7d40fec93b46a907ffe9fcf5dd336b41a28d3dca6b0a8c14303240b7507b3e98ec8a84c212adaaa60eda6004925963aac2862c6cff2b7057b2a1f7469f227a7c2cc402d3617b256f443897afd114b4379575857c05bf9fd3de85213b1bb8b777ff9a56eff8a74fe88e9df56981efb6dee7',
            "redirect_uri": "https://b95f-46-251-196-81.ngrok.io"
        }

        if request.data['grant_type'] == 'authorization_code':
            data['grant_type'] = 'authorization_code'
        else:
            data['grant_type'] = 'refresh_token'
            data['refresh_token'] = request.data['refresh_token']

        url = 'https://emilrakaev.amocrm.ru/oauth2/access_token/'
        res = requests.post(url, json=data)
        return Response(res.json(), status=status.HTTP_200_OK)


class AmocrmRequest(mixins.ListModelMixin, GenericViewSet):

    def list(self, request, *args, **kwargs):
        url = "https://emilrakaev.amocrm.ru/api/v4/contacts?query=" + request.GET['phone']
        # url = "https://emilrakaev.amocrm.ru/api/v3/contacts?filter[454535]" + request.data['email'] + "&filter[454523]=" + request.data['phone']
        # Ваш вариант который вы предложили в тз у меня не сработал(передавать в фильтр id поля),
        # пришлось через query вытаскивать только телефон (но это не правильно наверное)
        headers = {'Authorization': 'Bearer ' + accsess_token}
        res = requests.get(url, headers=headers)
        if res.status_code == 200:
            id_contact = str(res.json()['_embedded']['contacts'][0]['id'])
            url = "https://emilrakaev.amocrm.ru/api/v4/contacts/" + id_contact
            params = {
                'name': request.GET['name'],
                'custom_fields_values': [
                    {
                        "field_id": 880391,
                        "values": [
                            {
                                "value": request.GET['phone'],
                            }
                        ]
                    },
                    {
                        "field_id": 880393,
                        "values": [
                            {
                                "value": request.GET['email'],
                            }
                        ]
                    }
                ]
            }
            res = requests.patch(url, headers=headers, json=params)

        elif res.status_code == 204:
            params = [{
                'name': request.GET['name'],
                'custom_fields_values': [
                    {
                        "field_id": 880391,
                        "values": [
                            {
                                "value": request.GET['phone'],
                            }
                        ]
                    },
                    {
                        "field_id": 880393,
                        "values": [
                            {
                                "value": request.GET['email'],
                            }
                        ]
                    }
                ]
            }]
            res = requests.post(url, headers=headers, json=params)
        else:
            return Response(res.json())
        if res.json()['id']:
            id_contact = res.json()['id']
        else:
            id_contact = res.json()['_embedded']['contacts'][0]['id']
        params = [{
            'name': 'Im new testing lead',
            "_embedded": {
                "contacts": [
                    {
                        "id": id_contact
                    }
                ]
            }
        }]
        url = "https://emilrakaev.amocrm.ru/api/v4/leads"
        res = requests.post(url, headers=headers, json=params)
        return Response(res.json(), status=status.HTTP_200_OK)
