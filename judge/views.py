from django.shortcuts import render, redirect
import random
from django.shortcuts import render
from django.http import HttpResponse
from .models import FoodItem
import random

def top_view(request):
    return render(request, "top.html")

def input_view(request):
    like_foods = ["マヨネーズ", "マックのハンバーガー", "ソーセージ"]
    dislike_foods = ["唐揚げ", "チキン南蛮", "焼き鳥", "ハンバーグ", "牛丼", "豚カツ","バーガーキングのハンバーガー"]
    all_foods = like_foods + dislike_foods

    # --- セッション初期化 ---
    if "questions" not in request.session:
        # 10問ランダムで出題
        questions = random.sample(all_foods, min(10, len(all_foods)))
        request.session["questions"] = questions
        request.session["current_index"] = 0
        request.session["score"] = 0

    questions = request.session["questions"]
    index = request.session["current_index"]
    score = request.session["score"]

    # --- 全問終わったら結果へ ---
    if index >= len(questions):
        context = {"score": score, "total": len(questions)}
        score = request.session["score"]
        total = len(questions)

        share_text = f"私は {total}問中 {score}問 正解しました！ #渡邉肉 #meat_or_not"

        context = {
            "score": score,
            "total": total,
            "share_text": share_text,
        }
        # セッションをクリア
        for key in ["questions", "current_index", "score"]:
            if key in request.session:
                del request.session[key]
        return render(request, "judge/result.html", context)

    # --- 現在の問題 ---
    food_name = questions[index]

    # --- 回答処理 ---
    if request.method == "POST":
        user_answer = request.POST.get("answer")
        correct_answer = "好き" if food_name in like_foods else "嫌い"
        if user_answer == correct_answer:
            request.session["score"] = score + 1
        request.session["current_index"] = index + 1
        return redirect("judge:input")

    # --- 問題画面を表示 ---
    context = {
        "food": food_name,
        "current": index + 1,
        "total": len(questions),
    }
    return render(request, "judge/input.html", context)
def result_view(request):
    # This view is no longer needed as result is handled in input_view
    return redirect("judge:input")
