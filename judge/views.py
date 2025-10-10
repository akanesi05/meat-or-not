from django.shortcuts import render
from django.http import HttpResponse
from .models import FoodItem
import random
def top_view(request):
    return render(request, "top.html")


# def input_view(request):
#     if request.method == 'POST':
#         food_name = request.POST.get('food_name')
#         is_meat = judge_meat(food_name)
#         return render(request, 'judge/result.html', {'food_name': food_name, 'is_meat': is_meat})
#     return render(request, 'judge/input.html')
def input_view(request):
    foods = {
    "唐揚げ": False,
    "牛丼": True,
    "チキン南蛮": False,
    "ハンバーグ": True,
    "焼き鳥": False,
    "豚カツ": True,
}
    if request.method == "POST":
        food_name = request.POST.get("food_name")
        user_answer = request.POST.get("answer")
        result = judge_watanabe(food_name, user_answer)
        return render(request, "judge/result.html", {
            "food_name": food_name,
            "correct": result
        })
    food = random.choice(list(foods.keys()))
    return render(request, "judge/input.html", {"food": food})


def judge_watanabe(food_name, user_answer):
    # 渡辺さんの食べ物データベース
    foods = {
        "唐揚げ": False,
        "牛丼": True,
        "チキン南蛮": False,
        "ハンバーグ": True,
        "焼き鳥": False,
        "豚カツ": True,
    }

    # 正解データを取得
    correct_answer = foods.get(food_name)

    # ユーザーの答え（yes/no）を True/False に変換
    user_answer_bool = True if user_answer == "yes" else False

    # 一致していれば正解！
    return correct_answer == user_answer_bool


def result_view(request):
    # 仮の実装。必要に応じて内容を変更してください。
    return render(request, 'judge/result.html')
