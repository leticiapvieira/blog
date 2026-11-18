def site_globals(request):
    return {
        'ownername': 'Letícia Vieira',   # ← Nome do proprietário(a) do site
        'show_aside': True,             # ← Se `False`, `<aside>` é ocultado
    }