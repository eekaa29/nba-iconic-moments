from django.shortcuts import render
import  requests
# Create your views here.
def get_latest_articles(request):
    team = request.GET.get("team", "")#Obtener el valor de team, en caso de que no lo tenga que sea un string vacío
    api_url = f'https://nba-stories.onrender.com/articles'
    if team:
        api_url += f'?team={team}'
    else:
        api_url
    try:
        response = requests.get(api_url)
        content= response.json()
    except Exception as e :
        content = []
    return render(content,"article/latest_articles.html", {"articles": content})