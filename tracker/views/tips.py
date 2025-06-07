from django.shortcuts import render
from django.core.paginator import Paginator
from tracker.models.exercise_tips import ExerciseTip

def tips_view(request):
    # Pobierz wszystkie aktywne porady
    tips = ExerciseTip.objects.filter(is_active=True).order_by('-created_at')
    
    # Filtrowanie po tagach/kategoriach
    category = request.GET.get('category')
    if category:
        tips = tips.filter(category=category)
    
    # Paginacja - 6 porad na stronę
    paginator = Paginator(tips, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    # Pobierz unikalne kategorie dla filtra
    categories = ExerciseTip.objects.filter(is_active=True).values_list('category', flat=True).distinct()
    
    context = {
        'page_obj': page_obj,
        'categories': categories,
        'selected_category': category,
    }
    return render(request, 'tracker/tips.html', context)