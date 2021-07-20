def handle_uploaded_file(f):
    with open('Organization/static/upload_files/site_images/'+f.name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)