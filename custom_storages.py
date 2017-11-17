from django.core.files.storage import get_storage_class
from django.conf import settings
from storages.backends.s3boto import S3BotoStorage
from filebrowser_safe.storage import S3BotoStorageMixin


class CachedS3BotoStorage(S3BotoStorage, S3BotoStorageMixin):

    def __init__(self, *args, **kwargs):
        super(CachedS3BotoStorage, self).__init__(*args, **kwargs)
        self.local_storage = get_storage_class(
            "compressor.storage.CompressorFileStorage")()

    def save(self, name, content):
        name = super(CachedS3BotoStorage, self).save(name, content)
        self.local_storage._save(name, content)
        return name


class MediaStorage(S3BotoStorage, S3BotoStorageMixin):
    location = settings.MEDIAFILES_LOCATION


StaticStorage = lambda: CachedS3BotoStorage(location=settings.STATICFILES_LOCATION)

