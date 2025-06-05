from tracker.models.exercise_tips import ExerciseTip

def populate_tips():
    tips = [
        {
            'title': 'Prawidłowa technika przysiadów',
            'content': 'Utrzymuj plecy proste, stopy na szerokość barków, kolana nie powinny wychodzić przed palce stóp.',
            'category': 'STRENGTH'
        },
        {
            'title': 'Optymalne tętno podczas cardio',
            'content': 'Dla najlepszych efektów utrzymuj tętno na poziomie 60-80% swojego maksimum (220 minus wiek).',
            'category': 'CARDIO'
        },
        {
            'title': 'Rozciąganie po treningu',
            'content': 'Po każdym treningu poświęć 5-10 minut na rozciąganie głównych grup mięśniowych.',
            'category': 'FLEXIBILITY'
        },
        {
            'title': 'Nawodnienie organizmu',
            'content': 'Pij minimum 2-3 litry wody dziennie, a podczas treningu 500ml na każdą godzinę ćwiczeń.',
            'category': 'NUTRITION'
        },
        {
            'title': 'Regeneracja mięśni',
            'content': 'Mięśnie potrzebują 48-72 godzin na regenerację po intensywnym treningu siłowym.',
            'category': 'RECOVERY'
        },
        {
            'title': 'Technika martwego ciągu',
            'content': 'Utrzymuj proste plecy, sztangę blisko ciała, ruch zaczynaj z nóg, nie z pleców.',
            'category': 'STRENGTH'
        },
        {
            'title': 'Interwały treningowe',
            'content': 'Stosuj stosunek pracy do odpoczynku 1:2 (np. 30s sprintu, 1min marszu) dla najlepszych efektów.',
            'category': 'CARDIO'
        },
        {
            'title': 'Białko w diecie',
            'content': 'Spożywaj 1.6-2.2g białka na kg masy ciała dziennie dla optymalnej regeneracji mięśni.',
            'category': 'NUTRITION'
        },
        {
            'title': 'Sen a regeneracja',
            'content': '7-9 godzin snu to optymalny czas dla pełnej regeneracji organizmu po treningu.',
            'category': 'RECOVERY'
        },
        {
            'title': 'Technika pompek',
            'content': 'Utrzymuj ciało w linii prostej, łokcie pod kątem 45 stopni do tułowia.',
            'category': 'STRENGTH'
        }
    ]

    created_count = 0
    for tip in tips:
        _, created = ExerciseTip.objects.get_or_create(
            title=tip['title'],
            defaults={
                'content': tip['content'],
                'category': tip['category'],
                'is_active': True
            }
        )
        if created:
            created_count += 1

    return f"Dodano {created_count} nowych porad. Łącznie w bazie: {ExerciseTip.objects.count()} porad."

if __name__ == '__main__':
    print(populate_tips())