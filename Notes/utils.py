from django.utils.text import slugify
import uuid
def generate_slug(title:str)->str:
    from .models import Notes
    title=slugify(title)
    while(Notes.objects.filter(slug=title).exists()):
        title=slugify(title)+"-"+(str(uuid.uuid4()))[0:4]
    return title