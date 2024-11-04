from django.core.files.storage import Storage
from cloudinary import CloudinaryImage
from cloudinary.uploader import upload

class CloudinaryStorage(Storage):
    def _save(self, name, content):
        file_content = content.read()
        upload_result = upload(file_content, public_id=name, resource_type='raw')  # Specify 'raw' for non-image files
        return upload_result['secure_url']

    def url(self, name):
        return CloudinaryImage(name).build_url(resource_type='raw')  # Ensure correct resource type for URL

    def exists(self, name):
        try:
            CloudinaryImage(name).image_info()
            return True
        except Exception:
            return False