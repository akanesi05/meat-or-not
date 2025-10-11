from django.shortcuts import render
from django.http import HttpResponse
from .models import FoodItem
import random

def top_view(request):
    return render(request, "top.html")

print('あ')
# def input_view(request):
#     if request.method == 'POST':
#         food_name = request.POST.get('food_name')
#         is_meat = judge_meat(food_name)
#         return render(request, 'judge/result.html', {'food_name': food_name, 'is_meat': is_meat})
#     return render(request, 'judge/input.html')
def input_view(request):
    like_foods = ["マヨネーズ", "マックのハンバーガー", "ソーセージ"]
    dislike_foods = ["唐揚げ", "チキン南蛮", "焼き鳥","ハンバーグ", "牛丼", "豚カツ"]

    all_foods = like_foods + dislike_foods
    if request.method == "POST":
        food_name = request.POST.get("food_name")
        user_answer = request.POST.get("answer")  # "好き" or "嫌い"
        
        # 正解を取得
        print(food_name)
        if food_name in like_foods:
            correct_answer = "好き"
            
        else:
            correct_answer = "嫌い"
        print(correct_answer)
        # ユーザーが選んだ答えと正解を比較
        correct = (user_answer == correct_answer)
        print(user_answer)
        print(correct)
        return render(request, "judge/result.html", {
            "food_name": food_name,
            "correct": correct,
            "correct_answer": correct_answer
        })
 
    # 出題する食べ物をランダムに選ぶ
    food = random.choice(all_foods)
    return render(request, "judge/input.html", {"food": food})

def judge_watanabe(food_name, user_answer):
    # 渡辺さんの食べ物データベース
  
    # 正解データを取得
    correct_answer = foods.get(food_name)

    # ユーザーの答え（yes/no）を True/False に変換
    user_answer_bool = True if user_answer == "yes" else False

    # 一致していれば正解！
    return correct_answer == user_answer_bool


def result_view(request):
    # 仮の実装。必要に応じて内容を変更してください。
    return render(request, 'judge/result.html')
