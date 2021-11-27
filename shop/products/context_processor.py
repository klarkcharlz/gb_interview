from .models import Section


def get_sections(get_response):
    sections = Section.objects.all()
    return {'sections': sections}
