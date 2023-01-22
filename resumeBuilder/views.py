import openai
# from django.views import api_
from rest_framework.decorators import api_view
from django.http import JsonResponse


def gpt3(stext):
    key1 = 'sk-99cdw4MLPoQh6nNyjWWmT3'
    key2 = 'BlbkFJmA2IKhBIvqrH5VM7mCv3'
    openai.api_key = f"{key1}{key2}"
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt="I have learnt %s so what else apart from them should i learn in bullet points answer in less words" % stext,
        temperature=0.5,
        max_tokens=1000,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    content = response.choices[0].text.split('.')
    print(content)
    return response.choices[0].text


@api_view(['GET'])
def resume(request, q):
    response = gpt3(q)
    response = response.strip()
    response = response.strip('\"')
    ans = {'response': response}
    return JsonResponse(ans)
