from django.core.management.base import BaseCommand
import subprocess
from django.conf import settings

class Command(BaseCommand):
    help = 'Start RTSP to HLS transcoding'

    def handle(self, *args, **options):
        media_path = settings.MEDIA_ROOT
        subprocess.run([
            'ffmpeg',
            '-rtsp_transport', 'tcp',
            '-i', 'rtsp://pool250:_250_pool@45.152.168.61:52037',
            '-c:v', 'libx265',
            '-preset', 'fast',
            '-crf', '28',
            '-sc_threshold', '0',
            '-g', '48',
            '-keyint_min', '48',
            '-hls_time', '4',
            '-hls_list_size', '5',
            '-hls_flags', 'delete_segments',
            '-f', 'hls',
            f'{media_path}/stream.m3u8'
        ])