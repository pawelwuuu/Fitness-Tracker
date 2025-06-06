from django.shortcuts import render, redirect
from tracker.models import ProgressPhoto, DailyWeightEntry
from tracker.forms import ProgressPhotoForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse
from django.template.loader import render_to_string
from django.views.decorators.http import require_POST

@login_required
def photo_upload_view(request):
    if request.method == 'POST':
        form = ProgressPhotoForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            latest_weight_entry = DailyWeightEntry.objects.filter(user=request.user).order_by('-date').first()
            instance.weight = latest_weight_entry.weight_kg if latest_weight_entry else None
            instance.save()
            return redirect('photo_gallery')
    else:
        form = ProgressPhotoForm()
    return render(request, 'tracker/upload_photo.html', {'form': form})

@login_required
def photo_gallery_view(request):
    photos = ProgressPhoto.objects.filter(user=request.user)

    selected_ids = request.GET.getlist('selected', [])
    selected_photos = ProgressPhoto.objects.filter(id__in=selected_ids)

    if request.headers.get('Hx-Request'):
        return render(request, 'tracker/photo_compare_partial.html', {'selected_photos': selected_photos})

    return render(request, 'tracker/photo_gallery.html', {'photos': photos})

@require_POST
@login_required
def compare_photos_view(request):
    ids = request.POST.getlist('compare')
    photos = ProgressPhoto.objects.filter(id__in=ids, user=request.user)
    if photos.count() == 2:
        html = render_to_string('tracker/photo_comparison.html', {'photos': photos})
        return HttpResponse(html)
    return HttpResponse('')
