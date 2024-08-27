from helm.proxy.services.remote_service import RemoteService
from helm.common.authentication import Authentication
from helm.proxy.accounts import Account
import os

CRFM_API_KEY = os.getenv("CRFM_API_KEY")

auth = Authentication(api_key=CRFM_API_KEY)
service = RemoteService("https://crfm-models.stanford.edu")
account: Account = service.get_account(auth)

model = "gpt4" 
for i, k in enumerate(account.usages[model]):
    print(f"Model: {model}, Usage {i}: {k}: {account.usages[model][k]}")