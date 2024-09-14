from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.http import JsonResponse
from .forms import TranslationForm
import json, os, uuid
import aiofiles

SAVE_DIR  = "./translations"
os.makedirs(SAVE_DIR, exist_ok= True)

async def index(request):
    if request.method == 'POST':
        form = TranslationForm(request.POST)
        if form.is_valid():
            english_text = form.cleaned_data['english_text']
            lithuanian_text = form.cleaned_data['lithuanian_text']

            data = {
                'EN': english_text,
                'LT': lithuanian_text
            }
            unique_id = str(uuid.uuid4())

            json_file_path = os.path.join(SAVE_DIR, 'translations.json')
            async with aiofiles.open(json_file_path, 'a+', encoding='utf-8') as f:
                await f.seek(0)  # Перемещаемся в начало файла
                try:
                    content = await f.read()
                    existing_data = json.loads(content) if content else {}
                except json.JSONDecodeError:
                    existing_data = {}

                existing_data[unique_id] = data

                await f.seek(0) # Move cursor to begining of file
                await f.truncate()  # Clear old data
                await f.write(json.dumps(existing_data, ensure_ascii=False, indent=4)) # rewrite file

            return HttpResponse("""
                                    <script>
                                        alert("Data saved successfully!");
                                        window.location.href = '{}';
                                    </script>
                                """.format(request.path_info))
    else:
        form = TranslationForm()

    return render(request, 'collect_data/index.html', {'form': form})