from ..models import *
import os
from .. import settings as app_settings


class HlsStreamService:
    def init_channel_space(self, stream_name):
        output_path = os.path.join(app_settings.HLS_STREAM_ROOT, stream_name)
        if not os.path.exists(output_path):
            os.makedirs(output_path)
        for file in os.listdir(output_path):
            os.remove(os.path.join(output_path, file))
        return output_path

    def deploy_transcode_daemon(self, channel_object):
        import subprocess
        input_path = channel_object.rtsp_url
        stream_name = channel_object.stream_name
        output_path = self.init_channel_space(stream_name)
        f_null = open(os.devnull, 'w')
        execution_process = subprocess.Popen(self.ffmpeg_command_builder(input_path, stream_name, output_path), stdout=f_null)
        return execution_process.pid

    def ffmpeg_command_builder(self, rtsp_url, nickname, output_path):
        from urllib.parse import urlparse
        import os

        ffmpeg_command = app_settings.FFMPEG_PATH
        command = [ffmpeg_command, '-hide_banner', '-loglevel', 'error', '-y', '-fflags', 'nobuffer']

        if urlparse(rtsp_url).scheme == 'rtsp':
            command.extend(['-rtsp_transport', 'tcp'])

        command.extend([
            '-i', rtsp_url,
            '-vsync', 'drop',
            '-an',

            '-c:v', 'libx264',
            '-preset', 'ultrafast',
            '-tune', 'zerolatency',
            '-pix_fmt', 'yuv420p',

            '-f', 'hls',
            '-hls_flags', 'delete_segments+append_list',
            '-hls_time', '5',
            '-hls_list_size', '3',
            '-hls_segment_filename', os.path.join(output_path, '%d.ts'),
            '-segment_list_flags', '+live',

            # Выходной файл
            os.path.join(output_path, 'index.m3u8')
        ])

        return command

    def channel_ready(self, stream_name):
        stream_path = os.path.join(app_settings.HLS_STREAM_ROOT, stream_name)
        fragment_count = 0
        for file in os.listdir(stream_path):
            if file.split('.')[-1] == "ts":
                fragment_count += 1
        return fragment_count > 1

    def setup_pids(self):
        for channel in PoolStream.objects.all():
            channel.transcode_pid = 0
            channel.save()
        print('PIDs ready')
