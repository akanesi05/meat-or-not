from django.shortcuts import render
from django.http import HttpResponse
from .models import FoodItem

def input_view(request):
    if request.method == 'POST':
        food_name = request.POST.get('food_name')
        is_meat = judge_meat(food_name)
        return render(request, 'judge/result.html', {'food_name': food_name, 'is_meat': is_meat})
    return render(request, 'judge/input.html')


def judge_meat(food_name):
    # 簡単な判定ロジック（例）
    meat_list = ['肉', '鶏肉', '豚肉', '牛肉']
    return any(meat in food_name for meat in meat_list)

def result_view(request):
    # 仮の実装。必要に応じて内容を変更してください。
    return render(request, 'judge/result.html')
